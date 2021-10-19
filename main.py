from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
firefox_options = Options()
firefox_options.set_preference('detach', True)
driver.get("https://linkcom.muroran-it.ac.jp")
driver.find_element(By.NAME, "LoginUserID").send_keys("15999833")
driver.find_element(By.NAME, "LoginPassword").send_keys("15999833")
driver.find_element(By.NAME, "LoginBtn").click()

driver.find_element(By.LINK_TEXT, "伝言メモ").click()





