import uuid
from django.db import models
from private_storage.fields import PrivateFileField # type: ignore


class Todo(models.Model):
    
    file_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    attachment = models.FileField(upload_to='public', null=True)


