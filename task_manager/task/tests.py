from django.test import TestCase, Client
from django.shortcuts import reverse
from django.core.exceptions import ObjectDoesNotExist
from task_manager.user.models import CustomUser
from task_manager.status.models import Status
from django.contrib.auth import authenticate

from .models import Task


class TaskCRUDTest(TestCase):
    user_data = {
        'username': 'Jhondoe',
        'first_name': 'Jhon',
        'last_name': 'Doe',
        'password': '123456a',
    }

    status_data = {'name': 'Example status'}

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(**self.user_data)
        self.status = Status.objects.create(**self.status_data)

        self.data = {
            'create': {'name': 'Example task',
                       'description': 'This is example task',
                       'author': self.user.pk,
                       'status': self.status.pk},
            'update': {'name': 'Updated task',
                       'description': 'This is updated task',
                       'author': self.user.pk,
                       'status': self.status.pk},
        }

        self.client.force_login(self.user)

        # login_url = reverse('login')

        # self.client.post(
        #     login_url,
        #     {
        #         'username': self.user.username,
        #         'password': self.user.password
        #     }
        # )

    def test_task_create(self):
        url = reverse('task_create')
        task_data = self.data['create']

        self.client.post(url, task_data)

        task = Task.objects.last()
        self.assertEqual(task_data['name'], task.name)
        self.assertEqual(task.description, task_data['description'])
        self.assertEqual(task.status.pk, self.status.pk)

    def test_task_read(self):
        create_url = reverse('task_create')
        task_data = self.data['create']
        self.client.post(create_url, task_data)

        task = Task.objects.last()
        url = reverse('task_show', kwargs={'pk': task.pk})
        response = self.client.get(url)
        self.assertContains(response, task.name)

    def test_task__update(self):
        create_url = reverse('task_create')
        task_data = self.data['create']
        self.client.post(create_url, task_data)
        task = Task.objects.last()

        url = reverse('task_update', kwargs={'pk': task.pk})

        task_updated_data = self.data['update']
        self.client.post(url, task_updated_data)

        task_updated = Task.objects.get(pk=task.pk)
        self.assertEqual(task_updated_data['name'], task_updated.name)

    def test_task_task_delete(self):
        create_url = reverse('task_create')
        task_data = self.data['create']
        self.client.post(create_url, task_data)

        task = Task.objects.last()
        update_url = reverse('task_delete', kwargs={'pk': task.pk})

        self.client.post(update_url)
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(pk=task.pk)
