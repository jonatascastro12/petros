from django.utils.translation import gettext as _
from dashboard_view.dashboard_reports import DashboardReport
from main.forms import MonthBirthdayReportForm
from main.models import UserProfile

class MonthBirthdayReport(DashboardReport):
    permission = ('can_view_userprofile')
    model = UserProfile
    filter_form = MonthBirthdayReportForm
    list_display = [
        (_('Name'), 'user__get_full_name'),
        (_('Day'), 'birth_date__day'),
        (_('Email'), 'user__email'),
        (_('Phones'), 'phone1'),
    ]
    actions = ['print', 'send_message', ]
    icon = 'fa-birthday-cake'

    def get_queryset(self, form):
        objects = self.model.accounted.\
            filter(birth_date__month=form.cleaned_data.get('month')).\
            all()
        objects = list(objects)
        objects = sorted(objects, key=lambda u:int(u.birth_date.day))

        return objects

