#! python3
# 2048.py - Plays 2048 game until game over
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

gameOver = True

while True:
    try:
        htmlElem.send_keys(Keys.HOME)
        elems = browser.find_element_by_link_text('Try again')
        htmlElem.send_keys(Keys.HOME)
        break
    except:
        htmlElem.send_keys(Keys.HOME)
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.HOME)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.HOME)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.HOME)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.HOME)