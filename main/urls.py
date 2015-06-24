from django.conf.urls import patterns, url, include
from django.utils.translation import ugettext as _
from main.admin import dashboard
from main.views import PersonCreateView, PersonListView, PersonDetailView, PersonUpdateView, MinuteListView, \
    MinuteCreateView, MinuteUpdateView, MinuteDetailView, MonthBirthdayReportView, GroupCreateView, GroupListView, \
    GroupDetailView, GroupUpdateView

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
    url(_(r'^/cells$'), GroupListView.as_view(admin_site=dashboard, group_type="cell"), name="main_cell"),
    url(_(r'^/cells/add$'), GroupCreateView.as_view(admin_site=dashboard, group_type="cell"), name="main_cell_add"),
    url(_(r'^/cells/(?P<pk>[0-9]+)'), include([
        url(_(r'[/]$'), GroupDetailView.as_view(admin_site=dashboard, group_type="cell"), name="main_cell_detail"),
        url(_(r'/edit$'), GroupUpdateView.as_view(admin_site=dashboard, group_type="cell"), name="main_cell_edit"),
    ])),
)
