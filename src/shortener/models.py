from .utils import code_generator
from django.db import models

# Create your models here.



class shortener(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
	

	def save(self, *args, **kwargs):
		print("something")
		self.shortcode = code_generator()
		super(shortener, self).save(*args , **kwargs)





	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url) 



'''
python manage.py makemigration
python manage.py migrate
python manage.py createsuperuser
'''