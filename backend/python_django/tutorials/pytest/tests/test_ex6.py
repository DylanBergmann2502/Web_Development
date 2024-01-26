import pytest
from django.test import LiveServerTestCase
from selenium import webdriver

# Example 1
# class TestBrowser1(LiveServerTestCase):
#     def test_example(self):
#         driver = webdriver.Chrome("./chromedriver")
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title

# Example 2
# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title

# Example 3
# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()