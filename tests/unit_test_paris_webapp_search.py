import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonMeteoSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_city(self):
        driver = self.driver
        driver.get("http://localhost:5000/")
        assert "Météo" in driver.title
        elem = driver.find_element(By.ID, "search")
        elem.clear()
        elem.send_keys("Paris")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()