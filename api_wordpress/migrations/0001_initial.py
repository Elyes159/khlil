# Generated by Django 4.2.11 on 2024-04-14 09:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('attachment', models.FileField(null=True, upload_to='public')),
            ],
        ),
    ]
