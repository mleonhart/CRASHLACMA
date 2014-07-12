from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from main.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('main/home.html')
        self.assertEqual(response.content.decode(), expected_html)
    
class AboutPageTest(TestCase):

	def test_uses_about_template(self):
		response = self.client.get('/about/')
		self.assertTemplateUsed(response, 'main/about.html')