from django.test import TestCase, Client
from django.shortcuts import reverse
from django.core.exceptions import ObjectDoesNotExist
from task_manager.user.models import CustomUser

from .models import Status


class StatusCRUDTest(TestCase):
    user_data = {
        'username': 'jhondoe',
        'first_name': 'Jhon',
        'last_name': 'Doe',
        'password': '123456a',
    }

    def setUp(self):
        self.client = Client()
        self.data = {
            'create': {'name': 'Test status'},
            'update': {'name': 'Updated test status'},
        }

        CustomUser.objects.create_user(**self.user_data)
        login_url = reverse('login')
        self.client.post(
            login_url,
            {
                'username': self.user_data['username'],
                'password': self.user_data['password']
            }
        )

    def test_status_create(self):
        url = reverse('status_create')
        status_data = self.data['create']

        self.client.post(url, status_data)
        status = Status.objects.last()
        self.assertEqual(status.name, status_data['name'])

    def test_status_read(self):
        url = reverse('status_index')
        status_data = self.data['create']
        status = Status.objects.create(**status_data)

        response = self.client.get(url)
        self.assertIn(status.name, response.content.decode('utf-8'))

    def test_status_update(self):
        status_data = self.data['create']
        status = Status.objects.create(**status_data)
        url = reverse('status_update', kwargs={'pk': status.pk})

        status_updated_data = self.data['update']
        self.client.post(url, status_updated_data)

        status_updated = Status.objects.get(pk=status.pk)
        self.assertEqual(status_updated_data['name'], status_updated.name)

    def test_status_delete(self):
        status_data = self.data['create']
        status = Status.objects.create(**status_data)
        url = reverse('status_delete', kwargs={'pk': status.pk})

        self.client.post(url)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=status.pk)
