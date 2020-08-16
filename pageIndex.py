class pageindex():
    def __init__(self):
        self.query_top = 'search_query_top'
        self.quert_button = 'submit_search'
        self.driver = my_driver

    def search(self, item):
        self.driver.find_element_by_id(self.query_top).send_keys('hola')
        self.driver.find_element_by_name(self.quert_button).click()
