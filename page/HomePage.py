from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page.BasePage import BasePage
from locators.LocatorsHomePage import *



class HomePage(BasePage):

    #driver = DriverManager()
    def __init__(self, driver):
        self.driver = driver
        self.home_url = 'http://localhost:8080/'

    def goto_to_food_page(self):
        '''
        Методе перехода на стриницу товаров
        :return:
        '''
        self.click_element(locator_sandbox)
        self.click_element(locator_product)

    # !проверка заголовка стриницы продукты
    def check_food_page(self):
        '''
        Метод проверки заголовка стриницы
        :return: заголовок стриницы
        '''
        return self.driver.current_url


    def reset_products(self):
        '''
        Метод очиски стриницы товаров
        :return:
        '''
        self.click_element(locator_sandbox)
        self.click_element(locator_reset)