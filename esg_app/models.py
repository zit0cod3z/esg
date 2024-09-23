from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Registration(models.Model):
	name= models.CharField(max_length=200)
	nationality= models.CharField(max_length=200)
	email= models.EmailField(null=True, max_length=200)
	organization= models.CharField(max_length=200)
	position = models.CharField(null=True, blank=True, max_length=200)
	industry = models.CharField(max_length=200)
	event= models.CharField(blank=True, null=True, max_length=2000)
	submitted_at= models.DateTimeField(auto_now_add=True)

	class Meta():
		ordering = ('-submitted_at',)

	def __str__(self):
		return f'Registration by {self.name} from a {self.nationality} at {self.submitted_at} attending {self.event}'