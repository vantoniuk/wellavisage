from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^template$', views.template, name='picture-template'),
	url(r'^insert/$', views.insert, name='insert'),
	url(r'^list/([0-9]+)/([0-9]{1,2})/([0-9]{1,2})/$', views.list, name='views-list'),
]