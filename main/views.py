from django.core.urlresolvers import reverse_lazy
from django.utils.translation import gettext as _
from dashboard_view.views import DashboardView, DashboardMenu, DashboardCreateView, DashboardUpdateView, \
    DashboardListView, DashboardDetailView
from main.forms import PersonForm
from main.models import UserProfile

menu_dict = [
    {'name': 'overview', 'icon_class': 'fa-dashboard', 'verbose_name': _('Overview'),
     'link': reverse_lazy('dashboard_overview')},
    {'name': 'main', 'icon_class': 'fa-users', 'verbose_name': _('People'), 'children':
        [
            {'name': 'person', 'verbose_name': _('Person'), 'link': reverse_lazy('main_person')},
        ]},

]
DashboardView.menu = DashboardMenu(menu=menu_dict)


class DashboardAccountedListView(DashboardListView):
    def get_queryset(self):
        queryset = super(DashboardAccountedListView, self).get_queryset()

        if (hasattr(queryset.model, 'accounted')):
            if hasattr(self.request.user,'userprofile'):
                queryset = queryset.filter(church_account=self.request.user.userprofile.church_account)

        return queryset


class PersonCreateView(DashboardCreateView):
    model = UserProfile
    form_class = PersonForm
    pass

class PersonUpdateView(DashboardUpdateView):
    pass

class PersonListView(DashboardAccountedListView):
    model = UserProfile
    fields = ['user.get_full_name']

class PersonDetailView(DashboardDetailView):
    pass