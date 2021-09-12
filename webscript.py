from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://celestrak.com/NORAD/archives/request.php')

time.sleep(2)

RequestorFullName = "Saad Imran Rana"
fname = web.find_element_by_xpath('/html/body/div/form/table/tbody/tr[1]/th/div[2]/input')
fname.send_keys(RequestorFullName)

RequestorEmail = "saadlacas@gmail.com"
emailaddr = web.find_element_by_xpath('/html/body/div/form/table/tbody/tr[2]/th/div[2]/input')
emailaddr.send_keys(RequestorEmail)

NoradCatalaogueNumbers = "47414\n47142"
NoradCatno = web.find_element_by_xpath('/html/body/div/form/table/tbody/tr[5]/td[1]/textarea')
NoradCatno.send_keys(NoradCatalaogueNumbers)

SDate = "2021-01-01"
StartDate = web.find_element_by_xpath('/html/body/div/form/table/tbody/tr[5]/td[2]/input')
StartDate.send_keys(SDate)

EDate = "2021-09-01"
EndDate = web.find_element_by_xpath('/html/body/div/form/table/tbody/tr[5]/td[3]/input')
EndDate.send_keys(EDate)

SubmitReq = web.find_element_by_xpath('/html/body/div/form/p[5]/input[1]')
time.sleep(10)
SubmitReq.click()