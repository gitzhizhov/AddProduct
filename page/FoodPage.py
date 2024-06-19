
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from page.BasePage import BasePage
from locators.LocatorsFoodPage import *



class FoodPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def click_button_add(self):
        self.click_element(locator_button_add)

    def click_button_save(self):
        self.click_element(locator_button_save)

    def select_type(self, locator, type):
        '''
        Метод выбора типа товара
        :param locator:
        :param type:
        :return:
        '''
        select = Select(self.find_element(locator))
        self.find_element(locator).click()
        sleep(1)
        if type == 'Фрукт': select.select_by_value('FRUIT')
        if type == 'Овощ': select.select_by_value('VEGETABLE')

    def adding_product(self, prod_name, prod_type, is_exotic):
        '''
        Метод добавления товара
        :param prod_name:
        :param prod_type:
        :param is_exotic:
        :return:
        '''
        self.click_element(locator_field_name)
        self.fill_field(locator_field_name, prod_name)
        self.select_type(locator_select_type, prod_type)
        self.set_checkbox(locator_checkbox_exotic, is_exotic)

    def check_add_product(self):
        '''
        Метод проверки добавленного товара
        :return:
        '''
        i = len(self.driver.find_elements(By.XPATH, '//tbody/tr')) # Считаем кол-во записей
        #print(i) # 4
        name_p = self.driver.find_element(By.XPATH, f'//table/tbody/tr[{i}]/td[1]').text
        type_p = self.driver.find_element(By.XPATH, f'//table/tbody/tr[{i}]/td[2]').text
        exot_p = self.driver.find_element(By.XPATH, f'//table/tbody/tr[{i}]/td[3]').text
        print(f'name: {name_p}, type: {type_p}, exotic {exot_p}')

    def reset_products(self):
        '''
        Метод очиски стриницы товаров
        :return:
        '''
        self.click_element(locator_sandbox)
        self.click_element(locator_reset)



