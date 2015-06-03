from django.conf.urls import patterns, url, include
from django.utils.translation import gettext as _
from main.views import PersonCreateView, PersonListView, PersonDetailView, PersonUpdateView

urlpatterns = patterns('',
    url(_(r'^/person$'), PersonListView.as_view(), name="main_person"),
    url(_(r'^/person/add$'), PersonCreateView.as_view(), name="main_person_add"),
    url(_(r'^/person/(?P<pk>[0-9]+)'), include([
        url(_(r'[/]$'), PersonDetailView.as_view(), name="main_person_detail"),
        url(_(r'/edit$'), PersonUpdateView.as_view(), name="main_person_edit"),
    ])),
)
