from selenium import webdriver
from time import sleep


class Tb:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tinder.com/")
        sleep(5)

    def login(self):
        login_div = t.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]')
        links = login_div.find_elements_by_tag_name('button')
        names = [name.text for name in links if name.text != '']

        if 'LOG IN WITH FACEBOOK' in names:
            close_first = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
            close_first.click()

            login_btn = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            login_btn.click()

            fb_login = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_login.click()

            bw = self.driver.window_handles[0]
            popup = self.driver.switch_to.window(self.driver.window_handles[1])

            em = self.driver.find_element_by_xpath('//*[@id="email"]')
            em.send_keys('username')

            pasd = self.driver.find_element_by_xpath('//*[@id="pass"]')
            pasd.send_keys('password')

            clickln = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
            clickln.click()

            self.driver.switch_to.window(bw)

        else:
            self.driver.close()

        sleep(3)

        accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept.click()

        sleep(3)

        allow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow.click()

        enablel = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enablel.click()

        sleep(3)

        try:
            nothan = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
            nothan.click()

        except:
            pass

    def popupcl(self):
        popupcl = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popupcl.click()


t = Tb()
t.login()

like = t.driver.find_element_by_xpath(
    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')

while True:
    sleep(1)
    try:
        like.click()
    except Exception:
        try:
            t.popupcl()
        except Exception:
            pass