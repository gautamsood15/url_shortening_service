from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import shortener

# Create your views here.

def url_redirect_view(request, shortcode=None, *args, **kwargs):     # FXN based view
	obj = get_object_or_404(shortener, shortcode=shortcode)
	return HttpResponse(obj.url)


class URLCBView(View):   # class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(shortener, shortcode=shortcode)
		return HttpResponse(obj.url)


	def post(self, request, *args, **kwargs):
		return HttpResponse()
