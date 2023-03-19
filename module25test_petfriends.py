import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver.exe')
   # Переходим на страницу авторизации

   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   # pytest.driver.quit()


def test_show_my_pets():
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('dimapisarev2019@mail.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('gbcfhtd1337228')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
class element_has_css_class(object):
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False