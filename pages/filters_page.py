import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class FiltersPage(Base):
    """Устанавливаем нужные фильтры"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    all_filters = "div.navisort-line-one.swiper-slide.swiper-slide-active span:nth-child(3) .navisort-item__content"
    list_publ_house = "#section-search-form > div:nth-child(4) > div.bl-name.block-pubhouse-bl-name"
    publ_house = "div.viewport.row > div > div:nth-child(1) > label"
    list_cover = "#section-search-form > div:nth-child(6) .bl-name"
    cover = "#section-search-form > div:nth-child(6) .inputs div:first-child"
    button_show = ".show-goods > input.show-goods__button"
    main_value = ".navisort-part.navisort-head.navisort-part-7 > span.navisort-head-text.navisort-head-books-count"

    # Getters

    def get_all_filters(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.all_filters)))

    def get_list_publ_house(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.list_publ_house)))

    def get_publ_house(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.publ_house)))

    def get_list_cover(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.list_cover)))

    def get_cover(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.cover)))

    def get_button_show(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_show)))

    def get_main_value(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_value)))

    # Actions

    def click_all_filters(self):
        ActionChains(self.driver).move_to_element(self.get_all_filters()).click().perform()
        print('Filters is open')

    def click_list_publ_house(self):
        ActionChains(self.driver).move_to_element(self.get_list_publ_house()).click().perform()

    def click_publ_house(self):
        ActionChains(self.driver).move_to_element(self.get_publ_house()).click().perform()

    def close_list_publ_house(self):
        ActionChains(self.driver).move_to_element(self.get_list_publ_house()).click().perform()

    def click_list_cover(self):
        ActionChains(self.driver).move_to_element(self.get_list_cover()).click().perform()

    def click_cover(self):
        ActionChains(self.driver).move_to_element(self.get_cover()).click().perform()

    def close_list_cover(self):
        ActionChains(self.driver).move_to_element(self.get_list_cover()).click().perform()

    def click_button_show(self):
        ActionChains(self.driver).move_to_element(self.get_button_show()).click().perform()
        print('Click button')

    def hover_main_value(self):
        ActionChains(self.driver).move_to_element(self.get_main_value()).perform()

    # Methods

    def filters_fields(self):
        with allure.step("Filters fields"):
            self.click_all_filters()
            self.click_list_publ_house()
            self.click_publ_house()
            self.close_list_publ_house()
            self.click_list_cover()
            self.click_cover()
            self.close_list_cover()
            self.click_button_show()
            self.hover_main_value()
