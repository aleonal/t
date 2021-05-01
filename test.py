import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class GoogleTestCase(unittest.TestCase):
        
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://opensource-demo.orangehrmlive.com/')
        self.addCleanup(self.browser.quit)

    def test_login(self):

        # Type admin in username
        elem = self.browser.find_element_by_name('txtUsername')    
        elem.clear()
        elem.send_keys("Admin")
        
        # Type in password
        elem = self.browser.find_element_by_name('txtPassword')
        elem.clear()
        elem.send_keys("admin123")

        # Activate Login button
        elem = self.browser.find_element_by_name('Submit')
        elem.send_keys(Keys.RETURN)

        # Assert login did not fail
        assert "Invalid credentials" not in self.browser.page_source
        
        # Assert we are in the dashboard
        assert "Quick Launch" in self.browser.page_source

    def test_add_user(self):
        self.test_login()

        # Navigate to Admin tab
        elem = self.browser.find_element_by_id('menu_admin_viewAdminModule')
        elem.send_keys(Keys.RETURN)

        # Assert we are in the System Users page
        assert "System Users" in self.browser.page_source

        # Activavte button to add a new user
        elem = self.browser.find_element_by_name('btnAdd')
        elem.send_keys(Keys.RETURN)

        # Assert we are in the Add User page
        assert "Add User" in self.browser.page_source
        
        # Select user role as ESS
        self.browser.find_element_by_xpath("//select[@name='systemUser[userType]']/option[text()='ESS']").click()

        # Fill in employee name
        elem = self.browser.find_element_by_id('systemUser_employeeName_empName')
        elem.send_keys('Orange Test')

        # Assert employee exists
        assert "Orange Miner" in self.browser.page_source

        # Fill in employee username
        elem = self.browser.find_element_by_id('systemUser_userName')
        elem.send_keys('imaminer')

        # Select user status as enabled
        self.browser.find_element_by_xpath("//select[@name='systemUser[status]']/option[text()='Enabled']").click()

        # Fill in user password
        elem = self.browser.find_element_by_id('systemUser_password')
        elem.send_keys('test123123')

        # Confirm password
        elem = self.browser.find_element_by_id('systemUser_confirmPassword')
        elem.send_keys('test123123')

        # Activate button to save, a.k.a. add user
        elem = self.browser.find_element_by_id('btnSave')
        elem.send_keys(Keys.RETURN)

        # Assert wer returned to users page
        assert "System Users" in self.browser.page_source
        
        # Assert user was added and is listed in users page
        assert "imaminer" in self.browser.page_source

    def test_delete_user(self):
        self.test_login()

        # Navigate to Admin tab
        elem = self.browser.find_element_by_id('menu_admin_viewAdminModule')
        elem.send_keys(Keys.RETURN)

        # Assert we are in the System Users page
        assert "System Users" in self.browser.page_source 

        elem = self.browser.find_element_by_id('searchSystemUser_userName')
        elem.clear()
        elem.send_keys('imaminer')

        elem = self.browser.find_element_by_id('searchBtn')
        elem.send_keys(Keys.RETURN)

        
if __name__ == "__main__":
    unittest.main()

    # def test_page_title(self):
    #     self.browser.get('http://www.my.utep.edu')
    #     self.assertIn('MY UTEP', self.browser.title)

    # def test_main_links(self):
    #     self.browser.get('http://www.my.utep.edu')
    #     link_tags = self.browser.find_elements_by_xpath("//a")
    #     link_urls = []

    #     for link in link_tags:
    #         link_urls.append(link.get_attribute('href'))

    #     for link in link_urls:
    #         print("Fetching " + link)
            
    #         t0 = time.time()
    #         self.browser.get(link)
    #         t1 = time.time()

    #         print("Link took {0} seconds to load. \n".format(t1 - t0))

    #     print("Amount of links tested: {0}".format(len(link_urls)))




# class FirefoxTestCase(unittest.TestCase):
    
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         self.addCleanup(self.browser.quit)

    