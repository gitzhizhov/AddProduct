
from selenium import webdriver

class DriverManager():

    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver