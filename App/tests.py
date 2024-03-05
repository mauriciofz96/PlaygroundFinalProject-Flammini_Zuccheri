from django.test import TestCase
from .forms import BlogPostForm, ContactMessageForm, UserRegisterForm

class TestForms(TestCase):
    def test_blogpost_form_valid_data(self):
        form = BlogPostForm(data={
            'title': 'Wired',
            'subtitle': 'Jeff Beck',
            'content': '1976',
            'category': 'Jazz-Rock',
        })
        self.assertTrue(form.is_valid())

    def test_contact_message_form_valid_data(self):
        form = ContactMessageForm(data={
            'name': 'Natalia',
            'lastname': 'Natalia',
            'message': 'Este es un mensaje de prueba: Hola 123 probando',
        })
        self.assertTrue(form.is_valid())

    def test_user_register_form_valid_data(self):
        form = UserRegisterForm(data={
            'username': 'usuario_test',
            'email': 'test@ejemplo.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        self.assertTrue(form.is_valid())