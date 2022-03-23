#Importing libraries 
import time 
import os
from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import csv

#Selenium Webdriver 
os.environ['PATH'] += r"/home/umair/Documents/python/driver"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

#searching bergen companies in Google maps 
driver.get("https://www.google.nl/maps/search/bergen+companies/@52.6803052,4.6817917,14z/data=!3m1!4b1?authuser=0&hl=en")
time.sleep(3)
html=driver.page_source

#scrolling down the page
time.sleep(3)
result=driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[13]/div/a ')
driver.execute_script("arguments[0].scrollIntoView();", result)
                                   
time.sleep(3)                      #/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[25]/div/a  
result1=driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[27]/div/a')
driver.execute_script("arguments[0].scrollIntoView();", result1)

time.sleep(4)              
result2=driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/div[39]/div/a')
driver.execute_script("arguments[0].scrollIntoView();", result2)

#Locating the results section 
time.sleep(4)
entries=driver.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
scroll=driver.find_elements_by_css_selector('div[class="siAUzd-neVct section-scrollbox"]')

#just checking out that how many companies are there in one page
l=len(entries)
print("total companies link in current page ", l)

#opening a csv file
file = open('companydetails.csv', 'w')  #creating a csv file to store data 
write=csv.writer(file)   

write.writerow(["Company Name", "Address", "Phone Number", "Website"])

#function for phone number and website 
def phone_website(text1):        
    text_blob=text1.splitlines()
    website=""
    aux_number=""
    phone=""

    company_name = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text
    
    try:
        address = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]').text
    except NoSuchElementException:
        address="No address could be found"

    for line in range(len(text_blob)):
        
            if "closed" in text_blob[line].lower() or "open" in text_blob[line].lower() or "claim this" in text_blob[line].lower():
                aux_number = ""
            
            if text_blob[line].startswith('+31') or text_blob[line].startswith('31'):
                phone = text_blob[line]
    
            if text_blob[line].endswith('.nl'):
                website = 'https://' + text_blob[line]

    print('')
    print("details of company")
    print(f"company_name: {company_name}")
    print(f"address: {address}")
    print(f"phone: {phone}")
    print(f"website: {website}")
    #print(f"aux: {aux_number}")

    write.writerow([company_name, address, phone, website])


#Extracting the information
link_list=[]   
for entry in entries:
    #time.sleep(3)
    link=entry.get_attribute('href')
    #print(link)
    link_list.append(link)

#opening the link of each company one by one and extracting data
for links in link_list:
    driver.get(links)
    time.sleep(4)

    junk_block=driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[7]').text
    phone_website(junk_block)
    print('')

file.close()
