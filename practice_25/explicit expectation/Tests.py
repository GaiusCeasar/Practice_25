import pytest
from collections import Counter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_my_pets():

   pytest.driver.find_element_by_id('email').send_keys('arvaindel@gmail.com')

   pytest.driver.find_element_by_id('pass').send_keys('qwerty')

   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   pytest.driver.find_element_by_css_selector('.navbar-toggler-icon').click()

   pytest.driver.find_element_by_link_text('Мои питомцы').click()

   pytest.driver.implicitly_wait(10)
   number_of_pets= WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]"))).text
   number_of_pets=number_of_pets.split()
   number_of_pets=int(number_of_pets[3])

   images=WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/th/img")))
   cards_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr")))
   name = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[1]")))
   age = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[3]")))
   breed = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr/td[2]")))

   """создаю списки , что бы добавить в них фото питомцев и имена для последующих тестов"""
   sp_name_pet=[]
   sp_foto=[]

   for i in range(len(name)):

      """проверяю наличие имен, пород, и возрастов питомцев"""
      assert name[i].text != ''
      assert age[i].text!=''
      assert breed[i].text != ''

      """добавляю в список фотографии питомцев для проверки их количества"""
      r = images[i].get_attribute('src')
      sp_foto.append(r)

      """добавляю в список имена питомцев для последующей проверки совпадения имен"""
      c = name[i].text
      sp_name_pet.append(c)

   """сверяю количество карточек питомцев с их общим количеством"""
   assert number_of_pets == len(cards_pets)

   """создаю словарь повторяющихся вхождений и проверяю, что они все равны 1"""
   povtorenia = Counter(sp_name_pet)
   for key in povtorenia:
      assert povtorenia[key]==1

   """проверяю количество  питомцев без фотографии и сравнием с половиной питомцев"""
   sp_foto = Counter(sp_foto)
   assert sp_foto[''] < number_of_pets / 2
