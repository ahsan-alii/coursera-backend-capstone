from django.test import TestCase
from django.urls import reverse
from .models import Booking

class TestHomeView(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class TestBookView(TestCase):
    def test_book_view_get(self):
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')

    def test_book_view_post_valid_form(self):
        valid_form_data = {
            'field1': 'value1',
            'field2': 'value2',
            # Add more form fields as needed
        }
        response = self.client.post(reverse('book'), data=valid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Success')

    def test_book_view_post_invalid_form(self):
        invalid_form_data = {
            'field1': '',
            'field2': 'value2',
            # Add more form fields as needed
        }
        response = self.client.post(reverse('book'), data=invalid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Invalid form')
        self.assertIn('errors', response.json())

class TestMenuView(TestCase):
    def test_menu_view(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    # Add more tests for the menu view as needed

# Add more view test cases for other views as needed
