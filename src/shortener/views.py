from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import shortener

# Create your views here.

def home_view_fbv(request, *args, **kwargs):
	if request.method == "POST":
		print(request.POST)
	return render(request, "shortener/home.html", {})


class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "Submit URL",
			"form": the_form
		}
		return render(request, "shortener/home.html", context)


	def post(self, request, *args, **kwargs):
		from = SubmitUrlForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data.get("url"))
		

		context = {
			"title": "Submit URL",
			"form": form
		}

		return render(request, "shortener/home.html", context)



class URLCBView(View):   # class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(shortener, shortcode=shortcode)
		return HttpResponse(obj.url)
