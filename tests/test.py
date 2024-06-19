
import pytest

from time import sleep
from page.HomePage import HomePage
from page.FoodPage import FoodPage
from tests.conf_test import *

prod_name = 'Lychee'
prod_type = 'Фрукт'
prod_exotic = True

def test_check_adding_product(browser):
    home_page = HomePage(browser)
    food_page = FoodPage(browser)

    home_page.go_to_site() # переходим на стартовую страницу сайта

    home_page.goto_to_food_page() # переходим на стриницу товаров
    assert home_page.check_food_page() == 'http://localhost:8080/food' # проверяем заголовок
    sleep(1)

    food_page.click_button_add() # кликаем по кнопке Добавить
    food_page.adding_product(prod_name, prod_type, prod_exotic) # добавляем товар
    food_page.click_button_save() # кликаем по кнопке сохранить
    sleep(1)

    food_page.check_add_product() # провуряем добавленный продукт

    food_page.reset_products() # сброс данных

