from selenium import webdriver
import unittest
import time


class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/chromedriver')
        self.driver.get('https://uat-guaranteefunds.mobeats.com.ar/#/')
        self.driver.implicitly_wait(5)
        self.indexPage = PageIndex(self.driver)

    # @unittest.skip("not needed now")
    def test_loginFontenla(self):
        self.indexPage.search('mfontenla')
        time.sleep(3)

    ''' #@unittest.skip("not needed now")
    def test_loginAcindar(self):
        self.indexPage.search('20342952829@4')
        time.sleep(3)

    def test_loginNacion(self):
        self.indexPage.search('27274277446')
        self.driver_find_element_by_xpath("//*[@id='main_navbar']/div/div/div/ul[2]/li/a")'''

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
