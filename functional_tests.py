# Functional test == Acceptance Test == End-to-End Test == Black Box Test
# Test how the users see our app.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a coole new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists.
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # She types "buy peacock feathers" into a text box
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        # She enters "Use peacock feathres to make a fly"
        inputbox.send_keys('Buy peacock feathers')
        # The page updates again, and now shows both items on her list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathres' for row in rows), "New to-do item did not appear in table")
        # The page generated a unique URL for her -- There is some explanatory text to that effect.
        # She visits that URL - her to-do list is still there.
        # self.fail('Finish the test!')


if __name__ == "__main__":
    unittest.main(warnings="ignore")
