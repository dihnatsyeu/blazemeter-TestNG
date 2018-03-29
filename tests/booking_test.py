
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.BaseTest import BaseTest



@pytest.mark.incremental
class TestBooking(BaseTest):


    @pytest.mark.parametrize("url", ["http://blazedemo.com/"])
    def test_search_flight(self, url):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get(url)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[value='Find Flights']"))).click()


    def test_choose_any_flight(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Choose This Flight']"))).click()
        text = self.driver.find_element_by_tag_name("h2").text
        with pytest.raises(AssertionError):
            assert text == "Your flight from Paris to Boston has been reserved."
        print "Seems like you have booked incorrect flight!"
