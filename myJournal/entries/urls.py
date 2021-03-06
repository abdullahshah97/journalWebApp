from django.conf.urls import url
from . import views

"""URLs for entries"""

app_name = 'entries'

urlpatterns = [
    # Home
    url(r'^$', views.index, name='index'),
    url(r'^titles/$', views.titles, name='titles'),
    url(r'^titles/(?P<titles_id>\d+)/$', views.title, name='title'),
    url(r'^new_title/$', views.new_title, name='new_title'),
    url(r'^new_entry/(?P<title_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    url(r'^all_posts/$', views.all_posts, name='all_posts'),
    url(r'^delete_entry/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry'),
    url(r'^delete_title/(?P<title_id>\d+)/$', views.delete_title, name='delete_title'),

]
