# import action
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from utilities.logger import Logger


class Mikros_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    pulse_contr = "//*[@id='content_main']/div[1]/div[1]/h1"  # Импульсный регулятор напряжения text
    price_pulloutreg = "//span[@id='totalPrice']"  # цена импульсного регулятора
    info_basket = "//*[@id='ordering']/div[5]/button/span"  # в корзину
    the_shopping = "//*[@id='ordering']/div[5]/button/span" # Добавить в корзину

    # Getters

    def get_pulse_contr(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pulse_contr)))

    def get_price_pulloutreg(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_pulloutreg)))

    def get_info_baskets(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.info_basket)))

    def get_the_shoppings(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.the_shopping)))

    # Action

    def clic_info_baskets(self):
        self.get_info_baskets().click()
        print("clic в корзину")

    def clic_the_shoppings(self):
        self.get_the_shoppings().click()
        print("clic Корзина")

    # Methods

    def select_pulse_contr(self):
        with allure.step("Select pulse contr"):
            Logger.add_start_step(method="Select_pulse_contr")
            self.assert_word(self.get_pulse_contr(),'FSCQ0765RTYDTU, Импульсный регулятор напряжения [TO-220-5 FP (Formed Leads)]')
            self.assert_word(self.get_price_pulloutreg(),'220')
            Logger.add_end_step(url=self.driver.current_url, method="Select_pulse_contr")

    def select_info_baskets(self):
        with allure.step("Select info baskets"):
            Logger.add_start_step(method="Select_info_baskets")
            self.clic_info_baskets()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="Select_info_baskets")

    def select_the_shoppings(self):
        with allure.step("Select the shoppings"):
            Logger.add_start_step(method="select_the_shoppings")
            self.clic_the_shoppings()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="select_the_shoppings")
