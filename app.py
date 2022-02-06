import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Variables
page_rae = 'https://dle.rae.es/'
executable_path = "/home/mario/Documentos/code/projects/rae_scrapwords/geckodriver"
word = 'pelaje'

def create_driver(executable_path):
    serv = Service(executable_path=executable_path)
    driver_local = webdriver.Firefox(service=serv)
    return driver_local


def start(driver, page):
    driver.get(page)
    interaction(driver)
    finish(driver)


def interaction(driver):
    word_form = driver.find_element(By.ID, 'wq')
    word_form.send_keys(word, Keys.ENTER)
    time.sleep(3)
    definitions = driver.find_elements(By.XPATH, "//div[@id='resultados']/article")

    for definition in definitions:
        definition_get = definition.find_element(By.XPATH, './/p')
        print(definition_get)


def finish(driver):
    driver.close()

start(create_driver(executable_path), page_rae)