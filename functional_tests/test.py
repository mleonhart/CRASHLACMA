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
		
	
	def test_can_start_a_list_and_retrieve_it_later(self): 
		# Edith has heard about a cool project happening at LACMA and
		# decided to find out more about it via its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention CRASH LACMA
		# but she doesn't really get what is going on.
		self.assertIn('CRASH LACMA', self.browser.title)  
		
		# and decides to clicking on the About link in the main navigation area
		# and it takes her to a page with a comprehensible URL and relevant content. 
		self.check_link('main-navbar', 'About', '/about')
		self.check_page_content('tweet images', 'lorem ipsum dolor sit amet')

		# she then returns to the home page. 
		self.browser.find_element_by_class_name('navbar-brand').click()
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('This is a website.', page_text)
		
		# she then decides to view the Map page page. 

		# and then the browse page

		# with a better understanding of what is going on she closes her web browser
		#... and tweets! (how to test that!!!)

		#Not really done yet
		self.fail('Finish the test!')  

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  