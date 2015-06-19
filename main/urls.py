from django.conf.urls import patterns, url, include
from django.utils.translation import gettext as _
from main.admin import dashboard
from main.views import PersonCreateView, PersonListView, PersonDetailView, PersonUpdateView, MinuteListView, \
    MinuteCreateView, MinuteUpdateView, MinuteDetailView, MonthBirthdayReportView

urlpatterns = patterns('',
    url(_(r'^/person$'), PersonListView.as_view(admin_site=dashboard), name="main_person"),
    url(_(r'^/person/add$'), PersonCreateView.as_view(admin_site=dashboard), name="main_person_add"),
    url(_(r'^/person/(?P<pk>[0-9]+)'), include([
        url(_(r'[/]$'), PersonDetailView.as_view(admin_site=dashboard), name="main_person_detail"),
        url(_(r'/edit$'), PersonUpdateView.as_view(admin_site=dashboard), name="main_person_edit"),
    ])),
    url(_(r'^/minute$'), MinuteListView.as_view(admin_site=dashboard), name="main_minute"),
    url(_(r'^/minute/add$'), MinuteCreateView.as_view(admin_site=dashboard), name="main_minute_add"),
    url(_(r'^/minute/(?P<pk>[0-9]+)'), include([
        url(_(r'[/]$'), MinuteDetailView.as_view(admin_site=dashboard), name="main_minute_detail"),
        url(_(r'/edit$'), MinuteUpdateView.as_view(admin_site=dashboard), name="main_minute_edit"),
    ])),
)
