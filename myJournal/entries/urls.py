from django.conf.urls import url
from . import views

"""URLs for entries"""

urlpatterns = [
    #Home
    url(r'^$', views.index, name='index'),
    url(r'^titles/$', views.titles, name='titles'),
    url(r'^titles/(?P<titles_id>\d+)/$', views.title, name='title'),
    url(r'^new_title/$', views.new_title, name='new_title'),
]
