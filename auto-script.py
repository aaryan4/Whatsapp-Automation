from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.keys import Keys


import autoit
import os
import csv
import time

caps = DesiredCapabilities().CHROME

options = webdriver.ChromeOptions()

prefs = {'profile.default_content_setting_value': {'images': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='./drivers/chromedriver',
                          desired_capabilities=caps, options=options)

file_name = './data.csv'
csvFile = open(file_name, 'rt')
csvReader = csv.reader(csvFile, delimiter=",")


# phones = list()
# for row in csvReader:
#     phones.append(row)
#     phones_length = len(phones)
#     print(phones_length)

phone_numbers = []
for number in csvReader:
    phone_numbers.append(number)

phones = phone_numbers.pop(0)
# phones = ['+919910218097', '+919953072648']
# phones_length = len(phones)


def start(phone):
    url = 'https://web.whatsapp.com/send?phone='+phone
    driver.get(url)
    time.sleep(3)

    # send_button = driver.find_element_by_xpath('//*[@id="action-button"]')
    # send_button.click()
    # time.sleep(3)

    filepath = os.getcwd() + r'\dummy.pdf'
    # whatsappweb_button = driver.find_element_by_xpath(
    #     '//*[@id="fallback_block"]/div/div/a')
    # whatsappweb_button.click()
    # time.sleep(5)

    attachment_button = driver.find_element_by_xpath(
        '//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    time.sleep(2)
    attachment_button.click()
    time.sleep(3)

    file_button = driver.find_element_by_xpath(
        '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button')
    file_button.send_keys(filepath)
    time.sleep(2)
    file_button.click()

    autoit.control_focus("Open", "Edit1")
    autoit.control_set_text("Open", "Edit1", (filepath))
    autoit.control_click("Open", "Button1")
    time.sleep(2)

    filepath = 'dummy.pdf'
    autoit.control_focus("Open", "Edit1")
    autoit.control_set_text("Open", "Edit1", (filepath))
    autoit.control_click("Open", "Button1")

    time.sleep(3)

    file_send_button = driver.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
    file_send_button.click()


for phone in phones:
    start(phone)
