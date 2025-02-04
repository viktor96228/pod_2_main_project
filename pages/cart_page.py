from adodbapi.examples.xls_write import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    basket = "//*[@id='content_main']/div[1]/h1" # Корзина
    pulse_contr_cart = "//*[@id='cart']/tbody/tr/td[2]/a" # Импульсный регулятор напряжения в корзине
    price_pulse_contr_cart = "//span[@class='price_wrapper']" # цена в корзине
    deseon = "//*[@id='delete_checked']" # Удалить выбранные
    dyvt = "//*[@id='roothtml']/body/div[2]/div/div/div/div/div/h3"
    del_seon = "//*[@id='fancyConfirm_ok']"

 #Getters


    def get_baskets(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket)))

    def get_pulse_contr_carts(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pulse_contr_cart)))

    def get_price_pulse_contr_carts(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_pulse_contr_cart)))

    def get_deseons(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.deseon)))

    def get_dyvts(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dyvt)))

    def get_del_seons(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.del_seon)))

    # Action


    def clic_deseons(self):
        self.get_deseons().click()
        print("clic Удалить выбранные")


    def clic_del_seons(self):
        self.get_del_seons().click()
        print("clic Да")

    #Methods


    def select_baskets(self):
        with allure.step("Select baskets"):
            Logger.add_start_step(method="Select_baskets")
            self.assert_word(self.get_baskets(), 'Корзина')
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="Select_baskets")

    def select_pulse_contr_carts(self):
        with allure.step("Select pulse contr carts"):
            Logger.add_start_step(method="Select_pulse_contr_carts")
            self.assert_word(self.get_pulse_contr_carts(),'FSCQ0765RTYDTU, Импульсный регулятор напряжения [TO-220-5 FP (Formed Leads)]')
            Logger.add_end_step(url=self.driver.current_url, method="Select_pulse_contr_carts")

    def select_price_pulse_contr_carts(self):
        with allure.step("Select price pulse contr carts"):
            Logger.add_start_step(method="Select_price_pulse_contr_carts")
            self.assert_word(self.get_price_pulse_contr_carts(), '220 руб.')
            Logger.add_end_step(url=self.driver.current_url, method="Select_price_pulse_contr_carts")


    def select_deseons(self):
        with allure.step("Select deseons"):
            Logger.add_start_step(method="Select_deseons")
            self.clic_deseons()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="Select_deseon")

    def select_dyvts(self):
        with allure.step("Select dyvts"):
            Logger.add_start_step(method="Select_dyvts")
            self.assert_word(self.get_dyvts(), 'Удалить выбранные')
            Logger.add_end_step(url=self.driver.current_url, method="Select_dyvts")


    def select_del_seons(self):
        with allure.step("Select del seons"):
            Logger.add_start_step(method="Select_del_seons")
            self.clic_del_seons()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="Select_del_seons")
