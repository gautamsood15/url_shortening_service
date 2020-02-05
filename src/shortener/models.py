from django.db import models



from .utils import code_generator, create_shortcode

# Create your models here.

class shortenerManager(models.Manager):
	
	def all(self , *args , **kwargs):
		qs_main = super(shortenerManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs


class shortener(models.Model):
	url       = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	active    = models.BooleanField(default=True)
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
	


	objects = shortenerManager()
	#some_random = shortenerManager()



	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":	
			self.shortcode = create_shortcode(self)
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