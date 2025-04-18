from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url='C:\Program Files\Google\Chrome\Application\chrome.exe')

    def play(self, query):
        self.query = query
        self.driver.get( "http://www.youtube.com/results?search_query="+ query)
        video = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        video.click()


assist=music()
assist.play('hanuman chalisa')