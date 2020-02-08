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
		context = {
			"title": "Submit URL",
			"form": form
		}
		template = "shortener/home.html"
		if form.is_valid():
			new_url = from.cleaned_data.get("url")
			obj, created = shortener.objects.get_or_created(url=new_url)
			context = {
				"object": obj,
				"created":created,
			}

		if created:
			template = "shortener/success.html"
		else:
			template = "shortener/already-exists.html"


		return render(request, template, context)



class URLRedirectView(View):   # class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(shortener, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)
