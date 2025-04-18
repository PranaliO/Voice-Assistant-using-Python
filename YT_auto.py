from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class music():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url='C:\Program Files\Google\Chrome\Application\chrome.exe')

    def play(self, query):
        self.query = query
        self.driver.get( "http://www.youtube.com/results?search_query="+ query)
        video = self.driver.find_element(By.XPATH, '//*[@id="dismissable"]')
        # search.click()
        video.send_keys(query)
        video.send_keys(Keys.RETURN)
        # enter =self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        # enter.click()

        time.sleep(2)
        self.driver.quit()

# assist=music()
# assist.play('beliver')