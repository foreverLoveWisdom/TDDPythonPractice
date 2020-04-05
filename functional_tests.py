# Functional test == Acceptance Test == End-to-End Test == Black Box Test
# Test how the users see our app.

from selenium import webdriver
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
        self.fail("Finish the test!")
        # She types "buy peacock feathers" into a text box
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        # She enters "Use peacock feathres to make a fly"
        # The page updates again, and now shows both items on her list
        # The page generated a unique URL for her -- There is some explanatory text to that effect.
        # She visits that URL - her to-do list is still there.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
