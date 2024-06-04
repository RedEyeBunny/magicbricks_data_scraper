from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=1,2,"
           "3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,"
           "Villa,Residential-Plot&cityName=Surat")
driver.fullscreen_window()
l1=[]
count=0
while True:
    title = driver.find_elements(By.CLASS_NAME, 'mb-srp__card__container')
    per_sq_ft = driver.find_elements(By.CLASS_NAME, "mb-srp__card__price--size")

    if count == 0:
        for info in title:  # iterate over all elements in the list
            print(info.find_element(By.TAG_NAME, 'h2').text)
        for info in per_sq_ft:
            print(info.text)
        break
        '''
        orig_len_title += len(title)  # Increment orig_len_title by the length of the title list
        print('List length:', orig_len_title)
        print("END OF LIST")
        '''