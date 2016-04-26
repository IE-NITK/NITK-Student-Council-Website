from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import website.urls
import smriti.urls
import website.views as websiteviews
from . import views

urlpatterns = [
    url(r'^$', websiteviews.homePage, name='home'), #DO NOT remove this line!
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^', include(website.urls, namespace='website')),
    url(r'^smriti/', include(smriti.urls, namespace='smriti')),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^django-rq/', include('django_rq.urls')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
