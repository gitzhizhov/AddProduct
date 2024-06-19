#локаторы страницы товаров

from selenium.webdriver.common.by import By

locator_button_add = (By.XPATH, '//button[@type = \'button\' and .=\'Добавить\']') # кнопка добавить
locator_title_adding_product = (By.XPATH, '//div[@class=\'modal-dialog\']//h5[.=\'Добавление товара\']') # всплывающее окно Добавление товара
locator_field_name = (By.XPATH, '//input[@id=\'name\']') # поле наименование
locator_select_type = (By.XPATH, '//select[@name=\'type\']') # селектор выбора типа
locator_checkbox_exotic = (By.XPATH, '//input[@id=\'exotic\' and @type=\'checkbox\']') # чекбокс экзотик
locator_button_save = (By.XPATH, '//button[.=\'Сохранить\']') # кнопка сохранить
locator_table = (By.XPATH, '//tbody/tr') # таблица

locator_sandbox = (By.XPATH, '//a[@id = \'navbarDropdown\']') # песочница
locator_reset = (By.XPATH, '//a[@id=\'reset\' and .=\'Сброс данных\']') # сброс данных