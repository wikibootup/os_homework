import os

from oslab_login import OSLAB_login
from time import sleep
from selenium import webdriver


class OSLAB_hw(OSLAB_login):
    def __init__(self):
       super(OSLAB_hw, self).__init__()
       self.hw1_post_url = os.environ.get('HW1_POST_URL')

    def download_hw1(self):
        self.browser = self.login()

        # Temporary solution, without implicit, explicit wait
        sleep(3)

        self.browser.get(self.hw1_post_url)

        files = self.browser.find_element_by_class_name('fileAttached')
        files_ul = files.find_element_by_tag_name('ul')
        files_li = files_ul.find_elements_by_tag_name('li')
        for f in files_li:
            f.find_element_by_tag_name('a')
            f.click()
        print("ok")


hw = OSLAB_hw()
hw.download_hw1()
