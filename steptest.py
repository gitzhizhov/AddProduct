import time

import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


home_page_url = 'http://localhost:8080/'
food_page_url = 'http://localhost:8080/food'


chrome_option = webdriver.ChromeOptions()
driver = webdriver.Chrome()

# открываем стартовую страницу
driver.get(home_page_url)
driver.maximize_window() # разворачиваем на весь экран
time.sleep(2)



# locators home_page
locator_sandbox = (By.XPATH, '//a[@id = \'navbarDropdown\']') # песочница
locator_product = (By.XPATH, '//a[.= \'Товары\']') # товары
locator_reset = (By.XPATH, '//a[@id=\'reset\' and .=\'Сброс данных\']') # сброс данных

# locators food_page
locator_button_add = (By.XPATH, '//button[@type = \'button\' and .=\'Добавить\']') # кнопка добавить
locator_title_adding_product = (By.XPATH, '//div[@class=\'modal-dialog\']//h5[.=\'Добавление товара\']') # всплывающее окно Добавление товара
locator_field_name = (By.XPATH, '//input[@id=\'name\']') # поле наименование
locator_select_type = (By.XPATH, '//select[@name=\'type\']') # селектор выбора типа
locator_checkbox_exotic = (By.XPATH, '//input[@id=\'exotic\' and @type=\'checkbox\']') # чекбокс экзотик
locator_button_save = (By.XPATH, '//button[.=\'Сохранить\']') # кнопка сохранить
locator_table = (By.XPATH, '//tbody/tr') # таблица



def find_element(locator, time=5):
    return WebDriverWait(driver, time).until(EC.presence_of_element_located(locator),
                                                  message=f'Элемент по локатору {locator} не найден')

def click_element(locator):
    find_element(locator, time=2).click()
    time.sleep(1)

def fill_field(locator, value):
    find_element(locator).send_keys(value)


def select_type(locator, type):
    #dropdown = driver.find_element(By.XPATH, '//select[@name=\'type\']')
    #dropdown.click()
    #select = Select(dropdown)
    select = Select(find_element(locator))
    find_element(locator).click()
    time.sleep(1)
    if type == 'Фрукт': select.select_by_value('FRUIT')
    if type == 'Овощ': select.select_by_value('VEGETABLE')

def set_checkbox(locator, value):
    if value:
        find_element(locator).click()
    time.sleep(1)



def adding_product(prod_name, prod_type, is_exotic):
    fill_field(locator_field_name, prod_name)
    select_type(locator_select_type, prod_type)
    set_checkbox(locator_checkbox_exotic, is_exotic)



def goto_to_food_page():
    click_element(locator_sandbox)
    click_element(locator_product)
    print(driver.current_url) # http://localhost:8080/food

def add_product():
    click_element(locator_button_add)
    #
    #fill_field(locator_field_name)
    #select_type(locator_select_type)
    #set_checkbox(locator_checkbox_exotic)
    #
    adding_product('Mango', 'Фрукт', True)
    time.sleep(2)
    click_element(locator_button_save)


def check_add_product():
    i = len(driver.find_elements(By.XPATH, '//tbody/tr')) # Считаем кол-во записей
    name_p = driver.find_element(By.XPATH, f'//table/tbody/tr[{i}]/td[1]').text
    type_p = driver.find_element(By.XPATH, f'//table/tbody/tr[{i}]/td[2]').text
    exot_p = driver.find_element(By.XPATH, f'//table/tbody/tr[{i}]/td[3]').text
    print(f'name: {name_p}, type: {type_p}, exotic {exot_p}')



def reset_products():
    click_element(locator_sandbox)
    click_element(locator_reset)


goto_to_food_page()
add_product()
check_add_product()
reset_products()


# работает
# element_sandbox1 = driver.find_element(By.XPATH, '//a[@id = \'navbarDropdown\']')
# element_sandbox1.click()
# time.sleep(2)
# element_product1 = driver.find_element(By.XPATH, '//a[.= \'Товары\']')
# element_product1.click()
# time.sleep(2)



def quit_driver():
    driver.quit()