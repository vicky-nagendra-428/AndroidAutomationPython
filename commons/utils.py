from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Utils:

    def __init__(self, utils_driver):
        self.driver = utils_driver

    def get_element_identification_method(self, element_identifier_type):

        if element_identifier_type == 'id':
            return MobileBy.ID
        elif element_identifier_type == 'class name':
            return MobileBy.CLASS_NAME
        elif element_identifier_type == 'xpath':
            return MobileBy.XPATH

    def get_element(self, element_identifier_string, element_identifier_type):
        return self.driver.find_element(self.get_element_identification_method(element_identifier_type),
                                        element_identifier_string)

    def wait_for_element_visibility(self, element_identifier_string, element_identifier_type):
        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((self.get_element_identification_method(element_identifier_type),
                                            element_identifier_string)))

    def get_elements(self, element_identifier_string, element_identifier_type):
        return self.driver.find_elements(self.get_element_identification_method(element_identifier_type),
                                         element_identifier_string)

    def click_the_element(self, element_identifier_string, element_identifier_type):
        self.wait_for_element_visibility(element_identifier_string, element_identifier_type)
        self.get_element(element_identifier_string, element_identifier_type).click()
        print("========> Element click is successful, for : " + element_identifier_type + " : " + element_identifier_string)

