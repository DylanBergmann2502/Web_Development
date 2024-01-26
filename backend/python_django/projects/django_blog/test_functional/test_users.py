import os
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#These are functional tests
class TestLogin_Logout(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/login/')

    def tearDown(self):
        self.driver.close()

    def test_form_no_data(self):
        login = self.driver.find_element(By.ID, 'login')
        login.send_keys(Keys.RETURN)
        assert 'Log In' in self.driver.page_source

    def test_form_valid(self):
        username = self.driver.find_element(By.NAME,'username')
        password = self.driver.find_element(By.NAME,'password')
        login = self.driver.find_element(By.ID,'login')

        username.send_keys(os.environ.get('WEB_USERNAME'))
        password.send_keys(os.environ.get('WEB_PASS'))
        login.send_keys(Keys.RETURN) # press enter the button

        assert 'New Post' in self.driver.page_source # This verifies that the form works
        # Test logout
        logout = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Logout')
        logout.send_keys(Keys.RETURN)
        assert 'Login' in self.driver.page_source # In case, there is a post containing the keyword "login" or "register
        assert 'Register' in self.driver.page_source

    def test_forgot_pwd(self):
        forgot_pwd = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Forgot')
        forgot_pwd.send_keys(Keys.RETURN)
        assert 'Reset Password' in self.driver.page_source

    def test_sign_up(self):
        sign_up = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign Up')
        sign_up.send_keys(Keys.RETURN)
        assert 'Join Today' in self.driver.page_source

class TestRegister(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/register/')

    def tearDown(self):
        self.driver.close()

    def test_form_no_data(self):
        sign_up = self.driver.find_element(By.ID, 'sign-up')
        sign_up.send_keys(Keys.RETURN)
        assert 'Join Today' in self.driver.page_source

    def test_form_invalid(self):
        username = self.driver.find_element(By.NAME,'username')
        password1 = self.driver.find_element(By.NAME,'password1')
        password2 = self.driver.find_element(By.NAME, 'password2')
        sign_up = self.driver.find_element(By.ID,'sign-up')

        username.send_keys('sleeping_at_last')
        password1.send_keys('@Sleeping_at_last1') #the password is too similar to the username
        password2.send_keys('@Sleeping_at_last1')
        sign_up.send_keys(Keys.RETURN)

        assert 'Join Today' in self.driver.page_source

    def test_form_valid(self):
        username = self.driver.find_element(By.NAME,'username')
        password1 = self.driver.find_element(By.NAME,'password1')
        password2 = self.driver.find_element(By.NAME, 'password2')
        sign_up = self.driver.find_element(By.ID,'sign-up')

        username.send_keys('sleeping_at_last')
        password1.send_keys('@Dylan_Bergmann1')
        password2.send_keys('@Dylan_Bergmann1')
        sign_up.send_keys(Keys.RETURN)

        assert 'Log In' in self.driver.page_source

class TestProfile(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8000/login/')

    def tearDown(self):
        self.driver.close()

    def test_profile(self):
        # log the user in
        username_login = self.driver.find_element(By.NAME, 'username')
        password_login = self.driver.find_element(By.NAME,'password')
        login = self.driver.find_element(By.ID,'login')

        username_login.send_keys(os.environ.get('WEB_USERNAME'))
        password_login.send_keys(os.environ.get('WEB_PASS'))
        login.send_keys(Keys.RETURN)

        # click on profile
        profile = self.driver.find_element(By.LINK_TEXT, 'Profile')
        profile.send_keys(Keys.RETURN)

        assert 'Profile Info' in self.driver.page_source

        # # These tests fail due to selenium.common.exceptions.StaleElementReferenceException:
        # # Message: stale element reference: element is not attached to the page document
        # # test form w/o passing any data
        # email_profile = self.driver.find_element(By.ID, 'update')
        # update_text = self.driver.find_element(By.ID,"update")
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'update')))
        # update_text.click()
        #
        # assert 'locducnguyen' in self.driver.page_source
        #
        # # test form with new data
        # email_profile.send_keys('dylanbergmann020@gmail.com')
        # update_text.click()