from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import config

class UnfollowBot():

    def __init__(self, username, password):
        self.opts = Options()
        self.opts.add_argument("user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36")
        self.url = "https://www.instagram.com/"
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='./chromedriver', options=self.opts)
        self.driver.set_window_size(375, 667)
        self.follower_lists = []
    
    def login(self):
        driver = self.driver
        driver.get(self.url+"accounts/login/")
        time.sleep(1)
        username_input = driver.find_element_by_xpath("//input[@name='username']")
        username_input.send_keys(self.username)
        password_input = driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)

    def fetchFollowers(self):
        driver = self.driver
        driver.get(self.url+self.username)
        follower_link = driver.find_element_by_xpath("//a[@href='/"+self.username+"/followers/']")
        follower_link.click()
        time.sleep(20)
        follower_lists = driver.find_elements_by_css_selector('a.FPmhX.notranslate._0imsa')
        for item in follower_lists:
            self.follower_lists.append(item.get_attribute('title'))
        
    
    def unfollow(self):
        driver = self.driver
        driver.get(self.url+self.username)
        following = driver.find_element_by_xpath("//a[@href='/"+self.username+"/following/']")
        following.click()
        time.sleep(20)
        following_lists = driver.find_elements_by_class_name("uu6c_")
        # for item in following_lists:
        #     print(item)

        # WIP: 
        #   1.  list all following
        #   2.  iterate the list
        #   3.  compare following to follower if not exist, unfollow

        print(len(following_lists))
        print(len(self.follower_lists))

app = UnfollowBot(config.USERNAME, config.PASSWORD)
app.login()
app.fetchFollowers()
app.unfollow()