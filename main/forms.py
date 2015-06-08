from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms.fields import DateField, CharField
from django.forms.models import ModelForm
from django.utils.translation import gettext as _
from input_mask.contrib.localflavor.br.widgets import BRCPFInput, BRZipCodeInput, BRPhoneNumberInput
from localflavor.br.forms import BRCPFField, BRZipCodeField, BRPhoneNumberField
from main.models import UserProfile


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
    cpf = BRCPFField(required=True, label='CPF', widget=BRCPFInput)
    birth_date = DateField(widget=DateTimePicker(options={"format": "DD/MM/YYYY",
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