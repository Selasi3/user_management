from django.db import models

# Create your models here.
class FileUpload(models.Model):
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to="media")