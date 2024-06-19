from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,driver):
        self.driver = driver


    def find_element(self, locator, time = 5):
        ''' Ищет один элемент и возвращает его
        :param locator: locator
        :param time: время поиска
        :return: element
        '''
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                 message=f'Элемент по локатору {locator} не найден')

    def find_elements(self, locator, time = 5):
        ''' Ищет множество и возвращает его в виде списка
        :param locator:
        :param time:
        :return:
        '''
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_element_located(locator),
                                                      message=f'Элементы по локатору {locator} не найден')

    def go_to_site(self):
        ''' Метод позволяет перейти на указанную старицу
        :return:
        '''
        return self.driver.get(self.home_url)

    def click_element(self, locator):
        ''' Метод клика по элементу
        :param locator: переданный локатор
        :return:
        '''
        self.find_element(locator).click()
        sleep(1)

    def fill_field(self, locator, value):
        ''' Метод заполнения поля переданный значением
        :param locator: переданный локатор поля
        :param value: переданное значение
        :return:
        '''
        self.find_element(locator).send_keys(value)

    def set_checkbox(self, locator, value):
        ''' Метод установки "флага" чекбокса
        :param locator: переданнй локатор
        :param value: значение. True - чекбокс прожат
        :return:
        '''
        if value:
            self.find_element(locator).click()
        sleep(1)

    def check_url(self):
        ''' Методе возвращает адрес стриницы
        :return:
        '''
        return self.driver.current_url