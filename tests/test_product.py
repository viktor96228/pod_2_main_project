import time
import allure
from unittest import result

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from base.base_class import Base
from pages.cart_page import Cart_page
# from pages.cart_page import Cart_page
# from pages.finish_page import Finish_page
from pages.login_page import login_page
from pages.menu_page import Menu_page
from pages.mikros_page import Mikros_page


@allure.description("Test product")
def test_product(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Старт тест Авторизации")
    login = login_page(driver)
    login.authorizations()
    print("Финиш тест Авторизации")
    time.sleep(10)
    print("Старт тест Каталог")
    mp = Menu_page(driver)
    mp.select_menu()
    mp.select_components()
    mp.select_microcircuits()
    mp.select_ac_dcp()
    mp.select_pullout_regs()
    print("Финиш тест Каталог")
    time.sleep(3)
    print("Старт тест выбранного продукта")
    mp = Mikros_page(driver)
    mp.select_pulse_contr()
    mp.select_info_baskets()
    mp.select_the_shoppings()
    print("Финиш тест выбранного продукта")
    print("Старт тест Корзина")
    cp = Cart_page(driver)
    cp.select_baskets()
    cp.select_pulse_contr_carts()
    cp.select_price_pulse_contr_carts()
    cp.select_deseons()
    cp.select_dyvts()
    cp.select_del_seons()
    print("Финиш тест Корзина")

    # f = Finish_page(driver)
    # f.finish()
    #
    # # assert Cart_page.get_cart_lenovo(self) == Note_page.get_lenoo(self)
    # # assert Cart_page.get_cart_price_lenovo(self) == Note_page.get_price_lenoo(self)
    #
    #
    #
    # time.sleep(10)
    # driver.quit()


