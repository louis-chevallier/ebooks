import os, tqdm
import requests
import urllib.request
import re
from bs4 import BeautifulSoup
import multiprocessing
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from utillc import *
from selenium.webdriver.firefox.service import Service as ServiceF
from selenium.webdriver.chrome.service import Service as ServiceC
import PIL
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import numpy as np
#wd = browser = webdriver.Firefox(executable_path=    GeckoDriverManager().install())
EKO()
import sys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import cherrypy

import PIL
from PIL import Image

class P:

    def __init__(self) :
        options = FirefoxOptions()
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # changing user-agent because etoro detects the automated browser somehow
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/86.0.4240.183 Safari/537.36")
        EKO()


        s = ServiceC('/usr/bin/chromedriver')
        bot = self.driver = webdriver.Chrome(service=s, options=options)
        #self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)
        #self.driver = webdriver.Firefox(options=options)
        #self.driver.get("https://pythonbasics.org")
        #wd = webdriver.Firefox(service=service, options=options)
        EKO()
        
        self.url = "https://podcloud.fr/podcast/franck-ferrand-raconte"
        
        browser = self.driver.get(self.url)        
        EKOX(self.driver.title)
        html_source = self.driver.page_source
        #with open("html.html", "w") as fd : fd.write(html_source)

        EKOX(hash(html_source))
        #EKOX(dir(bot))

        for i in range(9999) :
            EKOX(i)
            elem = bot.find_element(By.XPATH, "//*[text()='Afficher plus']")
            EKOX(elem)
            try :
                elem.click()
                time.sleep(2)
            except Exception as ex:
                EKOX(ex)
                EKOT("tout déplié")
                break
        xpath = "/html/body/section[2]/section/div[2]/section/div[2]/div[2]/div"
        elems = bot.find_elements(By.XPATH, xpath)
        EKOX(len(list(elems)))
        for ie, e in tqdm.tqdm(enumerate(list(elems))) :
            aa = bot.find_element(By.XPATH, xpath + "[%d]/a" % (ie+1))
            title = aa.text
            EKOX(title)
            try : 
                bb = bot.find_element(By.XPATH, xpath + "[%d]/span[2]/div/ul/li[4]/a" % (ie+1))
                ref = bb.get_attribute("href")
                filename = title.replace("/", "_") + ".mp3"
                if not os.path.exists(filename) :
                    doc = requests.get(ref)
                    with open(filename, 'wb') as f:
                        f.write(doc.content)
                    EKOT("%s written" % filename)
                else :
                    EKOT("%s already there" % filename)                    
            except Exception as ex :
                EKOX(ex)
                pass

                
        bot.close()  # shuts down the bot


if __name__ == '__main__':
    p = P()


