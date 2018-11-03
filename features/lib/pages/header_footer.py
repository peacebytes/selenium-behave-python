from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class HeaderFooter(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)

    locator_dictionary = {
        "sign_in": (By.CSS_SELECTOR, 'div.header_user_info > a.login'),
        "contact_us": (By.LINK_TEXT, 'Contact us'),
        "sign_out": (By.CSS_SELECTOR, 'div.header_user_info > a.logout'),
        "my_account": (By.XPATH, '//a[@title="Manage my customer account"]'),
        "account": (By.CSS_SELECTOR, 'div.header_user_info > a.account')
    }
