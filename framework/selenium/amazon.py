from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
driver.get('https://amazon.in')
driver.implicitly_wait(30)

'''
login_xpath="//*[@id='nav-link-accountList-nav-line-1']"
driver.find_element_by_xpath(login_xpath).click()
driver.implicitly_wait(30)
#-----------

email="ABc@gmaIl.com"
password=""
login_id="ap_email"
password=""
driver.find_element_by_id(login_id).send_keys()
'''

all_xpath="/html/body/div[1]/header/div/div[4]/div[1]/a/i"
driver.find_element_by_xpath(all_xpath).click()


