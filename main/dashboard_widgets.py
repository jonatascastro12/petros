import json
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from django.template.context import Context
from django.template.loader import get_template
from dashboard_view.dashboard_widgets import DashboardWidget
from main.models import UserProfile
import datetime

class PetrosDashboardWidget(DashboardWidget):
    def _render_widget_person_month_birthday(self):
        template_html = get_template('dashboard_widgets/person_month_birthday.html')
        c = Context({
            'birthday_report_view': '',
            'ajax_view': 'widget_ajax_call',
            'widget_name': 'person_month_birthday'
        })
        template_js = get_template('dashboard_widgets/person_month_birthday_js.html')

        return (template_html.render(c), template_js.render(c), )

    def _action_person_month_birthday(self, request):
        today = datetime.date.today()
        users = UserProfile.accounted.filter(birth_date__month=today.month).all()[:10]
        users_list = []
        for u in users:
            users_list.append({'name': u.user.get_full_name(), 'day': str(u.birth_date.day),
                               'thumb': u.get_small_thumbnail(), 'url': u.get_absolute_url()})
        users_list = sorted(users_list, key=lambda u:int(u['day']))
        data = json.dumps({'users_list': users_list, 'month': today.strftime('%B')})
        return HttpResponse(data)
