from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import shortener

# Create your views here.

def url_redirect_view(request, shortcode=None, *args, **kwargs):     # FXN based view
	#print(request.user)
	#print(request.user.is_authenticated())
	#obj = shortener.objects.get(shortcode=shortcode)
	

	obj = get_object_or_404(shortener, shortcode=shortcode)
	obj_url = obj.url

	#try:
	#	obj = shortener.objects.get(shortcode=shortcode)
	#except:
	#	obj = shortener.objects.all().first()
	
	#obj_url = None	
	#qs = shortener.objects.filter(shortcode__iexact=shortcode.upper())
	#if qs.exists() and qs.count() == 1:
	#	obj = qs.first()
	#	obj_url = obj.url

	return HttpResponse("hello {sc}".format(sc=obj.url))


class URLCBView(View):   # class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		return HttpResponse("hello again  {sc}".format(sc=shortcode))


