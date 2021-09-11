import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv()

chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# target = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# target.click()

# search = driver.find_element_by_css_selector("input[name='search']")
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)


driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys('yi')
l_name = driver.find_element_by_name("lName")
l_name.send_keys('hoo')
email = driver.find_element_by_name("email")
email.send_keys('test@tset.com')
submit = driver.find_element_by_css_selector('button')
submit.click()

# driver.quit()
