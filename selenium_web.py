from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('C:\Program Files\Google\Chrome\Application\chrome.exe')

    def get_info(self, query):
        self.query = query
        self.driver.get( "https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        # search.click()
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        enter =self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        # enter.click()

        time.sleep(2)
        self.driver.quit()

# assist=infor()
# assist.get_info('neutron stars')