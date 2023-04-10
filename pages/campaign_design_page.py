import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CampaignDesignPage(BasePage):
    ADD_NEW_VARIATION = (By.ID, "add-new-variation")
    ADD_NEW_VARIANT_BUTTON = (By.ID, "add-new-variation")
    TEMPLATE_LIST = (By.CLASS_NAME, 'template-list')
    SELECT_INSTORY_TEMPLATE = (By.XPATH, '//*[@class ="template-list"]//li//*[text()="Single Story"]')
    OKBUTTON = (By.LINK_TEXT, 'OK')
    NOTIFICATION_CONFIRM = (By.CLASS_NAME, "inline-select-notification-confirm")
    SWITCH_IFRAME = (By.XPATH, '//*[@id="iframe-edit"]')
    # PARTNER_HEADER = (By.CSS_SELECTOR, '#masthead .top-header')
    HEADER_WRAPPER = (By.CLASS_NAME, 'header-navigation-wrap')
    BEFORE_INSTORY_TEMPLATE = (By.CLASS_NAME, 'append-before')
    SAVE_BUTTON = (By.ID, 'save')
    NEXT_BUTTON = (By.ID, "save-and-next")
    TEMPLATE_LIST_ELEMENTS = 'li'

    def campaign_design_step(self):
        self.add_new_variation()
        campaign_id = self.get_campaign_id()
        self.select_template()
        self.append_template()
        self.insert_template()
        self.click_element(*self.NEXT_BUTTON)
        time.sleep(10)
        self.click_element(*self.NEXT_BUTTON)
        return campaign_id

    def add_new_variation(self):
        self.wait_for_element_clickable(self.ADD_NEW_VARIATION).click()

    def get_campaign_id(self):
        return self.driver.current_url.split('/')[6]

    def select_template(self):
        time.sleep(20)
        self.visibility_of_element(*self.SELECT_INSTORY_TEMPLATE)
        self.wait_for_element_clickable(self.SELECT_INSTORY_TEMPLATE)
        self.hover_move_to_element(*self.SELECT_INSTORY_TEMPLATE)
        self.wait_for_element_clickable(self.SELECT_INSTORY_TEMPLATE_BUTTON)
        time.sleep(1)
        self.click_element(*self.SELECT_INSTORY_TEMPLATE_BUTTON)

    def append_template(self):
        time.sleep(10)
        self.wait_for_element_clickable(self.OKBUTTON)
        time.sleep(1)
        self.click_element(*self.OKBUTTON)

    def insert_template(self):
        time.sleep(1)
        self.wait_for_element_clickable(self.HEADER_WRAPPER).click()
        self.wait_for_element_clickable(self.BEFORE_INSTORY_TEMPLATE).click()
        time.sleep(1)
        self.click_element(*self.SAVE_BUTTON)