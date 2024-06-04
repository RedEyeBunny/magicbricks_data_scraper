from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()


def scrape(city: str):
    url = f'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=1,2,' \
          f'3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,' \
          f'Villa,Residential-Plot&cityName={city}'
    driver.get(url)
    time.sleep(2)
    count = 0  # maintains the number of scrolls performed,only for debugging purposes
    orig_len_title = 0#maintains the number of entries in previous iteration,useful for slicing
    while True:
        time.sleep(1)
        title = driver.find_elements(By.CLASS_NAME, 'mb-srp__card__container')
        per_sq_ft = driver.find_elements(By.CLASS_NAME, "mb-srp__card__price--size")

        if count == 0:
            for info in title:  # iterate over all elements in the list
                print(info.find_element(By.TAG_NAME, 'h2').text)

            '''
            for info in per_sq_ft:
                print(info.text)
            '''

            print('1st List length:', orig_len_title)
            print("END OF LIST")
            print('Scroll No. ', count)

        else:
            new_titles = title[orig_len_title:]  # debugging purposes

            for info in title[orig_len_title:]:  # from next of last element of last list to end of new list
                print(info.find_element(By.TAG_NAME, 'h2').text)
            # per_sq_ft=driver.find_elements(By.CLASS_NAME,"mb-srp__card__price--size")
            # orig_len_title += len(title)
            print('old title list length:', orig_len_title)
            print('new title list length:', len(title))
            print('number of new entries in new title list:', len(new_titles))
            print("END OF LIST")
            print('Scroll No. ', count)

        orig_len_title = len(title)  # updates the previous title list length,i.e the older length
        # print ('count:',count,' ','title length:',len(title),' ','per_sq_ft Length:',len(per_sq_ft))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        count += 1
        time.sleep(1)


scrape("Surat")
