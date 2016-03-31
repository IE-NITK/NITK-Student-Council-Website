from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homePage, name='home'),
    url(r'^message/$', views.MessagePage.as_view(), name='message'),
    url(r'^represent/', views.represent.as_view(), name='represent'),
    url(r'^calendar/$', views.calEvents, name='calendar'),
    url(r'^announce/', views.announcements, name='announce'),
    url(r'^contacts/',views.ContactNumbers.as_view(),name='contacts'),
    url(r'^nitk_life/', views.NitkLifePage.as_view(), name='nitk_life'),
    url(r'^news/$', views.newsPage, name='news'),
    url(r'^news/(?P<num>[0-9]+)/$', views.newsPage, name='eachNews'),
    url(r'^faq/',views.FAQ.as_view(),name='faq'),
	url(r'^resources/',views.Resources.as_view(),name='resources'),
    url(r'^senate/',views.SenatePage.as_view(),name='senate'),
]
