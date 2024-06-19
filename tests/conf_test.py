# файл под фикстуры

import pytest

from selenium import webdriver
from managers.DriverManager import DriverManager

@pytest.fixture(scope="session")
def browser():
    driver = DriverManager().get_driver()
    #chrome_option = webdriver.ChromeOptions()
    #driver = webdriver.Chrome(options=chrome_option)
    driver.maximize_window() # разворачиваем на весь экран

    yield driver
    driver.quit()   # закрываем