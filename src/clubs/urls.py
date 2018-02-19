from django.conf.urls import url
from . import views

app_name = 'clubs'

urlpatterns = [
	#/clubs/
	url('^$',views.IndexView.as_view(),name='index'),

	# /clubs/id/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

	# /clubs/club_id/event_id/
	url(r'^[0-9]+/(?P<pk>[0-9]+)/$', views.EventView.as_view(), name='event'),

]  