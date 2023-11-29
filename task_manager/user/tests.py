from django.test import TestCase, Client
from .models import CustomUser as User
from django.urls import reverse


# Create your tests here.
class TestUser(TestCase, Client):

    def setUp(self):
        self.user = User.objects.create(first_name='Frank',
                                        last_name='Abignel',
                                        username='Aviator')
        self.user.set_password('123456')
        self.user.save()
        self.client = Client()

    def test_login(self):
        self.client.login(username='Aviator', password='123456')
        # Проверка успешного входа
        self.assertEqual(self.client.session['_auth_user_id'], str(self.user.id))

    def test_logout(self):

        self.client.login(username='Aviator', password='123456')
        self.assertEqual(self.client.session['_auth_user_id'], str(self.user.id))
        self.client.logout()
        # Проверка успешного выхода (отсутствия данных аутентификации)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_signup_redirect(self):
        data = {
            'first_name': 'name',
            'last_name': 'name2',
            'username': 'new_user',
            'password1': 'new_password123',
            'password2': 'new_password123',
        }
        response = self.client.post(reverse('user_create'), data)
        # Проверяем, что после успешной регистрации произошел редирект на нужную страницу
        self.assertRedirects(response, reverse('login'),
                             status_code=302,
                             target_status_code=200)

    def test_update_user(self):
        self.client.force_login(self.user)
        self.user.username = 'Leo'
        self.user.first_name = 'Franklin'
        self.user.last_name = 'Abernaty'
        self.user.save()
        self.assertEqual(self.user.username, 'Leo')
        self.assertEqual(self.user.first_name, 'Franklin')
        self.assertEqual(self.user.last_name, 'Abernaty')

    def test_update_user_redirect(self):
        data = {
            'first_name': 'New Name',
            'last_name': 'New Last Name',
            'username': 'newusername',
            'old_password': 'oldpass123',
            'new_password1': 'newpass123',
            'new_password2': 'newpass123',
        }
        self.client.force_login(self.user)
        response = self.client.post(reverse('user_update',
                                            kwargs={'pk': self.user.id}),
                                    data)

        self.assertRedirects(response, reverse('users_index'))
        self.assertContains(response, 'User is successfully updated')

    def test_delete_user(self):
        pass
