from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register$', views.register, name='register'),
	url(r'^token$', views.token, name='token'),
	url(r'^submit$', views.create, name='create'),
	url(r'^api/retrieve$', views.retrieve, name='retrieve'),
]