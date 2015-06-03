from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect
from django.utils.translation import gettext as _
from dashboard_view.views import DashboardView, DashboardMenu, DashboardCreateView, DashboardUpdateView, \
    DashboardListView, DashboardDetailView, DashboardOverviewView, DashboardProfileView
from main.forms import PersonForm_User, PersonForm_Personal, PersonForm_Contact, PersonForm, UserForm
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

class PetrosDashboardOverviewView(DashboardOverviewView):
    template_name = "dashboard_base.html"

class PetrosDashboardProfileView(DashboardProfileView):
    template_name = "dashboard_base.html"


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

    def get_success_url(self):
        return reverse('main_person_edit', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = None

        form = self.get_form()
        form_user = UserForm(request.POST)
        form_basic = PersonForm_User(request.POST)
        form_personal = PersonForm_Personal(request.POST)
        form_contact = PersonForm_Contact(request.POST)

        if form_basic.is_valid() and form_user.is_valid() and form_personal.is_valid() and form_contact.is_valid():
            return self.form_valid(form, form_user, form_basic)
        else:
            return self.form_invalid(form_basic, form_user, form_personal, form_contact)

    def form_valid(self, form, form_user, form_basic):
        form_user.instance.first_name = form_basic.cleaned_data.get('first_name', '')
        form_user.instance.last_name = form_basic.cleaned_data.get('last_name', '')
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
    
    def form_invalid(self, form_basic, form_user, form_personal, form_contact):
        return self.render_to_response(self.get_context_data(form_basic=form_basic,
                                                             form_user=form_user,
                                                             form_personal=form_personal,
                                                             form_contact=form_contact))

    def get_context_data(self, **kwargs):
        context = super(PersonCreateView, self).get_context_data(**kwargs)

        context['form_basic'] = PersonForm_User() if not 'form_user' in kwargs else kwargs['form_basic']
        context['form_user'] = UserForm() if not 'form_user' in kwargs else kwargs['form_user']
        context['form_personal'] = PersonForm_Personal() if not 'form_personal' in kwargs else kwargs['form_personal']
        context['form_contact'] = PersonForm_Contact() if not 'form_contact' in kwargs else kwargs['form_contact']

        return context

class PersonUpdateView(DashboardUpdateView):
    model = UserProfile
    form_class = PersonForm

    def get_success_url(self):
        return reverse('main_person_edit', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = None

        form = self.get_form()
        form_user = UserForm(request.POST)
        form_basic = PersonForm_User(request.POST)
        form_personal = PersonForm_Personal(request.POST)
        form_contact = PersonForm_Contact(request.POST)

        if form_basic.is_valid() and form_user.is_valid() and form_personal.is_valid() and form_contact.is_valid():
            return self.form_valid(form, form_user, form_basic)
        else:
            return self.form_invalid(form_basic, form_user, form_personal, form_contact)

    def form_valid(self, form, form_user, form_basic):
        form_user.instance.first_name = form_basic.cleaned_data.get('first_name', '')
        form_user.instance.last_name = form_basic.cleaned_data.get('last_name', '')
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

    def form_invalid(self, form_basic, form_user, form_personal, form_contact):
        return self.render_to_response(self.get_context_data(form_basic=form_basic,
                                                             form_user=form_user,
                                                             form_personal=form_personal,
                                                             form_contact=form_contact))

    def get_context_data(self, **kwargs):
        context = super(PersonUpdateView, self).get_context_data(**kwargs)

        context['form_basic'] = PersonForm_User(instance=self.object) if not 'form_user' in kwargs else kwargs['form_basic']
        context['form_user'] = UserForm(instance=self.object.user) if not 'form_user' in kwargs else kwargs['form_user']
        context['form_personal'] = PersonForm_Personal(instance=self.object) if not 'form_personal' in kwargs else kwargs['form_personal']
        context['form_contact'] = PersonForm_Contact(instance=self.object) if not 'form_contact' in kwargs else kwargs['form_contact']

        return context

class PersonListView(DashboardAccountedListView):
    model = UserProfile
    fields = [
        ('Nome', 'user__get_full_name'),
        ('Tipo', 'get_type_display')
    ]

class PersonDetailView(DashboardDetailView):
    model = UserProfile