from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Firefox()

driver.get("https://ban8sso.pima.edu/ssomanager/c/SSB?pkg=bwpktais.P_SelectTimeSheetRoll")

userName = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

userName.send_keys("Username")
password.send_keys("Password")
password.send_keys(Keys.RETURN)

try:
    payperiods = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"period_1_id"))
    )
except:
    driver.quit
    pass

class PayPeriod:
    def __init__(self,startMonth,startDay):
        self.startMonth = startMonth
        self.startDay = startDay

regex = "(?P<startMonth>\w{3}) (?P<startDay>\d{2}), (?P<startYear>\d{4}) to (?P<endMonth>\w{3}) (?P<endDay>\d{2}), (?P<endYear>\d{4}) (?P<status>(\w+\s{1}\w+)|(\w+))"
pay_period = []
for line in payperiods.text.splitlines():
    match = re.match(regex,line)
    pay_period.append(PayPeriod(match.group('startMonth'), match.group('startDay')))

print(pay_period)
driver.quit