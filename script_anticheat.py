try:
    import pyautogui
    import warnings
    import random
    import string
    import time
    import sys

    from selenium.webdriver.common.action_chains import ActionChains
    from datetime import timedelta
    from selenium import webdriver
    from datetime import datetime
except:
    print("Some libraries failed to load. Please check that you have installed all the required libraries.")
    import sys
    sys.exit()

warnings.filterwarnings("ignore", category=DeprecationWarning)

try:
    browser = webdriver.Chrome(executable_path = "chromedriver")
    browser.get("http://monkeytype.com/")
except:
    print("Failed to find/load the Chrome Driver. Please make sure it is in the same directory as the program.")
    print("If you are using MacOS, please recheck the installation instructions in the readme file.")
    sys.exit()

error = False
count = 0

def count_down(length):
    for i in range(length):
        print(length, "    ", end = "\r")
        length -= 1
        time.sleep(1)

def type_text(error, count, start, words):
    pyautogui.PAUSE = 0
    for word in words:
        for char in word.get_attribute("textContent"):
            try:
                if random.randint(1,100) == 1:
                    pyautogui.write(random.choice(string.ascii_letters), interval = algorithm(True, count, start))
                    time.sleep(random.randint(1,8)/100)
                    if random.randint(1,1) == 1:
                        pyautogui.press("backspace")
                pyautogui.write(char, interval = algorithm(False, count, start))
            except:
                sys.exit()
        pyautogui.write(" ", interval = algorithm(False, count, start))

def given_word_count(error, count):
    print("You have 30s to sign in and select the desired typing test", end = "\r")
    time.sleep(5)
    count_down(25)
    try:
        words = browser.find_elements_by_class_name("word")
    except:
        print("Unable to find the words to type on the website. Check the right page is loaded.")
        browser.close()
        sys.exit()
    start = time.time()
    type_text(error, count, start, words)

def algorithm(error, count, start):
    if error == True:
        error = False
        return random.randint(5,8)/150
    else:
        while time.time() - start <= 1:
            print("Beginning  ", end = "\r")
            return random.randint(1,7)/190
        while time.time() - start > 1 and time.time() - start <= 3:
            print("Pre-middle ", end = "\r")
            return random.randint(2,8)/190
        while time.time() - start > 6 and time.time() - start <= 8:
            print("Pre-ending ", end = "\r")
            return random.randint(2,7)/190
        while time.time() - start > 8 and time.time() - start <= 15:
            print("Ending     ", end = "\r")
            return random.randint(1,5)/180
        while time.time() - start > 3 and time.time() - start < 6:
            print("Middle     ", end = "\r")
            return random.randint(3,5)/180

def main(error, count):
    print('\033[?25l', end="")
    given_word_count(error, count)

if __name__ == "__main__":
    main(error, count)
