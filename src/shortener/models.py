from django.db import models



from .utils import code_generator, create_shortcode

# Create your models here.

class shortenerManager(models.Manager):
	
	def all(self , *args , **kwargs):
		qs_main = super(shortenerManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs


	def refresh_shortcode(self, items=None):
		qs = shortener.objects.filter(id__gte=1) 
		if items is not None and isinstance(items, int):
			qs = qs.order_by('-id')[:items]
		new_codes = 0			
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.id)
			q.save()
			new_codes += 1
		return "New codes made: {i}".format(i=new_codes)




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


#class Meta:
#	ordering = '-id'







	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url) 



'''
python manage.py makemigration
python manage.py migrate
python manage.py createsuperuser

'''