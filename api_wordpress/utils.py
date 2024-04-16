import os
from django.http import HttpResponse, JsonResponse
from django.conf import settings

def download_file(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename="' + os.path.basename(file_path) + '"'
            return response
    else:
        return JsonResponse({'error': 'File not found'}, status=404)
