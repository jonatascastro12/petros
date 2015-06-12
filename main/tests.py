import re
from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.test.client import Client
from main.models import UserProfile, ChurchAccount, Church


class UserProfileTestCase(TestCase):
    up1 = None
    up2 = None
    up3 = None
    up4 = None
    c = None

    def setUp(self):
        u1 = User.objects.create_user('teste1', 'teste1@email.com', '123456')

        ca = ChurchAccount.objects.create(name="Teste Conta Igreja", cnpj="123456789", user_admin=u1)

        self.c = Church.accounted.create(name="Teste Igreja", cnpj="123456789", church_account=ca)

        u2 = User.objects.create(username='teste2', password='123456')
        u3 = User.objects.create(username='teste3', password='123456')
        u4 = User.objects.create(username='teste4', password='123456')

        self.up1 = UserProfile.accounted.create(user=u1, gender='M', church=self.c, church_account=ca)
        self.up2 = UserProfile.accounted.create(user=u2, gender='M', church=self.c, church_account=ca)
        self.up3 = UserProfile.accounted.create(user=u3, gender='F', church=self.c, church_account=ca)
        self.up4 = UserProfile.accounted.create(user=u4, gender='F', church=self.c, church_account=ca)

    def test_login_access(self):
        c = Client()

        response = c.get('/dashboard/')
        self.assertEqual(response.status_code, 302)

        response = c.get('/main/person')
        self.assertEqual(response.status_code, 302)

        c.login(username='teste1', password='123456')

        response = c.get('/main/person')
        self.assertEqual(response.status_code, 200)

    def test_list_views(self):
        c = Client()
        c.login(username='teste1', password='123456')

        response = c.get('/main/person')
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        c = Client()
        c.login(username='teste1', password='123456')

        response = c.get('/main/person/'+str(self.up1.pk)+'/')
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        c = Client()
        c.login(username='teste1', password='123456')

        response = c.get('/main/person/add')
        self.assertEqual(response.status_code, 200)

        #try to create a new person
        response = c.post('/main/person/add',
            {
                'password1': '123456',
                'password2': '123456',
                'first_name': 'Teste',
                'last_name': 'Usuario',
                'username': 'teste5',
                'situation': 'A',
                'gender': 'M',
                'type': 'M',
                'how_many_child': 0,
                'church': str(self.c.id)
             }
        )

        self.assertEqual(response.status_code, 302)

        #get the person (userprofile) ID from redirect url
        userprofile_id = re.sub('^http.*(\d+)/edit$', r'\1', response.url)

        #test de url of the new object with the ID
        response = c.get('/main/person/'+str(userprofile_id)+'/')

        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        c = Client()
        c.login(username='teste1', password='123456')

        response = c.get('/main/person/'+str(self.up1.pk)+'/edit')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view(self):
        c = Client()
        c.login(username='teste1', password='123456')

        response = c.get('/dashboard/')
        self.assertEqual(response.status_code, 200)