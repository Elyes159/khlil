from django.contrib import admin

from api_wordpress.models import Todo




@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    list_display = ['attachment']
    
