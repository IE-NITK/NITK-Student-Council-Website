from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views
import website.views as websiteviews

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^message/$', views.MessagePage.as_view(), name='message'),
    url(r'^represent/', views.represent.as_view(), name='represent'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calendar/$', websiteviews.calEvents),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^clublife/', views.ClubLifePage.as_view(), name='club'),
    url(r'^news/', views.NewsPage.as_view(), name='news'),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
