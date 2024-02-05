import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

rows = []

def scrapping():
    for page in range(1, 10, 1):  # should be to 50 as there are 50 pages but it takes too long
        print(page)
        page_url = "http://books.toscrape.com/catalogue/page-" + str(page) + ".html"

        options = webdriver.ChromeOptions()
        # Ajoutez d'autres options si nécessaire

        driver = webdriver.Chrome( options=options)
        driver.get(page_url)
        all_li = driver.find_element(By.XPATH, '//ol[@class="row"]')

        for li in all_li.find_elements(By.XPATH, './/article[@class="product_pod"]'):
            titre = li.find_element(By.XPATH, './/h3/a').text
            prix = li.find_element(By.XPATH, './/p[@class="price_color"]').text
            status = li.find_element(By.XPATH, './/p[@class="instock availability"]').text
            rows.append((titre, prix, status))
            print(rows)
        
        driver.close()

    df = pd.DataFrame(rows, columns=["titre", "prix", "status"])
    df.to_csv(f"test.csv", index=False)

mydf=scrapping()
