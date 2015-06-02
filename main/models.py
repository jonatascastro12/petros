# coding=utf-8
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from localflavor.br.br_states import STATE_CHOICES
from localflavor.br.models import BRStateField
from crop_image.forms import CropImageModelField


class ChurchAccount(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ', blank=True)
    email = models.EmailField(blank=True, null=True, max_length='200')
    address_line = models.CharField(blank=True, null=True, max_length='300', verbose_name = 'Endereço', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9,\.\s]+$', _(u'Special char not permitted.'))])
    neighborhood = models.CharField(blank=True, null=True,  max_length='200', verbose_name = 'Bairro', validators=[RegexValidator(u'^[\'a-zA-Z0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$', _(u'Special char not permitted.'))])
    city = models.CharField(blank=True, null=True,  max_length='200', verbose_name = 'Cidade', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9\s]+$', _(u'Special char not permitted.'))])
    state = models.CharField(blank=True, null=True,  max_length='2', verbose_name = 'UF',choices=STATE_CHOICES)
    phone1 = models.CharField(blank=True, max_length=15, verbose_name=_('Phone')+' 1')
    phone2 = models.CharField(blank=True, max_length=15, verbose_name=_('Phone')+' 2')
    logo = CropImageModelField(upload_to="church_logos", null=True, blank=True)

    user_admin = models.ForeignKey(User, related_name="church_user_admin")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("Church Account")


class AccountedManager(models.Manager):
    pass

class AccountedModel(models.Model):
    church_account = models.ForeignKey(ChurchAccount)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    accounted = AccountedManager()

    class Meta:
        abstract = True

class ChurchType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Church Type')

# Create your models here.
class Church(AccountedModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ', blank=True)
    email = models.EmailField(blank=True, null=True, max_length='200')
    address_line = models.CharField(blank=True, null=True, max_length='300', verbose_name = 'Endereço', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9,\.\s]+$', _(u'Special char not permitted.'))])
    neighborhood = models.CharField(blank=True, null=True,  max_length='200', verbose_name = 'Bairro', validators=[RegexValidator(u'^[\'a-zA-Z0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$', _(u'Special char not permitted.'))])
    city = models.CharField(blank=True, null=True,  max_length='200', verbose_name = 'Cidade', validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9\s]+$', _(u'Special char not permitted.'))])
    state = models.CharField(blank=True, null=True,  max_length='2', verbose_name = 'UF',choices=STATE_CHOICES)
    phone1 = models.CharField(blank=True, max_length=15, verbose_name=_('Phone')+' 1')
    phone2 = models.CharField(blank=True, max_length=15, verbose_name=_('Phone')+' 2')
    type = models.ForeignKey(ChurchType)
    is_mother = models.BooleanField(default=True)
    church_mother = models.ForeignKey('self', null=True, blank=True, related_name="mother")
    logo = CropImageModelField(upload_to="church_logos", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('church_detail', (), {'pk': self.id})

    class Meta:
        verbose_name = _('Church')

class UserProfile(AccountedModel):
    user = models.OneToOneField(User)

    photo = CropImageModelField(upload_to='user_photos', blank=True, null=True)

    type = models.CharField(max_length=100, choices=(
        #translation: Gathered: Congregado
        ('G', _('Gathered')),
        ('M', _('Member')),
    ))

    cpf = models.CharField(max_length=14, verbose_name='CPF')
    rg = models.CharField(max_length=14, blank=True, null=True, verbose_name='RG')

    birth_date = models.DateField(verbose_name=_('Birth Date'))
    gender = models.CharField(max_length='1', verbose_name=_('Gender'), choices=[('M', _('Male')), ('F', _('Female'))])
    blood_type = models.CharField(max_length='2', blank=True, null=True, verbose_name=_('Blood Type'), choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-','B-'), ('O+', 'O+'), ('O-', 'O-')])

    address_line = models.CharField(blank=True, max_length='300', verbose_name=_('Address'), validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9,\.\s]+$', _(u'Special char not permitted.'))])
    neighborhood = models.CharField(blank=True, max_length='200', verbose_name=_('Neighborhood'), validators=[RegexValidator(u'^[\'a-zA-Z0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]+$', _(u'Special char not permitted.'))])
    city = models.CharField(blank=True, max_length='200', verbose_name=_('City'), validators=[RegexValidator(u'^[\'a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9\s]+$', _(u'Special char not permitted.'))])
    state = BRStateField(blank=True, null=True)
    zipcode = models.CharField(blank=True, null=True, max_length='10', )
    phone1 = models.CharField(blank=True, max_length='15', verbose_name='Telefone 1',)
    phone2 = models.CharField(blank=True, max_length='15', verbose_name='Telefone 2',)

    profession = models.CharField(blank=True, null=True, max_length='200', verbose_name=_('Profession'))
    work_place = models.CharField(blank=True, null=True, max_length='200', verbose_name=_('Work place'))

    father_name = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Father name'))
    mother_name = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Mother name'))
    marital_status = models.CharField(max_length='1', blank=True, null=True, choices=[('S', _('Single')), ('D', _('Divorced')), ('M', _('Married')), ('W', _('Widow')), ])
    spouse = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Spouse'))
    has_child = models.CharField(blank=True, null=True, max_length='1', verbose_name=_('Has Child?'), choices=[('Y', _('Yes')), ('N', _('No'))])
    how_many_child = models.PositiveSmallIntegerField(default=0)

    discipler = models.ForeignKey('self', related_name=_("discipler_user"), null=True, blank=True, verbose_name=_("Discipler"))

    #TODO: Spouse - Foreign Key
    #TODO: Children - ManyToManyField or Foreing Key in a ChildrenObject

    def __unicode__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse('main_person_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")

class MemberFunction(AccountedModel):

    def __str__(self):
        return self.name.encode('utf8')

    title = models.CharField(max_length=60, verbose_name='Título abrev.', help_text='Ex: Dc')
    name = models.CharField(max_length=255, verbose_name='Título', help_text='Ex: Diácono')
    title_female = models.CharField(max_length=60, verbose_name='Título abrev. Feminino', help_text = 'Ex: Dcª')
    name_female = models.CharField(max_length=255, verbose_name='Título Feminino', help_text = 'Ex: Diaconisa')

    class Meta:
        verbose_name = 'Função de membro'
        verbose_name_plural = 'Funções de membro'

class Member(AccountedModel):

    SITUATION_CHOICES = [('A', _('Active')), ('I', _('Inactive'))]

    def __str__(self):
        return self.person.name.encode('utf8')

    previous_church = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Previous church'))
    previous_function = models.CharField(max_length='255', blank=True, null=True, verbose_name=_('Previous function'))
    baptism_date = models.DateField(verbose_name=_('Baptism date'))
    baptism_place = models.CharField(max_length='255',blank=True, null=True, verbose_name=_('Baptism place'))
    admission_date = models.DateField(blank=True, null=True, verbose_name=_('Admission date'))
    member_function = models.ForeignKey(MemberFunction, verbose_name=_("Member Function"))
    situation = models.CharField(max_length=7, verbose_name=_("Situation"), choices=SITUATION_CHOICES)
    church = models.ForeignKey(Church)
    user = models.OneToOneField(User, verbose_name=_("User"), related_name="member")

    def get_member_function(self):
        if self.person.gender == 'F':
            return self.member_function.name_female
        else:
            return self.member_function.name

    def get_member_function_display(self):
        return self.get_member_function()

    def get_absolute_url(self):
        return reverse('member_detail', (), {'pk': self.id})

    class Meta:
        verbose_name = _('Member')


class GroupManager(models.Manager):
    def create_cell(self, args, **kwargs):
        pass

class Group(AccountedModel):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=(
        ('C', _('Cell')),
        ('D', _('Department')),
        ('M', _('Ministry')),
    ))
    users = models.ManyToManyField(User, blank=True)

    manager = GroupManager()