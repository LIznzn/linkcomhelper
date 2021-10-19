import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox()
firefox_options = Options()
firefox_options.set_preference('detach', True)

# 登录
driver.get("https://linkcom.muroran-it.ac.jp")
driver.find_element(By.NAME, "LoginUserID").send_keys("15999833")
driver.find_element(By.NAME, "LoginPassword").send_keys("15999833")
driver.find_element(By.NAME, "LoginBtn").click()

time.sleep(10)

# 查看邮件数量
driver.get("https://linkcom.muroran-it.ac.jp/Next60/default.cfm?version=next&app_cd=14&fuseaction=kms")
print(driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[0]/div/span/b").text)








