import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

time_tags = driver.find_elements_by_css_selector(
    "div.medium-widget.event-widget.last ul li time")
event_tags = driver.find_elements_by_css_selector(
    "div.medium-widget.event-widget.last ul li a")

# time_list = [tag.text for tag in time_tags]

events = {}

for idx, time_tag in enumerate(time_tags):
    events[idx] = {
        'time': time_tag.text,
        'name': event_tags[idx].text
    }

print(events)

# driver.close()
driver.quit()
