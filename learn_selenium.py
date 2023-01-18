from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://web3.dgpa.gov.tw/want03front/AP/WANTF00001.ASPX')

select = Select(driver.find_element(By.XPATH, '/html/body/form/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div[3]/div[2]/select'))
btn = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_IS_NOT_OFFICE')
btn_search = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_btnQUERY')

time.sleep(2)
select.select_by_index(6)
time.sleep(1)
btn.click()
time.sleep(1)
btn_search.click()
time.sleep(1)

text = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[1]/div[1]/div[2]/div[5]/div/div/div/div[2]/div[1]/table/tbody')

print(text.text)

time.sleep(10)


