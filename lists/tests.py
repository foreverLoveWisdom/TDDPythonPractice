from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'Buy peacock feathers'})
        self.assertIn('Buy peacock feathers', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
