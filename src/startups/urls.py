from django.conf.urls import url
from . import views

app_name = 'startups'

urlpatterns = [
	#/startups/
	url('^$',views.IndexView.as_view(),name='index'),

	# /startups/id/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

	# /startups/startup_id/event_id/
	url(r'^[0-9]+/(?P<pk>[0-9]+)/$', views.EventView.as_view(), name='event'),

]  