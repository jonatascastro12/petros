from django.conf.global_settings import SHORT_DATE_FORMAT
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect
from django.utils import formats
from django.utils.translation import gettext as _
from django.views.generic.base import View
from dashboard_view.dashboard_widgets import DashboardWidget
from dashboard_view.views import DashboardView, DashboardMenu, DashboardCreateView, DashboardUpdateView, \
    DashboardListView, DashboardDetailView, DashboardOverviewView, DashboardProfileView
from main.dashboard_widgets import PetrosDashboardWidget
from main.forms import PersonForm_Basic, PersonForm_Personal, PersonForm_Contact, PersonForm, UserForm, \
    UserFormNoPassword, PersonForm_Ecclesiastic, MinuteForm
from main.models import UserProfile, Minute

menu_dict = [
    {'name': 'overview', 'icon_class': 'fa-dashboard', 'verbose_name': _('Overview'),
     'link': reverse_lazy('dashboard_overview')},
    {'name': 'main', 'icon_class': 'fa-users', 'verbose_name': _('People'), 'children':
        [
            {'name': 'person', 'verbose_name': _('Person'), 'link': reverse_lazy('main_person'),
             'icon_class': 'fa-user', },
            {'name': 'minutes', 'verbose_name': _('Minutes'), 'link': reverse_lazy('main_minute'),
             'icon_class': 'fa-file-text-o', },
        ]},
    {'name': 'reports', 'icon_class': 'fa-file-text', 'verbose_name': _('Reports'), 'children':
        [
            {'name': 'month_birthday', 'verbose_name': _('Month Birthday'),
             'link': reverse_lazy('main_report_month_birthday'), 'icon_class': 'fa-birthday-cake', },
        ]},

]
DashboardView.menu = DashboardMenu(menu=menu_dict)

class PetrosDashboardOverviewView(DashboardOverviewView):
    template_name = "dashboard_base.html"
    widgets_list = [
        ('person_statistics',),
        ('last_signups',),
        ('person_month_birthday',),
    ]
    widget_class = PetrosDashboardWidget

DashboardView.widget_class = PetrosDashboardWidget

class PetrosDashboardProfileView(DashboardProfileView):
    template_name = "dashboard_base.html"


class DashboardAccountedView(View):
    
    def form_valid(self, *args, **kwargs):
        if kwargs['form']:
            print 'ok'
        return super(DashboardAccountedView, self).form_valid(*args, **kwargs)
    
    def get_queryset(self):
        queryset = super(DashboardAccountedView, self).get_queryset()

        if (hasattr(queryset.model, 'accounted')):
            if hasattr(self.request.user,'userprofile'):
                queryset = queryset.filter(church_account=self.request.user.userprofile.church_account)

        return queryset


class PersonCreateView(DashboardCreateView):
    model = UserProfile
    form_class = PersonForm

    def get_success_url(self):
        return reverse('main_person_edit', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = None

        form = self.get_form()
        form_user = UserForm(request.POST)
        form_basic = PersonForm_Basic(request.POST)
        form_personal = PersonForm_Personal(request.POST)
        form_contact = PersonForm_Contact(request.POST)
        form_ecclesiastic = PersonForm_Ecclesiastic(request.POST)

        if form_basic.is_valid() and form_user.is_valid() and form_personal.is_valid() and form_contact.is_valid() and \
                form_ecclesiastic.is_valid():
            return self.form_valid(form, form_user, form_basic)
        else:
            return self.form_invalid(form_basic, form_user, form_personal, form_contact, form_ecclesiastic)

    def form_valid(self, form, form_user, form_basic):
        user = form_user.save()
        form.instance.user = user
        form.instance.church_account = self.request.user.userprofile.church_account

        self.object = form.save()

        model_name = self.model._meta.verbose_name
        if self.object:
            object_name = ' ' + self.object.__unicode__() + ' '
        else:
            object_name = ' ' + form.instance.__unicode__() + ' '

        # LogEntry.objects.log_action(self.request.user.id, )
        messages.success(self.request, message=model_name + object_name + _('created successfully!'))

        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form_basic, form_user, form_personal, form_contact, form_ecclesiastic):
        return self.render_to_response(self.get_context_data(form_basic=form_basic,
                                                             form_user=form_user,
                                                             form_personal=form_personal,
                                                             form_contact=form_contact,
                                                             form_ecclesiastic=form_ecclesiastic))

    def get_context_data(self, **kwargs):
        context = super(PersonCreateView, self).get_context_data(**kwargs)

        context['form_basic'] = PersonForm_Basic() if not 'form_basic' in kwargs else kwargs['form_basic']
        context['form_user'] = UserForm() if not 'form_user' in kwargs else kwargs['form_user']
        context['form_personal'] = PersonForm_Personal() if not 'form_personal' in kwargs else kwargs['form_personal']
        context['form_contact'] = PersonForm_Contact() if not 'form_contact' in kwargs else kwargs['form_contact']
        context['form_ecclesiastic'] = PersonForm_Ecclesiastic() if not 'form_ecclesiastic' in kwargs else kwargs['form_ecclesiastic']

        return context

