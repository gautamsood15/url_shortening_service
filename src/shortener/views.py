from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import shortener

# Create your views here.

def url_redirect_view(request, shortcode=None, *args, **kwargs):     # FXN based view
	#print(request.user)
	#print(request.user.is_authenticated())
	obj = shortener.objects.get(shortcode=shortcode)
	return HttpResponse("hello {sc}".format(sc=obj.url))


class URLCBView(View):   # class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		return HttpResponse("hello again  {sc}".format(sc=shortcode))


