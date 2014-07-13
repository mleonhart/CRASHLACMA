from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase

from projection.views import projection_home

class projectionIndexPageTest(TestCase):

	def test_uses_projection_template(self):
		response = self.client.get('/projection/')
		self.assertTemplateUsed(response, 'projection/projection_home.html')
    
