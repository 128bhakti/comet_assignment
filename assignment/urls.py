from django.conf.urls import url
from . import views
from . import models
urlpatterns = [
		url(r'^$',views.index, name='index'),
		url(r'^',views.medium_crawl, name='medium_crawl')
]