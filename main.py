from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

google_form_url = "https://forms.gle/cDNF9L8gwi2k1a9XA"
zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=zillow_clone_url)
zillow_clone_webpage = response.text

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=google_form_url)

soup = BeautifulSoup(zillow_clone_webpage, "html.parser")

all_listings = soup.find_all(name="div", class_='StyledCard-c11n-8-84')

time.sleep(2)

for listing in all_listings:

    title = listing.find("address").getText().replace("\n", '').replace('|', ",").strip()
    price = listing.find("span", class_="PropertyCardWrapper__StyledPriceLine").getText().split("/")[0].replace("+", "").replace("1 bd","").replace("1bd","").strip()
    link = listing.find("a").get("href")

    time.sleep(1)

    # Get fresh inputs each time.
    all_questions = driver.find_elements(By.CSS_SELECTOR, value=".Xb9hP input")
    submit_button = driver.find_element(By.CSS_SELECTOR, value=".uArJ5e ")

    all_questions[0].send_keys(title)
    all_questions[1].send_keys(price)
    all_questions[2].send_keys(link)

    time.sleep(1)
    submit_button.click()
    time.sleep(2)

    # Wait for confirmation page to load and click "Submit another"
    submit_another_response_button = driver.find_element(By.CSS_SELECTOR, value=".c2gzEf a")
    submit_another_response_button.click()
    time.sleep(1)


driver.close()