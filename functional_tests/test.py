from selenium import webdriver
import unittest

class NewOutsideVisitorTest(unittest.TestCase): 

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self): 
		# Edith has heard about a cool project happening at LACMA and
		# decided to find out more about it via its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention CRASH LACMA
		# but she doesn't really get what is going on.
		self.assertIn('CRASH LACMA', self.browser.title)  

		# She notices sees and About link  
		# in the main navigation area (check for style? location?)
		nav_text = self.browser.find_element_by_id('main-navbar').text
		self.assertIn('About', nav_text)

		# and decides to clicking on the link. 
		self.browser.find_element_by_link_text('About').click()

		# she is on a page with about in the URL
		new_url = self.browser.current_url
		self.assertRegex(new_url, '/about')

		# she can read about text that says what this project is 
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('tweet images', page_text)
		self.assertNotIn('Levi is the Man. But he really is, though. He is the one dude on the project.', page_text)

		# she then returns to the home page. 
		self.browser.find_element_by_class_name('navbar-brand').click()
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertIn('This is a website.', page_text)


		#Not really done yet
		self.fail('Finish the test!')  

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  