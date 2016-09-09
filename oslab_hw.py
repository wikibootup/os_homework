import os

from oslab_login import OSLAB_login
from time import sleep
from selenium import webdriver


class OSLAB_HW(OSLAB_login):
    def download_hw1(self, post_url):
        self.browser = self.login()

        # Temporary solution, without implicit, explicit wait
        sleep(3)

        URL = post_url
        self.browser.get(URL)

        files = self.browser.find_element_by_class_name('fileAttached')
        files_ul = files.find_element_by_tag_name('ul')
        files_li = files_ul.find_elements_by_tag_name('li')
        for f in files_li:
            f.find_element_by_tag_name('a')
            f.click()
        print("ok")


hw = OSLAB_HW()
hw.download_hw1()