class PersonUpdateView(DashboardUpdateView, DashboardAccountedView):
    model = UserProfile
    form_class = PersonForm

    def get_success_url(self):
        return reverse('main_person_detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        form_user = UserFormNoPassword(request.POST, instance=self.object.user)
        form_basic = PersonForm_Basic(request.POST, instance=self.object)
        form_personal = PersonForm_Personal(request.POST, instance=self.object)
        form_contact = PersonForm_Contact(request.POST, instance=self.object)
        form_ecclesiastic = PersonForm_Ecclesiastic(request.POST, instance=self.object)

        if form_basic.is_valid() and form_user.is_valid() and form_personal.is_valid() and form_contact.is_valid() and \
                form_ecclesiastic.is_valid():
            return self.form_valid(form, form_user, form_basic)
        else:
            return self.form_invalid(form_basic, form_user, form_personal, form_contact, form_ecclesiastic)

    def form_valid(self, form, form_user, form_basic):
        user = form_user.save()
        form.instance.user = user
        form.instance.church_account = self.request.user.userprofile.church_account

        self.object = form.save()

        model_name = self.model._meta.verbose_name
        if self.object:
            object_name = ' ' + self.object.__unicode__() + ' '
        else:
            object_name = ' ' + form.instance.__unicode__() + ' '

        # LogEntry.objects.log_action(self.request.user.id, )
        messages.success(self.request, message=model_name + object_name + _('updated successfully!'))

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form_basic, form_user, form_personal, form_contact, form_ecclesiastic):
        return self.render_to_response(self.get_context_data(form_basic=form_basic,
                                                             form_user=form_user,
                                                             form_personal=form_personal,
                                                             form_contact=form_contact,
                                                             form_ecclesiastic=form_ecclesiastic))

    def get_context_data(self, **kwargs):
        context = super(PersonUpdateView, self).get_context_data(**kwargs)

        context['form_basic'] = PersonForm_Basic(instance=self.object) if not 'form_basic' in kwargs else kwargs['form_basic']
        context['form_user'] = UserFormNoPassword(instance=self.object.user) if not 'form_user' in kwargs else kwargs['form_user']
        context['form_personal'] = PersonForm_Personal(instance=self.object) if not 'form_personal' in kwargs else kwargs['form_personal']
        context['form_contact'] = PersonForm_Contact(instance=self.object) if not 'form_contact' in kwargs else kwargs['form_contact']
        context['form_ecclesiastic'] = PersonForm_Ecclesiastic(instance=self.object) if not 'form_ecclesiastic' in kwargs else kwargs['form_ecclesiastic']

        return context

class PersonUpdatePasswordView(DashboardUpdateView):
    model = User
    form_class = PasswordChangeForm

class PersonListView(DashboardListView, DashboardAccountedView):
    model = UserProfile
    filters = [
        'type',
    ]
    datatable_options = {
        'search_fields': ['user__first_name', 'user__last_name'],
        'columns': [
            (_('Name'), ['user__first_name', 'user__last_name'], 'get_user_full_name_data'),
            (_('Type'), 'get_type_display')
        ],
    }

    def get_user_full_name_data(self, instance, *args, **kwargs):
        return instance.user.get_full_name()

class PersonDetailView(DashboardDetailView):
    model = UserProfile
    
    
class MinuteCreateView(DashboardCreateView, DashboardAccountedView):
    model = Minute
    form_class = MinuteForm


class MinuteUpdateView(DashboardUpdateView, DashboardAccountedView):
    model = Minute
    form_class = MinuteForm

class MinuteDetailView(DashboardDetailView, DashboardAccountedView):
    model = Minute

class MinuteListView(DashboardListView, DashboardAccountedView):
    model = Minute
    datatable_options = {
        'columns': [
            (_('Date'), 'date', 'get_date_data'),
            (_('Title'), 'title'),
            (_('Category'), 'category__name', 'get_category_data'),
        ]
    }
    filters = [
        (_('Category'), 'category', 'checkbox_choice'),
        (_('Date'), 'date', 'date_range'),
    ]

    def get_date_data(self, instance, *args, **kwargs):
        return formats.date_format(instance.date, 'SHORT_DATE_FORMAT')

    def get_category_data(self, instance, *args, **kwargs):
        return instance.category

class MonthBirthdayReportView(View):
    pass