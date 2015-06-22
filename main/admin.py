from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import gettext as _
from dashboard_view.admin import DashboardAdminSite
from dashboard_view.dashboard_menu import DashboardMenu
from main.dashboard_reports import MonthBirthdayReport
from main.dashboard_widgets import MonthBirthdayWidget
from main.models import UserProfile, ChurchAccount, Church, ChurchType, Minute, MinuteCategory

menu_dict = [
    {'name': 'overview', 'icon_class': 'fa-dashboard', 'verbose_name': _('Overview'),
     'link': reverse_lazy('dashboard:index')},
    {'name': 'system', 'icon_class': 'fa-gear', 'verbose_name': _('Settings'), 'children':
        [
            {'name': 'settings', 'verbose_name': _('General Settings'), 'link': '#', 'icon_class': 'fa-wrench'},
            {'name': 'account', 'verbose_name': _('Account'), 'link': '#', 'icon_class': 'fa-gears'},
            {'name': 'team', 'verbose_name': _('Team'), 'link': '#', 'icon_class': 'fa-key'}
        ]
     },
    {'name': 'main', 'icon_class': 'fa-users', 'verbose_name': _('People'), 'children':
        [
            {'name': 'person', 'verbose_name': _('Person'), 'link': reverse_lazy('main_person'),
             'icon_class': 'fa-user', },
            {'name': 'minutes', 'verbose_name': _('Minutes'), 'link': reverse_lazy('main_minute'),
             'icon_class': 'fa-file-text-o', },
            {'name': 'cells', 'verbose_name': _('Cells'), 'link': reverse_lazy('main_cell'),
             'icon_class': 'fa-users', },
    ]},

]

menu = DashboardMenu(menu=menu_dict)

class PetrosDashboardAdmin(DashboardAdminSite):
    site_header = _('Petros Dashboard')
    site_title = _('Petros Dashboard')
    menu = menu


dashboard = PetrosDashboardAdmin('dashboard')


dashboard.register_report(MonthBirthdayReport)
dashboard.register_widget(MonthBirthdayWidget)


class ChurchAccountAdmin(admin.ModelAdmin):
    model = ChurchAccount


class ChurchTypeAdmin(admin.ModelAdmin):
    model = ChurchType


class ChurchAdmin(admin.ModelAdmin):
    model = Church


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(is_superuser=False)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super(UserAdmin, self).get_fieldsets(request, obj)
        else:
            return (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

class MinuteCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = MinuteCategory

class MinuteAdmin(admin.ModelAdmin):
    class Meta:
        model = Minute

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(ChurchAccount, ChurchAccountAdmin)
admin.site.register(Church, ChurchAdmin)
admin.site.register(ChurchType, ChurchTypeAdmin)

admin.site.register(MinuteCategory, MinuteCategoryAdmin)
admin.site.register(Minute, MinuteAdmin)