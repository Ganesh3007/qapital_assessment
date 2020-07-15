from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class Trello(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C://Users//msdpr//Downloads//chromedriver_win32//chromedriver.exe')

    def test_flow(self):
        driver = self.driver
        
        driver.get('https://trello.com/login')
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="user"]').send_keys('msdprabu8@gmail.com')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="login"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('ganesh123@')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login-submit"]').click()
        time.sleep(30)

        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/ul/li[3]/div/p/span').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/form/div[1]/div/div[1]/input').send_keys('testing')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="chrome-container"]/div[3]/div/div/div/form/div[2]/button/span[2]').click()

        driver.find_element_by_xpath('//*[@id="board"]/div/form/input').send_keys('TO do')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="board"]/div/form/div/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="board"]/div[2]/form/a/span').click()
        driver.find_element_by_xpath('//*[@id="board"]/div[2]/form/input').send_keys('Done')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="board"]/div[2]/form/div/input').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="board"]/div[1]/div/div[3]/a/span[2]').click()
        driver.find_element_by_xpath('//*[@id="board"]/div[1]/div/div[2]/div/div[1]/div/textarea').send_keys('list1')
        driver.find_element_by_xpath('//*[@id="board"]/div[1]/div/div[2]/div/div[2]/div[1]/input').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="board"]/div[1]/div/div[1]/div[2]/a').click()
        driver.find_element_by_xpath('//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/ul[1]/li[3]/a').click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



