from selenium import webdriver
import time
import unittest
import HtmlTestRunner


class suite(unittest.TestCase):

#This method is used to initialize the driver and set the path
    def setUp(self):
        self.Chrome_Driver = webdriver.Chrome(executable_path="Chrome_Driver\chromedriver.exe")
        
#This method is used to login to the application entering all the information correctly
    def test_login_with_information(self):
        self.Chrome_Driver.get("https://qa-practical.qa.swimlane.io/login")
        self.Chrome_Driver.implicitly_wait(8)
        self.user = self.Chrome_Driver.find_element_by_id("input-1")
        self.Chrome_Driver.implicitly_wait(8)
        self.user.send_keys("gilberto")
        time.sleep(4)
        self.Chrome_Driver.implicitly_wait(8)
        self.passwd = self.Chrome_Driver.find_element_by_id("input-2")
        self.passwd.send_keys("AuToMaTeN0w!")
        time.sleep(4)
        self.Chrome_Driver.implicitly_wait(8)
        self.button = self.Chrome_Driver.find_element_by_css_selector("#login > div > button")
        self.button.click()
        time.sleep(4)

#This method is used to try to login without any information entered on the textboxes
    def test_login_without_information(self):
        self.Chrome_Driver.get("https://qa-practical.qa.swimlane.io/login")
        self.Chrome_Driver.implicitly_wait(8)
        self.button = self.Chrome_Driver.find_element_by_css_selector("#login > div > button")
        self.button.click()
        time.sleep(4)

#This method is used to try to login just with the username
    def test_login_with_just_user(self):
        self.Chrome_Driver.get("https://qa-practical.qa.swimlane.io/login")
        self.Chrome_Driver.implicitly_wait(8)
        self.user = self.Chrome_Driver.find_element_by_id("input-1")
        self.Chrome_Driver.implicitly_wait(8)
        self.user.send_keys("gilberto")
        self.Chrome_Driver.implicitly_wait(8)
        self.button = self.Chrome_Driver.find_element_by_css_selector("#login > div > button")
        self.button.click()
        time.sleep(4)

#This method is used to make the password visible when doing click on the eye icon
    def test_making_passwd_visible(self):
        self.Chrome_Driver.get("https://qa-practical.qa.swimlane.io/login")
        self.Chrome_Driver.implicitly_wait(8)
        self.passwd = self.Chrome_Driver.find_element_by_id("input-2")
        self.passwd.send_keys("AuToMaTeN0w!")
        self.Chrome_Driver.implicitly_wait(8)
        self.passwd_visible = self.Chrome_Driver.find_element_by_css_selector("#login > ngx-input.ngx-input.ng-tns-c4-3.ng-touched.ng-dirty.ng-valid > div > div.ngx-input-flex-wrap > div > div > span")
        self.passwd_visible.click()
        time.sleep(5)
        self.passwd_visible.click()
        time.sleep(5)

#This method is used to make the password visible from previous method, hidden so no one can see it *****
    def test_making_passwd_hidden(self):
        self.Chrome_Driver.get("https://qa-practical.qa.swimlane.io/login")
        self.Chrome_Driver.implicitly_wait(8)
        self.passwd = self.Chrome_Driver.find_element_by_id("input-2")
        self.passwd.send_keys("AuToMaTeN0w!")
        self.Chrome_Driver.implicitly_wait(8)
        self.passwd_visible = self.Chrome_Driver.find_element_by_css_selector("#login > ngx-input.ngx-input.ng-tns-c4-3.ng-touched.ng-dirty.ng-valid > div > div.ngx-input-flex-wrap > div > div > span")
        self.passwd_visible.click()
        time.sleep(5)

# This method will shutdown the driver
    def tearDown(self):
        self.Chrome_Driver.quit()


# this is the main used to initialize the class
#Also in here we are using the HTMLtestRunner that will generate a report for us
if __name__ == "__main__":
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports"))
     









