__author__ = 'switbe'
from selenium.webdriver.common.by import By
from .base_page_object import BasePage
class MyAddress(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)
        self.su = context.su

    locator_dictionary = {
        "addAddressButton": (By.XPATH, '//a[@title="Add an address"]'),
        "address1": (By.ID, 'address1'),
        "city": (By.ID, 'city'),
        "id_state": (By.ID, 'id_state'),
        "postcode": (By.ID, 'postcode'),
        "id_country": (By.ID, 'id_country'),
        "phone": (By.ID, 'phone'),
        "alias": (By.ID, 'alias'),
        "submitAddressButton": (By.ID, 'submitAddress'),
        "state_options": (By.XPATH, "//*[@id='id_state']/option"),
        "country_options": (By.XPATH, "//*[@id='id_country']/option"),
        "selected_country": (By.CSS_SELECTOR, "#uniform-id_country > span"),
        "selected_state": (By.CSS_SELECTOR, "#uniform-id_state > span"),
        "addressesList": (By.CSS_SELECTOR, "div.address"),
        "addressLines": (By.CSS_SELECTOR, "ul > li"),
        "update_btn": (By.XPATH, "a[@title='Update']"),
        "delete_btn": (By.XPATH, "a[@title='Delete']"),
    }

    def get_address_details(self, parentElement):
        return self.su.find_elements_under_parent_element(parentElement, *self.locator_dictionary['addressLines'])

    def is_address_existed(self, address_alias):
        for webEle in self.addressesList:
            checking_address_alias = self.su.get_text_web_element(self.get_address_details(webEle)[0])
            if checking_address_alias.lower() == address_alias.lower():
                return True
        return False

    def delete_address(self, address_alias):
        flag = False
        for webEle in self.addressesList:
            list_address_detail_lines = self.get_address_details(webEle)
            #For each address item, check for its alias
            checking_address_alias = self.su.get_text_web_element(list_address_detail_lines[0])
            if checking_address_alias.lower() == address_alias.lower():
                #Click Delete button on address item to be removed
                delete_address_button = self.su.find_elements_under_parent_element(list_address_detail_lines[-1], *self.locator_dictionary['delete_btn'])
                self.su.click_element(delete_address_button)
                self.su.wait_for_alert_then_accept()
                flag = True
                break

        #Return "True" if deleting address has happened, otherwise, return False
        return flag

    def update_address (self, address_alias):
        new_address_alias = None
        for webEle in self.addressesList:
            list_address_detail_lines = self.get_address_details(webEle)
            #For each address item, check for its alias
            checking_address_alias = self.su.get_text_web_element(list_address_detail_lines[0])
            if checking_address_alias.lower() == address_alias.lower():
                #Click Update button on address item to be updated
                update_address_button = self.su.find_elements_under_parent_element(list_address_detail_lines[-1], *self.locator_dictionary['update_btn'])
                self.su.click_element(update_address_button)
                #Updates go here
                self.su.enter_text(self.su.get_value_web_element(self.address1) + "Updated", self.address1)
                self.su.enter_text(self.su.get_value_web_element(self.city) + "Updated", self.city)
                new_address_alias = self.su.get_value_web_element(self.alias) + "Updated"
                self.su.enter_text(new_address_alias, self.alias)
                self.su.click_element(self.submitAddressButton)
                break

        #Return new value of alias if address updating has happened, otherwise, return None
        return new_address_alias

    def add_address(self, addressDetails):
        flag = self.is_address_existed(addressDetails["alias"])
        if flag is False:
            self.su.click_element(self.addAddressButton)
            self.su.enter_text(addressDetails["address1"], self.address1)
            self.su.enter_text(addressDetails["city"], self.city)
            defaultState = self.su.get_text_web_element(self.selected_state)
            if defaultState != addressDetails["state_option"]:
                self.su.click_element_forcefully(self.id_state)
                self.su.select_option_from_select_list(addressDetails["state_option"], self.state_options)
            self.su.enter_text(addressDetails["postcode"], self.postcode)
            defaultCountry = self.su.get_text_web_element(self.selected_country)
            if defaultCountry != addressDetails["country_option"]:
                self.su.click_element_forcefully(self.id_country)
                self.su.select_option_from_select_list(addressDetails["country_option"], self.country_options)
            self.su.enter_text(addressDetails["phone"], self.phone)
            self.su.enter_text(addressDetails["alias"], self.alias)
            self.su.click_element(self.submitAddressButton)
        #Return "True" if adding address has happened, otherwise, return False
        return not flag