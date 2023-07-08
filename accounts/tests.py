from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from contacts.models import Contact

class AccountsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.dashboard_url = reverse('dashboard')

    def test_register_valid_form(self):
        response = self.client.post(self.register_url, {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': 'test123',
            'password2': 'test123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login page

        # Check if the user is created
        user = User.objects.get(username='johndoe')
        self.assertIsNotNone(user)

    def test_register_invalid_form(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'password': 'newpassword',
            'password2': 'differentpassword',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertEqual(User.objects.filter(username='newuser').count(), 0)

    def test_login_valid_credentials(self):
        # Create a test user
        user = User.objects.create_user(
            username='johndoe',
            password='test123',
        )

        response = self.client.post(self.login_url, {
            'username': 'johndoe',
            'password': 'test123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to dashboard page

        # Check if the user is authenticated
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'johndoe',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_logout(self):
        # Login a test user
        user = User.objects.create_user(
            username='johndoe',
            password='test123',
        )
        self.client.login(username='johndoe', password='test123')

        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect to index page

        # Check if the user is logged out
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_dashboard_authenticated_user(self):
        # Create a test user and associated contact
        user = User.objects.create_user(
            username='johndoe',
            password='test123',
        )
        contact = Contact.objects.create(
            user=user,
            name='John Doe',
            email='johndoe@example.com',
            message='Test message',
        )
        self.client.login(username='johndoe', password='test123')

        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')
        self.assertEqual(response.context['contacts'].count(), 1)

    def test_dashboard_unauthenticated_user(self):
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 302)  # Redirect to login page
        self.assertRedirects(response, self.login_url)
