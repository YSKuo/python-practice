import os
from dotenv import load_dotenv
from selenium import webdriver
import time

load_dotenv()

chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
money = driver.find_element_by_id("money")

timeout = time.time() + 5
five_min = time.time() + 60*5

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]


def buy_item():
    available_items = driver.find_elements_by_css_selector(
        "#store > div:not(div[class='grayed'])")
    if len(available_items) > 0:
        last_item = available_items[-1]
        print(last_item.text)
        last_item.click()

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:
        buy_item()
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(f"cookies/second: {cookie_per_s}")
        break
