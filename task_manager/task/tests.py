from django.test import TestCase, Client
from django.shortcuts import reverse
from django.core.exceptions import ObjectDoesNotExist
from task_manager.user.models import CustomUser
from task_manager.status.models import Status

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
        user = CustomUser.objects.create(**self.user_data)
        status = Status.objects.create(**self.status_data)
        self.data = {
            'create': {'name': 'Example task',
                       'description': 'This is example task',
                       'author': user,
                       'status': status},
            'update': {'name': 'Updated task',
                       'description': 'This is updated task',
                       'author': user,
                       'status': status},
        }

        login_url = reverse('login')
        self.client.post(
            login_url,
            {
                'username': self.user_data['username'],
                'password': self.user_data['password']
            }
        )

    def test_task_create(self):
        url = reverse('task_create')
        task_data = self.data['create']

        self.client.post(url, task_data)
        task = Task.objects.last()
        self.assertEqual(task.name, task_data['name'])
        self.assertEqual(task.description, task_data['description'])
        self.assertEqual(task.status, self.status.pk)


    # def test_task_read(self):
    #     url = reverse('task_index')
    #     task_data = self.data['create']
    #     task = Task.objects.create(**task_data)

    #     response = self.client.get(url)
    #     self.assertIn(task.name, response.content.decode('utf-8'))

    # def test_task__update(self):
    #     task_data = self.data['create']
    #     task = Task.objects.create(**task_data)
    #     url = reverse('task_update', kwargs={'pk': task.pk})

    #     task_updated_data = self.data['update']
    #     self.client.post(url, task_updated_data)

    #     task_updated = Task.objects.get(pk=task.pk)
    #     self.assertEqual(task_updated_data['name'], task_updated.name)

    # def test_task_task_delete(self):
    #     task_data = self.data['create']
    #     task = Task.objects.create(**task_data)
    #     url = reverse('task_delete', kwargs={'pk': task.pk})

    #     self.client.post(url)
    #     with self.assertRaises(ObjectDoesNotExist):
    #         Task.objects.get(pk=task.pk)
