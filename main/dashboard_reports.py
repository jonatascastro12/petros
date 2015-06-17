from django.utils.translation import gettext as _
from dashboard_view import dashboard_site
from dashboard_view.dashboard_reports import DashboardReport
from main.forms import MonthBirthdayReportForm
from main.models import UserProfile

class MonthBirthdayReport(DashboardReport):
    model = UserProfile
    filter_form = MonthBirthdayReportForm
    list_display = ['user__get_full_name', 'birth_date__month', ]
    actions = ['print', ]

    def get_queryset(self):
        objects = self.report.model.accounted.\
            filter(birth_date__month=self.filter_form.cleaned_data.get('month')).\
            all()
        objects = list(objects)
        objects = sorted(objects, key=lambda u:int(u.birth_date.day))

        return objects

    class Meta:
        verbose_name = _('Month Birthday')
        permission = ('can_view_userprofile')
