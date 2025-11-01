from django.test import TestCase
from django.urls import reverse, resolve
from .views import signup
from .forms import SignUpForm
from django.contrib.auth.models import User

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)

    def test_csrf(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_signup_form(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        }
        response = self.client.post(url, data)
        self.assertTrue(User.objects.filter(username='john').exists())


from django.test import TestCase
from django.template import Template, Context
from django.contrib.auth.models import User

class TemplateTagsTests(TestCase):
    def test_get_user_count_tag(self):
        User.objects.create_user(username='a', password='x')
        tpl = Template("{% load accounts_extras %}{% get_user_count %}")
        rendered = tpl.render(Context())
        self.assertIn('1', rendered.strip())

