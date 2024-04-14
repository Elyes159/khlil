from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import FileResponse, JsonResponse
from .models import Todo
import pyembroidery # type: ignore
from django.conf import settings
import os
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['POST', 'GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@xframe_options_exempt
def upload_file(request, extension):
    if request.method == "POST":
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            try:
                instance = Todo(attachment=uploaded_file)
                instance.save()
                return JsonResponse({'message': 'File uploaded successfully', 'file_id': instance.id}, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'No file provided in the request'}, status=400)
    elif request.method == "GET":
        last_uploaded_file = Todo.objects.last()
        if last_uploaded_file:
            try:
                attached_file_path = os.path.join(settings.MEDIA_ROOT, str(last_uploaded_file.attachment))
                
                converted_file_path = os.path.join(settings.MEDIA_ROOT, "converted1." + extension)
                
                pyembroidery.convert(attached_file_path, converted_file_path)

                # Vérifier si le fichier .pes converti existe avant de le renvoyer
                if os.path.exists(converted_file_path):
                    return FileResponse(open(converted_file_path, 'rb'), content_type='application/octet-stream')
                else:
                    return JsonResponse({'error': 'File not found'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'No file uploaded yet'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
