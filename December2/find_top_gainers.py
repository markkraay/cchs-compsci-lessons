from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Documentation you will need...
# https://www.selenium.dev/documentation/webdriver/locating_elements/
# https://www.selenium.dev/documentation/webdriver/web_element/

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.com/Jabra-Elite-75t-Earbuds-Comfortable/dp/B07X9VG6ZJ?ref_=Oct_DLandingS_D_3d85a924_60&smid=ATVPDKIKX0DER")
stocks = []
for i in range (1, 10):
    stock = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/div/div[2]/div[1]/table/tbody/tr[{i}]/td[2]').text
    price = int(driver.find_element(By.XPATH, f'//*[@id="scr-res-table"]/div[1]/table/tbody/tr[{i}]/td[3]/fin-streamer').text)
    stocks.append({'stock': stock, 'price': price})
print(stocks)

# Finding the max
max_stock = {'price': 0}
for pair in stocks:
    if pair['price'] > max_stock['price']:
        max_stock = pair
print(max_stock)




