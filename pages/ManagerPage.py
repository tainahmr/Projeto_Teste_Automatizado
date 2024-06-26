from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject

class ManagerPage(PageObject):

    add_customer = (By.CSS_SELECTOR, '[ng-click="addCust()"]')
    open_Account = (By.CSS_SELECTOR, '[ng-click="openAccount()"]')
    customers = (By.CSS_SELECTOR, '[ng-click="showCust()"]')

    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)

    # Clica na aba "Adicionar cliente"
    def click_add_customer_button(self):
        add_customer_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_customer))
        add_customer_button_element.click()

    # Clica na aba "Abrir conta"
    def click_open_account_button(self):
        open_account_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.open_Account))
        open_account_button_element.click()

    # Clica na aba "Clientes"
    def click_customers_button(self):
        customers_button_element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.customers))
        customers_button_element.click()