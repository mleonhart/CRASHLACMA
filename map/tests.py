from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase

from map.views import map_home

class MapIndexPageTest(TestCase):

	def test_uses_map_template(self):
		response = self.client.get('/map/')
		self.assertTemplateUsed(response, 'map/map_home.html')
    
