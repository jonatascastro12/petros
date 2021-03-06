"""petros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from dashboard_view.views import LoginView, LogoutView
import main
from main.views import PetrosDashboardOverviewView, PetrosDashboardProfileView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^dashboard/$', PetrosDashboardOverviewView.as_view(), name="dashboard_overview"),
    url(r'^dashboard/profile/$', PetrosDashboardProfileView.as_view(), name="dashboard_profile"),

    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),

    url(r'^', include('crop_image.urls')),
    url(r'^dashboard_utils/', include('dashboard_view.urls')),

    url(r'^main', include('main.urls')),

    url(r'^tinymce/', include('tinymce.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)