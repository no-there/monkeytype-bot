import time

from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
from selenium import webdriver

browser = webdriver.Chrome(executable_path = 'chromedriver')
browser.get('http://monkeytype.com')
keyboard = Controller()

time.sleep(30)

def type_text(words):
    for word in words:
        word = word.get_attribute("textContent")
        for char in word:
            keyboard.press(char)
            keyboard.release(char)
        keyboard.press(" ")
        keyboard.release(" ")

type_text(words = browser.find_elements_by_class_name("word"))
