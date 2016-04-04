from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^home/', views.HomePage.as_view(), name='home'),
    ]
