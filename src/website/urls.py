from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homePage, name='home'),
    url(r'^message/$', views.MessagePage.as_view(), name='message'),
    url(r'^represent/', views.represent.as_view(), name='represent'),
    url(r'^calendar/$', views.calEvents, name='calendar'),
    url(r'^clublife/', views.ClubLifePage.as_view(), name='club'),
    url(r'^announce/', views.announcements, name='announce'),
    url(r'^contacts/',views.ContactNumbers.as_view(),name='contacts'),
    url(r'^nitk_life/', views.NitkLifePage.as_view(), name='nitk_life'),
]
