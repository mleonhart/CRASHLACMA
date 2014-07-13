from selenium import webdriver
import unittest


class NewOutsideVisitorTest(unittest.TestCase): 

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()
	
	def check_link(self, link_location_id, link_text, expected_url):
		nav_text = self.browser.find_element_by_id(link_location_id).text
		self.assertIn(link_text, nav_text)
		self.browser.find_element_by_link_text(link_text).click()
		new_url = self.browser.current_url
		self.assertRegex(new_url, expected_url)
		
	def check_page_content(self, has_text, doesnothave_text):
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn(has_text, page_text)
		self.assertNotIn(doesnothave_text, page_text)
		
	def test_can_navigate_to_all_the_main_nav_pages(self): 
		# Edith has heard about a cool project happening at LACMA and
		# decided to find out more about it via its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention CRASH LACMA
		# but she doesn't really get what is going on.
		self.assertIn('CRASH LACMA', self.browser.title)  
		
		# and decides to clicking on the About link in the main navigation area
		# and it takes her to a page with a comprehensible URL and relevant content. 
		self.check_link('main-navbar', 'About', '/about')
		self.check_page_content('tweet images', 'Donec sed odio dui.')
		
		# she then decides to view the Map page page. 
		self.check_link('main-navbar', 'Map', '/map')
		self.check_page_content('This is a map.', 'Donec sed odio dui.')
		
		# and then the Browse page 
		self.check_link('main-navbar', 'Browse', '/browse')
		self.check_page_content('Browse the tweeted images', 'Donec sed odio dui.')

		# she then returns to the home page. 
		self.browser.find_element_by_class_name('navbar-brand').click()
		self.check_page_content('This is a website.', 'Donec sed odio dui.')

		# with a better understanding of what is going on she closes her web browser
		#... and tweets! (how to test that!!!???)  

class ProjectorTest(unittest.TestCase): 

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()
	
	# not DRY, whats a better test for this page?
	def check_projection_page_content(self, has_text, doesnothave_text):
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn(has_text, page_text)
		self.assertNotIn(doesnothave_text, page_text)

	# Michele needs to start up the projection so she navigates to the
	# server/projection page
	def test_can_load_projection_page(self): 
		#need refactoring to not reference localhost:8000
		self.browser.get('http://localhost:8000/projection') 
		
	# she notices....
	def test_layout_and_styling(self):
		#not dry, hard url dependent
		self.browser.get('http://localhost:8000/projection')

		#should we test 800 by 600?
		self.browser.set_window_size(1024, 768)

		# She notices the content is nicely centered ...
		#(not yet checking for vertical centeredness)
		content_container = self.browser.find_element_by_class_name('content')
		self.assertAlmostEqual(
			content_container.location['x'] + content_container.size['width'] / 2,
			512,
			delta=5
		)
		
		# ... and the background is a sleek black
		body_element = self.browser.find_element_by_tag_name('body')
		self.assertEqual(body_element.value_of_css_property('background-color'), 'rgba(0, 0, 0, 1)')
		

		#Not really done yet
		#self.fail('Finish the test!')  

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  