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
		#but she does not yet know what that means
		self.assertIn('CRASH LACMA', self.browser.title)  
		self.fail('Finish the test!')  

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  