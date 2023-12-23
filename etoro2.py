import smtplib, os
from email.message import EmailMessage
from random import randrange
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import selenium
from time import sleep
import pandas as pd
from utillc import *
EKOX(selenium.__version__)
usechrome = True

if usechrome :
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options as  Options
    from selenium.webdriver import Chrome as Driver
    #import chromedriver_autoinstaller 
    #chromedriver_autoinstaller.install() 
else :
    from selenium.webdriver.firefox.service import Service
    from selenium.webdriver.firefox.options import Options as Options
    from selenium.webdriver import  Firefox as Driver


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
import time
import cherrypy

import PIL
from PIL import Image

useragentarray = [ 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", 
]

debugging = True #False
trading_timeout = 2
page_load_timeout = 3
class Robot :

    def mail(self, txt) :
        # set your email and password
        # please use App Password
        email_address = "louis.chevallier@gmail.com"
        email_password = os.environ["app_password_for_gmail"]

        # create email
        msg = EmailMessage()
        msg['Subject'] = "secretariat telephonique"
        msg['From'] = "louis.chevallier@gmail.com"
        msg['To'] = "louis.chevallier@gmail.com"
        msg.set_content(txt)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            e = smtp.login(email_address, email_password)
            EKOX(e)
            e = smtp.send_message(msg)
            EKOX(e)
        EKOT("sent")

    def __init__(self) :
        options = Options()

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # changing user-agent because etoro detects the automated browser somehow
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/86.0.4240.183 Safari/537.36")
        EKO()

        if usechrome :
            #s = Service('/usr/bin/chromedriver')
            s = Service('./chromedriver_patched')
            #options.add_argument('--headless=new')
            options.add_argument("--disable-blink-features=AutomationControlled") 
            # Exclude the collection of enable-automation switches 
            options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
            
            # Turn-off userAutomationExtension 
            options.add_experimental_option("useAutomationExtension", False) 
            options.add_argument("window-size=1280,800")
            options.add_argument('--disable-blink-features=AutomationControlled')


            options.add_argument('--window-size=1920,1080')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-setuid-sandbox')
            options.add_argument('--disable-software-rasterizer')
            options.add_argument('--log-level=3')
            options.add_argument('--silent')
            options.add_argument('--useAutomationExtension=false')
            
            self.driver = Driver(service=s, options=options)

            # Changing the property of the navigator value for webdriver to undefined 
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            i = randrange(len(useragentarray))
            self.driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]})
            EKO()
            
        else :
            self.driver = Driver(options=options)            
        #self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)
        #self.driver = webdriver.Firefox(options=options)
        #self.driver.get("https://pythonbasics.org")
        #wd = webdriver.Firefox(service=service, options=options)
        EKO()
        self.email = "clovis-heaulier"
        self.password = os.environ["ETORO_PASSWORD"]

    def login(self) :
        EKOT(" ############################# Logging in...")
        driver = self.driver
        
        browser = self.driver.get("https://www.etoro.com/login")
        EKO()
        # bypassing e-Toros login system by changing user agent. Credits github.com/winterdrive
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'"
        })

        EKOI(self.screen(), sz=800)            

        # writing email and password on the form
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(self.email)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)
        
        # I don't like the xpath selector on this one, I will do it by text
        buttons = driver.find_elements(By.TAG_NAME, 'button')

        EKOI(self.screen(), sz=800)            
        for button in buttons:
            if button.text == 'Sign in':
                button.click()
                break
        sleep(5)
        EKOI(self.screen(), sz=800)

        sleep(120)
        
        

    def screen(self) :
        if debugging :
            p = '/tmp/screenie.png'
            self.driver.save_screenshot(p)
            x = Image.open(p)
            #im = cv2.imread(p)
            im = np.array(x)        
            return im
        else :
            return np.zeros((3,3,3)).astype(np.uint8)

    def enter(self, x, txt, waitms=12000) :
        EKON(x, txt)
        for i in range(50) :
            EKOX(i)
            EKOI(self.screen(), sz=800)            
            try :
                #self.driver.implicitly_wait(waitms/1000)                
                elem = self.driver.find_element(By.XPATH, x)
                EKOX(elem)
                assert(elem is not None)
                elem.send_keys(txt)
                EKOX(elem.text)
                EKOX(elem.get_attribute("value"))
                EKOI(self.screen(), sz=800)
                EKON(txt, elem.get_attribute("value"))
                if elem.get_attribute("value") == txt :
                    EKOT("######################## text %s entered in %s " % (txt, x))
                    break
            except Exception as e:
                pass
            time.sleep(0.2)
        EKOI(self.screen(), sz=800) 
        EKOX(elem is not None and  elem.get_attribute("value") == txt)
        assert(elem is not None and  elem.get_attribute("value") == txt)
        EKO()
        
    def found(self, x) :
        try :
            elem = self.driver.find_element(By.XPATH, x)
            return elem
        except Exception as e  :
            return None

        
    def click(self, x, absentOK=False, waitms=0, mode=By.XPATH) :
        EKOX(x)
        try :
            self.driver.implicitly_wait(waitms/1000)
            elem = self.driver.find_element(mode, x)
                    
        except Exception as e  :
            elem = None
            EKON(e, absentOK)
            assert(absentOK)
            pass
        
        if elem is None :
            EKOT("%s pas trouvé " % x)
            assert(absentOK)
        else :
            assert(elem is not None)
            EKOX(elem.text)
            EKOT("#################### clicking %s " % elem.text)

            elem.click()

    def waittextin(self, x, txt) :
        EKO()
        self.driver.implicitly_wait(5)
        EKO()
        elem = None
        for i in range(10) :
            EKOX(i)
            try :
                elem = self.driver.find_element(By.XPATH, x)
                EKOX(elem.txt)
                if elem.text == txt :
                    break
                else :
                    time.sleep(0.5)                    
            except Exception as e  :
                EKOX(e)
                elem = None
                time.sleep(0.5)
                EKO()
        assert(elem is not None)
        EKOI(self.screen(), sz=800)

    def wait_one(self, l, waitms=10000) :
        d, ws = 0.1, waitms/1000
        K = 1. / d / len(l)
        S = ws / K / len(l) / d
        EKON(S, K, ws)
        for sec in range(int(S)) :
            EKOX(sec)
            EKOI(self.screen(), sz=800)
            for _ in range(int(K)) :
                for ie, e in enumerate(l) :
                    if self.found(e) :
                        EKOX(e)
                        return ie
                    time.sleep(d)
        return -1
        
        

    # function that allows you to switch to virtual portfolio
    def switch_to_virtual(self, driver):
        driver.find_element(By.LINK_TEXT, 'Switch to Virtual').click()
        sleep(self.trading_timeout)
        driver.find_element(By.LINK_TEXT, 'Switch to Virtual Portfolio').click()
        sleep(self.page_load_timeout)
        return driver

    def get_portofolio(self) :
        pass

    
    # function that allows you to switch to real portfolio
    def switch_to_real(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, 'Switch to Real').click()
        sleep(trading_timeout)
        driver.find_element(By.LINK_TEXT, 'Go to Real Portfolio').click()
        sleep(page_load_timeout)
        EKOI(self.screen(), sz=800) 
        return driver

    def find(self, mode, target) :
        try :
            e = self.driver.find_element(mode, target)
        except :
            e = None
        return e

        
    
if __name__ == '__main__':
    EKO()
    robot = Robot()
    robot.login()
    robot.switch_to_real()
    robot.get_portfolio()
    
    #cherrypy.server.socket_host = '192.168.1.32' #'0.0.0.0' # put it here 



