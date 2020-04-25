from django.db import models
from datetime import datetime
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
	category_title = models.CharField(max_length = 200)
	category_image = models.ImageField(upload_to ="uploads/")
	category_summary = models.TextField()
	category_slug = models.CharField(max_length = 200,default = 1)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_title


class Receipe(models.Model):
	title = models.CharField(max_length = 200)
	image = models.ImageField(upload_to ="uploads/")
	text = models.TextField()
	time = models.DateTimeField("Date Published",default = datetime.now())
	category_title = models.ForeignKey(Category,default = 1,verbose_name = "Receipe",on_delete = models.SET_DEFAULT)
	receipe_slug = models.CharField(max_length = 200,default = 1)
	bookmarked_receipe = models.ManyToManyField(settings.AUTH_USER_MODEL,through = 'Bookmark',related_name="receipe")

	def __str__(self):
		return self.title

class Comment(models.Model):
	title = models.ForeignKey(Receipe,default = 1,verbose_name = "comment",on_delete = models.SET_DEFAULT)
	name = models.CharField(max_length = 200)
	email = models.EmailField(validators = [validate_email])
	text = models.TextField()
	created_on = models.DateTimeField(default = datetime.now())
	active = models.BooleanField(default = False)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return f'Comment by: {self.name}---{self.text}'

class Bookmark(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name = 'bookmark',on_delete = models.SET_NULL,null = True)
	receipe = models.ForeignKey(Receipe,related_name = 'bookmark',on_delete = models.SET_NULL,null=True)
	bookmark_or_not = models.BooleanField(default = True)

	def __str__(self):
		return f'{self.user}:{self.receipe}'

