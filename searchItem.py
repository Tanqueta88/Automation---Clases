import unittest
from selenium import webdriver
import time
#from pageIndex import PageIndex
#from pageItems import PageItems

class SearchCases(unittest.TestCase):

    def test_setUp(self):
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/chromedriver')
        self.driver.get('http:automationpractice.com/index.php')
        time.sleep(4)

    '''def setUp(self):
        self.driver = webdriver.Chrome('/PycharmProjects/pythonProject/chromedriver')
        self.driver.get('http:automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemPage = PageItems(self.driver)

    def test_search_find_elements(self):
        self.indexPage.search('hola')
        time.sleep(2)
        self.assertEqual(self.itemPage.return_no_element_text(), 'No results were found for your search "hola"')

    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemPage.return_selection_title())

    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        time.sleep(3)
        self.assertTrue('T-SHIRT' in self.itemPage.return_selection_title())'''

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
