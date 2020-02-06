from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import shortener

# Create your views here.

def url_redirect_view(request, shortcode=None, *args, **kwargs):     # FXN based view
	#print(request.user)
	#print(request.user.is_authenticated())
	#obj = shortener.objects.get(shortcode=shortcode)
	print('method is \n')
	print(request.method)

	obj = get_object_or_404(shortener, shortcode=shortcode)
	return HttpResponse("hello {sc}".format(sc=obj.url))


class URLCBView(View):   # class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(shortener, shortcode=shortcode)
		return HttpResponse("hello again  {sc}".format(sc=shortcode))


	def post(self, request, *args, **kwargs):
		return HttpResponse()
