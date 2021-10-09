import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C://Users/Ivakhnenko/PycharmProjects/practice_24/chromedriver.exe')
   pytest.driver.implicitly_wait(10)

   pytest.driver.get('http://petfriends1.herokuapp.com/login')


   yield

   pytest.driver.quit()

