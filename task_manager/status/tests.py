from django.test import TestCase, Client
from task_manager.task.models import Task
from django.core.exceptions import ObjectDoesNotExist
from .models import Status
from django.urls import reverse


class TestStatus(TestCase, Client):
    @classmethod
    def setUp(cls):
        cls.status1 = Status.objects.create(name="На тестировании")
        cls.status2 = Status.objects.create(name="В работе")
        cls.task = Task.objects.create(name="Task 1")
        cls.task.statuses.add(cls.status1)
        cls.client = Client()

    def test_status_show(self):
        statuses = Status.objects.all()
        message = "Status not found"
        self.assertIn(self.status1, statuses, message)
        self.assertIn(self.status2, statuses, message)

    def test_status_update(self):
        status = Status.objects.get(name="На тестировании")
        status.name = "В разработке"
        status.save()
        self.assertEqual(status.name, "В разработке")

    def test_status_deletion_blocked(self):
        # Проверяем, что статус связан с какой-либо задачей
        self.assertTrue(self.status1.tasks.exists())
        response = self.client.post(reverse('status_delete',
                                            kwargs={'pk': self.status1.pk}))
        self.assertEqual(response.status_code, 302)
        statuses = Status.objects.all()
        status = Status.objects.get(pk=self.status1.pk)
        self.assertIn(status, statuses)

    def test_status_delete(self):
        self.assertFalse(self.status2.tasks.exists())
        url = reverse('status_delete', kwargs={'pk': self.status2.pk})

        self.client.post(url)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(pk=self.status2.pk)
