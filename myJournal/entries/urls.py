from django.conf.urls import url
from . import views

"""URLs for entries"""

urlpatterns = [
    #Home
    url(r'^$', views.index, name='index'),
    url(r'^titles/$', views.titles, name='titles'),
]