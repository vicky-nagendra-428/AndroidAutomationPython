
import unittest

from pages.SearchProperty import SearchProperty


class SearchPropertyTest(unittest.TestCase):

    def setUp(self):
        print("=============> Setup is run in testcase file")

    def test_OpenPropertySearch(self):
        search_property = SearchProperty()
        search_property.click_on_property_search_link()
        search_property.check_property_search_form_is_displayed()
        search_property.select_value_from_property_type_dropdown("Text1")
        search_property.click_on_search_button()

    def test_can_have_many_tests(self):
        pass

    def tearDown(self):
        print("Suite running completed. \n remember setup and teardown functions run for every test case.")
        print("In this file test case means every function starting with `test_` ")
