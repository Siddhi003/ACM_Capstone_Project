from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib3
import urllib.request

searchterm = 'cat on white background' #will also be the name of the folder
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
#NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome(executable_path = 'D:/Projects/chromedriver.exe')
browser.get(url)
header = {'User_Agent': "Chrome/84.0.4147.105"}
counter = 0
succounter = 0
    
print ("start scrolling to generate more images on the page...")
#500 times we scroll down by 10000 in order to generate more images on the website

    
for _ in range(10):
    browser.execute_script("window.scrollBy(0, 10000)")
    
print("start scraping...")
    
for x in browser.find_elements_by_xpath('//*[@id="islrg"]/div/div/a/div/img'):
    counter = counter + 1
    print("Total Count: ", counter)
    print("Successfull Count: ", succounter)
    print("URL: ", x.get_attribute('src'))
    
    img = x.get_attribute('src')
    new_filename = "image" + str(counter) + ".jpg"
    
    try:
        path = 'D:/Projects/cat on white background/'
        path += new_filename
        urllib.request.urlretrieve(img, path)
        succounter = succounter + 1
    except Exception as e:
        print(e)
        
print(succounter, "pictures successfully downloaded")
browser.close()