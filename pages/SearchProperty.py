
from pages.PageSetup import PageSetupClass


class SearchProperty(PageSetupClass):

    def __init__(self):
        super(SearchProperty, self).__init__()
        self.driver = self.page_setup_driver
        self.load_page_elements()

    def load_page_elements(self):
        self.property_search_link = {"method": "xpath", "value": '//android.widget.LinearLayout[@content-desc="Property Search"]/android.widget.TextView'}
        self.property_type_alert_title = {'method': 'id', 'value': 'android:id/alertTitle'}
        self.property_search_dropdowns = {'method': 'id', 'value': 'com.android.sig:id/button'}
        self.property_type_text = {'method': 'id', 'value': 'android:id/text1'}
        self.search_button = {'method': 'id', 'value': 'com.android.sig:id/btnSearch'}

    def click_on_property_search_link(self):
        self.utils.click_the_element(self.property_search_link['value'], self.property_search_link['method'])

    def check_property_search_form_is_displayed(self):
        self.utils.wait_for_element_visibility(self.property_search_dropdowns['value'], self.property_search_dropdowns['method'])

    def select_value_from_property_type_dropdown(self, text1):
        psform_dropdowns = self.utils.get_elements(self.property_search_dropdowns['value'], self.property_search_dropdowns['method'])

        for dropdown in psform_dropdowns:
            if dropdown.text == 'Some Text':
                dropdown.click()
                break

        property_type_texts = self.utils.get_elements(self.property_type_text['value'], self.property_type_text['method'])

        for propertyTypeTextElement in property_type_texts:
            if propertyTypeTextElement.text == text1:
                propertyTypeTextElement.click()
                break

    def click_on_search_button(self):
        self.utils.click_the_element(self.search_button['value'], self.search_button['method'])
