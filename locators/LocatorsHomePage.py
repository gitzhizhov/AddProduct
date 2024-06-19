#локаторы стартовой(домашней) стриницы

from selenium.webdriver.common.by import By

locator_sandbox = (By.XPATH, '//a[@id = \'navbarDropdown\']') # песочница
locator_product = (By.XPATH, '//a[.= \'Товары\']') # товары
locator_reset = (By.XPATH, '//a[@id=\'reset\' and .=\'Сброс данных\']') # сброс данных