from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase

from browse.views import browse_home

class browseIndexPageTest(TestCase):

	def test_uses_browse_template(self):
		response = self.client.get('/browse/')
		self.assertTemplateUsed(response, 'browse/browse_home.html')
    
