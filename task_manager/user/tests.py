from django.test import TestCase, Client
from .models import CustomUser as User
from .forms import CustomUserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


# Create your tests here.
class UserCreateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = {
            'valid_user': {
                'username': 'Aviator',
                'first_name': 'Frank',
                'last_name': 'Abignale',
                'password1': 'useropsw123',
                'password2': 'useropsw123'
            },

            'wrong_user': {
                'username': '',
                'first_name': '',
                'last_name': '',
                'password1': '23',
                'password2': '234'
            }
        }

    def test_create_user_view(self):
        url = reverse('user_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_form_valid(self):
        user = self.data['valid_user']
        form = CustomUserCreationForm(user)
        self.assertTrue(form.is_valid())

    def test_create_user_form_invalid(self):
        user = self.data['wrong_user']
        form = CustomUserCreationForm(user)
        self.assertFalse(form.is_valid())

    def test_create_user_on_post(self):
        url = reverse('user_create')
        user = self.data['valid_user']
        self.client.post(url, user)
        new_user = User.objects.last()
        self.assertEqual(user['username'], new_user.username)
        self.assertEqual(user['first_name'], new_user.first_name)
        self.assertEqual(user['last_name'], new_user.last_name)


class UserRUDTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.data = {
            'user': {
                'username': 'Aviator',
                'first_name': 'Frank',
                'last_name': 'Abignale',
                'password': 'useropsw123',
            },

            'user_updated': {
                'username': 'Franky',
                'first_name': 'Frank',
                'last_name': 'Abernaty',
                'password1': 'useropsw123',
                'password2': 'useropsw123',
            }
        }

    def test_read_user(self):
        url = reverse('users_index')
        user = self.data['user']
        User.objects.create(**user)

        response = self.client.get(url)
        response_text = response.content.decode('utf-8')

        self.assertIn(user['username'], response_text)
        self.assertIn(user['first_name'], response_text)
        self.assertIn(user['last_name'], response_text)

    def test_update_user(self):
        user = self.data['user']
        user_updated = self.data['user_updated']

        new_user = User.objects.create_user(**user)

        login_url = reverse('login')
        self.client.post(
            login_url, {
                'username': user['username'],
                'password': user['password']
            }
        )

        url = reverse('user_update', kwargs={'pk': new_user.pk})
        self.client.post(url, user_updated)

        updated_user = User.objects.get(pk=new_user.pk)
        self.assertEqual(user_updated['username'], updated_user.username)
        self.assertEqual(user_updated['first_name'], updated_user.first_name)
        self.assertEqual(user_updated['last_name'], updated_user.last_name)

    def test_delete_user(self):
        user_data = self.data['user']
        user = User.objects.create_user(**user_data)

        login_url = reverse('login')
        self.client.post(
            login_url, {
                'username': user_data['username'],
                'password': user_data['password']
            }
        )
        url = reverse('user_delete', kwargs={'pk': user.pk})
        self.client.post(url)
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(pk=user.pk)
