import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Menu_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    menu = "//button[@id='catalog_button']" # Каталог товаров
    component = "//a[@id='cm_1730']" # Электронные компоненты
    elect_comp = "//h1[@data-id='1730']" # Электронные компоненты
    microcircuit = "//a[@class='link link_dark like-header like-header_3']" # Микросхемы
    crocir = "//h1[@data-id='1731']" # Микросхемы
    ac_dc = "//*[@id='content_main']/div[1]/div[2]/div[1]/div/div/div/a" # AC-DC Преобразователи, Off-Line коммутаторы
    acdc_off = "//h1[@data-id='2015']"  # AC-DC Преобразователи, Off-Line коммутаторы
    pullout_reg = "//*[@id='item9500050172']/td[1]/div/a"  # Импульсный регулятор напряжения

    # Getters

    def get_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_components(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.component)))

    def get_elect_compon(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.elect_comp)))

    def get_microcircuits(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.microcircuit)))

    def get_crocirs(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.crocir)))

    def get_ac_dcp(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ac_dc)))

    def get_acdcp_off(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.acdc_off)))

    def get_pullout_regs(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pullout_reg)))


   # Action

    def clic_menu(self):
        self.get_menu().click()
        print("clic Каталог")

    def clic_components(self):
        self.get_components().click()
        print("clic Электронные компоненты")

    def clic_microcircuits(self):
        self.get_microcircuits().click()
        print("clic Микросхемы")

    def clic_ac_dcp(self):
        self.get_ac_dcp().click()
        print("clic AC-DC Преобразователи, Off-Line коммутаторы")

    def clic_pullout_regs(self):
        self.get_pullout_regs().click()
        print("clic FSCQ0765RTYDTU, Импульсный регулятор напряжения [TO-220-5 FP (Formed Leads)]")


   # Methods

    def select_menu(self):
        with allure.step("Select menu"):
            Logger.add_start_step(method="select_menu")
            self.get_current_url()
            self.clic_menu()
            Logger.add_end_step(url=self.driver.current_url, method="select_menu")

    def select_components(self):
        with allure.step("Select Электронные компоненты"):
            Logger.add_start_step(method="select_components")
            self.clic_components()
            self.get_current_url()
            self.assert_word(self.get_elect_compon(),'Электронные компоненты')
            Logger.add_end_step(url=self.driver.current_url, method="select_components")

    def select_microcircuits(self):
        with allure.step("Select микросхемы"):
            Logger.add_start_step(method="select_microcircuits")
            self.clic_microcircuits()
            self.get_current_url()
            self.assert_word(self.get_crocirs(), 'Микросхемы')
            Logger.add_end_step(url=self.driver.current_url, method="select_microcircuits")


    def select_ac_dcp(self):
        with allure.step("Select ac_dcp"):
            Logger.add_start_step(method="select_ac_dcp")
            self.clic_ac_dcp()
            self.get_current_url()
            self.assert_word(self.get_acdcp_off(), "AC-DC Преобразователи, Off-Line коммутаторы")
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_3")

    def select_pullout_regs(self):
        with allure.step("Select pullout_regs"):
            Logger.add_start_step(method="select_pullout_regs")
            self.clic_pullout_regs()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="select_pulvol_regs")

