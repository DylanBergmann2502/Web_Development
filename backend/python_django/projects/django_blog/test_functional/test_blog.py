import os

from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumlogin import force_login

#These are functional tests
class TestHome(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/')

    def tearDown(self):
        self.driver.close()

    # test navigation bar
    def test_about(self):
        about = self.driver.find_element(By.LINK_TEXT, 'About')
        about.send_keys(Keys.RETURN)
        assert 'About Page' in self.driver.page_source

        # go back to home
        home = self.driver.find_element(By.LINK_TEXT, 'Home')
        home.send_keys(Keys.RETURN)
        assert 'Post' in self.driver.page_source

    def test_login(self):
        login = self.driver.find_element(By.LINK_TEXT, 'Login')
        login.send_keys(Keys.RETURN)
        assert 'Log In' in self.driver.page_source

    def test_register(self):
        login = self.driver.find_element(By.LINK_TEXT, 'Register')
        login.send_keys(Keys.RETURN)
        assert 'Join Today' in self.driver.page_source

    # test page content
    def test_author(self):
        author = self.driver.find_elements(By.PARTIAL_LINK_TEXT, 'Dylan')[0]
        author.send_keys(Keys.RETURN)
        assert 'Posts by' in self.driver.page_source

    def test_author(self):
        author = self.driver.find_elements(By.PARTIAL_LINK_TEXT, 'Dylan')[0]
        author.send_keys(Keys.RETURN)
        assert 'Posts by' in self.driver.page_source

    def test_post(self):
        post = self.driver.find_elements(By.PARTIAL_LINK_TEXT, 'Post')[0]
        post.send_keys(Keys.RETURN) # this is a link which will redirect to the post

        # post_title = self.driver.find_element(By.CLASS_NAME, 'article-title')
        # # this is not a link, just plain text, so clicking on it should display "element not interactable" :>
        # post_title.send_keys(Keys.RETURN)

# I don't have time yet to test post since it requires the messy force login :'>