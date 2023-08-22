# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def start():
    print("starting the earning process")

    # Set up the browser driver (choose the appropriate driver for your browser)
    driver = webdriver.Chrome()  # Change this to the appropriate driver if not using Chrome

    driver.get("https://watch.recast.tv/login")

    # Wait for the button to reappear
    timeout = 20  # Adjust the timeout as needed
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.presence_of_element_located((By.NAME, "email")))

    text_field = driver.find_element(By.NAME, "email")
    text_to_input = ""  # Input email of recast account
    text_field.send_keys(text_to_input)

    text_field = driver.find_element(By.NAME, "password")
    text_to_input2 = ""  # Input password of recast account
    text_field.send_keys(text_to_input2)

    submit_button = driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/form/button")
    submit_button.click()

    # Wait for the button to reappear
    timeout = 20  # Adjust the timeout as needed
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "headerMeProfileButton__icon")))

    while True:
            driver.get("https://watch.recast.tv/watch-and-earn")
            # Wait for the button to reappear
            timeout = 50
            wait = WebDriverWait(driver, timeout)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "adPlayer__playButton")))

            print("Play button reappeared!")

            # Find and click the button
            button = driver.find_element(By.CLASS_NAME, "adPlayer__playButton")
            button.click()

            # Wait for the button to reappear
            timeout = 50
            wait = WebDriverWait(driver, timeout)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div.watchAndEarnScreen > div.adPlayerPlaceholder.adPlayerPlaceholder--desktop > div.adPlayerPlaceholder__centerLayout > button")))

            print("replay button reappeared!")

            button = driver.find_element(By.CSS_SELECTOR, "#root > div.watchAndEarnScreen > div.adPlayerPlaceholder.adPlayerPlaceholder--desktop > div.adPlayerPlaceholder__centerLayout > button")
            button.click()

            print("1 Point!!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
