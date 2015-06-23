from bootstrap3_datetime.widgets import DateTimePicker
import datetime
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.forms.fields import DateField, CharField, ChoiceField
from django.forms.forms import Form
from django.forms.models import ModelForm
from django.utils.dates import MONTHS
from django.utils.translation import gettext as _
from django_select2.fields import AutoSelect2MultipleField, AutoModelSelect2MultipleField
from input_mask.contrib.localflavor.br.widgets import BRCPFInput, BRZipCodeInput, BRPhoneNumberInput
from localflavor.br.forms import BRCPFField, BRZipCodeField, BRPhoneNumberField
from main.models import UserProfile, Minute, Group, UserPreferences


class PersonForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'church_account']

class PersonForm_Basic(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo',]

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UserFormNoPassword(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class PersonForm_Personal(ModelForm):
    cpf = BRCPFField(required=False, label='CPF', widget=BRCPFInput)
    birth_date = DateField(required=False, widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False, "startDate": "new a({y: 1970})"}), label=_('Birth date'))

    class Meta:
        model = UserProfile
        fields = ['birth_date', 'rg', 'cpf', 'gender', 'marital_status', 'father_name', 'mother_name',
                  'spouse', 'blood_type', 'has_child', 'how_many_child']

class PersonForm_Contact(ModelForm):
    zipcode = BRZipCodeField(required=False, label=_('Zipcode'), widget=BRZipCodeInput)
    phone1 = BRPhoneNumberField(required=False, label=_('Phone 1'), widget=BRPhoneNumberInput)
    phone2 = BRPhoneNumberField(required=False, label=_('Phone 2'), widget=BRPhoneNumberInput)

    class Meta:
        model = UserProfile
        fields = ['address_line', 'neighborhood', 'city', 'state', 'zipcode', 'phone1', 'phone2', ]


#TODO: make church as "auto select2 field"
#TODO: make discipler as "auto select2 field"

class PersonForm_Ecclesiastic(ModelForm):
    baptism_date = DateField(required=False, widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False, "startDate": "new a({y: 1970})"}), label=_('Bapstism date'))
    admission_date = DateField(required=False, widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False, "startDate": "new a({y: 1970})"}), label=_('Admission date'))

    class Meta:
        model = UserProfile
        fields = ['type', 'situation', 'previous_church', 'previous_function', 'baptism_date', 'baptism_place',
                  'admission_date', 'member_function', 'church', 'discipler', ]


class MinuteForm(ModelForm):
    date = DateField(widget=DateTimePicker(options={"format": "DD/MM/YYYY",
                                       "pickTime": False, "startDate": "new a({y: 1970})"}), label=_('Date'))

    class Meta:
        model = Minute
        fields = ['title', 'date', 'category', 'content', ]



class PersonMultiSelectField(AutoModelSelect2MultipleField):
    queryset = UserProfile.accounted
    search_fields = ['user__first_name__icontains', 'user__last_name__icontains', 'user__username__icontains']

    def prepare_qs_params(self, request, search_term, search_fields):
        q = None
        for field in search_fields:
            kwargs = {}
            search_term = search_term.strip()
            if " " in search_term:
                splitted_terms = search_term.split(" ")
                for term in splitted_terms:
                    kwargs[field] = term
                    if q is None:
                        q = Q(**kwargs)
                    else:
                        q = q | Q(**kwargs)
            else:
                kwargs[field] = search_term
                if q is None:
                    q = Q(**kwargs)
                else:
                    q = q | Q(**kwargs)
        return {'or': [q], 'and': {}}


class GroupForm(ModelForm):
    userprofiles = PersonMultiSelectField(label=_('Members'))

    class Meta:
        model = Group
        fields = ['name', 'photo', 'place', 'weekday', 'time', 'userprofiles']


def get_actual_month():
    today = datetime.datetime.today()
    return today.month

class MonthBirthdayReportForm(Form):
    month_choices = (
        (1, _('January')),
        (2, _('February')),
        (3, _('March')),
        (4, _('April')),
        (5, _('May')),
        (6, _('June')),
        (7, _('July')),
        (8, _('August')),
        (9, _('Septembe(r')),
        (10, _('October')),
        (11, _('November')),
        (12, _('December'))
    )

    month = ChoiceField(choices=month_choices, initial=get_actual_month(), label=_('Month'), )


class UserPreferencesForm(ModelForm):
    class Meta:
        model = UserPreferences
        exclude = []