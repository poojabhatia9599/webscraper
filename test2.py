from selenium import webdriver
import re
import pandas as pd
from bs4 import BeautifulSoup
chrome_path = r"C:\Users\ajite\Desktop\web scraping\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.google.co.in/destination/map/topsights?q=list+of+places+to+visit+in+goa&safe=active&site=search&output=search&dest_mid=/m/01c1nm&sa=X&ved=0ahUKEwi0wJHBkJzZAhULto8KHckgAW4Q6tEBCC0oBDAA')

header = driver.find_elements_by_xpath("/html/body/div[5]/div[2]/div/ol/li")
place = []
short_desc = []
detailed_desc = []
rating = []
review_no = []
x = 1
for i in header:
    if x == 5:
        detailed_desc.append('-')
        
    temp = i.text
    x = 1
    data = temp.splitlines()
    
    for d in data:
        
        if x == 1:
            place.append(d)
            x = 2
        elif x == 2:
            
            
            if d.replace('.','',1).isdigit():
                rating.append(d)
                x = 3
            else:
                rating.append(0)
                review_no.append(0)
                short_desc.append(d)
                x = 5
        elif x == 3:
            review_no.append(d)
            x = 4
        elif x == 4:
            short_desc.append(d)
            x = 5
        elif x == 5:
            detailed_desc.append(d)
            x = 1
detailed_desc.append('-')

df = pd.DataFrame({'place': place, 'rating': rating, 'Short Description': short_desc, 'Detailed Description': detailed_desc})

df.to_csv(r'C:\Users\ajite\Desktop\web scraping\goa_data.csv')




