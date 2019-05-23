from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	file_name = models.CharField(max_length=400)
	unzip_path = models.CharField(max_length=400)
	zip_file = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

class Patch(models.Model):
	title = models.CharField(max_length=400)
	description = models.CharField(max_length=1000)
	created_at = models.DateTimeField('date published')


class Vulnerability(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=400)
	line_no = models.IntegerField(default=20)
	file = models.ForeignKey(File, on_delete=models.CASCADE)
	patch = models.ForeignKey(Patch, on_delete=models.CASCADE)
	created_at = models.DateTimeField('date published')