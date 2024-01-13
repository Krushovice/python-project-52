from django.test import TestCase, Client
from django.shortcuts import reverse
from django.core.exceptions import ObjectDoesNotExist
from task_manager.user.models import CustomUser

from .models import Label


class LabelCRUDTest(TestCase):
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

    def test_label_create(self):
        url = reverse('label_create')
        label_data = self.data['create']

        self.client.post(url, label_data)
        label = Label.objects.get(name=label_data['name'])
        self.assertEqual(label.name, label_data['name'])

    def test_label_read(self):
        url = reverse('labels_index')
        label_data = self.data['create']
        label = Label.objects.create(**label_data)

        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 500)
        self.assertIn(label.name, response.content.decode('utf-8'))

    def test_status_update(self):
        label_data = self.data['create']
        label = Label.objects.create(**label_data)
        url = reverse('label_update', kwargs={'pk': label.pk})

        label_updated_data = self.data['update']
        self.client.post(url, label_updated_data)

        label_updated = Label.objects.get(pk=label.pk)
        self.assertEqual(label_updated_data['name'], label_updated.name)

    def test_status_delete(self):
        """Test status delete on POST."""
        label_data = self.data['create']
        label = Label.objects.create(**label_data)
        url = reverse('label_delete', kwargs={'pk': label.pk})

        self.client.post(url)
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(pk=label.pk)
