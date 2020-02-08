from django.conf.urls import url
from django.contrib import admin

from shortener.views import url_redirect_view, URLCBView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    #url(r'^(?P<shortcode>[\w-]+){6,15}$', url_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+){6,15}$', URLCBView.as_view())
]
