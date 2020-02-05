from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

def url_redirect_view(request, *args, **kwargs):     # FXN based view
	return HttpResponse("hello")


class URLCBView(View):   # class based view
	def get(self, request, *args, **kwargs):
		return HttpResponse("hello again")

