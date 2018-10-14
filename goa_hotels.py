from selenium import webdriver
import re
import pandas as pd
import time
chrome_path = r"C:\Users\ajite\Desktop\web scraping\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.makemytrip.com/mmthtl/site/hotels/search?checkin=02252018&checkout=02262018&roomStayQualifier=1e0e&city=GOI&searchText=Goa,%20India&country=IN')


two_hotels = driver.find_elements_by_xpath('//*[@id="hotel_card_list"]/div')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);", two_hotels)


two = driver.find_elements_by_xpath('//*[@id="hotel_card_list"]/div')



goa_hotel = []
rating = []
type_of_traveler = []
couple = []
solo = []
nearest_loc = []
price = []
add_ons = []

first = 0
x = 1
for hotel in two:
    print(hotel.text)
    print('\n')
    print('\n')
    
    temp = hotel.text
    traveler = 0
    hotel_name = 0
    add_on = 0
    check = False
    if first == 1:
        first = 2
        continue
    if first != 1:
        hotel_data = temp.splitlines()
        for data in hotel_data:
            if '/' in data:
                rating.append(data)
                add_on = 0
            elif 'traveler' in data:
                if traveler == 0:
                    type_of_traveler.append(data)
                    hotel_name = 1
                    traveler = 1
                elif traveler == 1:
                    old = type_of_traveler[-1]
                    type_of_traveler.pop()
                    type_of_traveler.append(old + "|" + data)
            elif hotel_name == 1 and "#" not in data:
                goa_hotel.append(data)
                hotel_name = 0
                traveler = 0
            elif "km" in data:
                nearest_loc.append(data)
            elif "Rs" in data and "%" in data:
                price.append(data)
            elif "Free" in data:
                if add_on == 0:
                    
                    add_ons.append(data)
                    add_on = 1
                elif add_on == 1:
                    old_add_on = add_ons[-1]
                    add_ons.pop()
                    add_ons.append(old_add_on + "|" + data)
                    
        traveler = 0
        add_on = 0
        if check == False:
            first = 1
            check = True
        else:
            first = 2
print(len(goa_hotel))                
print(len(rating))      
print(len(type_of_traveler))       
print(len(price) )      
print(len(add_ons) )       
print(len(nearest_loc) )

df = pd.DataFrame({'Hotel': goa_hotel, 'rating': rating, 'Type of Traveler': type_of_traveler, 'Price': price, 'Add ons':add_ons, "Nearest Location": nearest_loc })

df.to_csv(r'C:\Users\ajite\Desktop\web #scraping\hotel_goa.csv')
                
                
                
                
                
                
                
                
            
            
        