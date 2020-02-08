from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import shortener

# Create your views here.

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "home.html", {})






class URLCBView(View):   # class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(shortener, shortcode=shortcode)
		return HttpResponse(obj.url)
