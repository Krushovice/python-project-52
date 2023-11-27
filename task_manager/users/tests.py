from django.test import TestCase, Client
from .models import CustomUser as User


# Create your tests here.
class TestUser(TestCase, Client):
    def __init__(self, *args, **kwargs):
        self.client = Client()

    def setUp(self):
        User.objects.create(first_name='Frank', last_name='Abignel', username='Aviator', password=123456)

    def test_login(self):
        pass
