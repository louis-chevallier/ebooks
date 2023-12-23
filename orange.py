import smtplib, os
from email.message import EmailMessage
from random import randrange
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import selenium
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

import time
import numpy as np

#wd = browser = webdriver.Firefox(executable_path=    GeckoDriverManager().install())
EKO()
import sys
import time
import cherrypy

import PIL
from PIL import Image

"""

url = "https://espaceclientpro.orange.fr"
url = "https://dro.orange.fr/authentification?TARGET=https://dro.orange.fr/detrompeur/B2B%3FcodeContexte%3DOPUS"
EKOX(url)
browser = driver.get(url)
EKOX(driver.title)
html_source = driver.page_source
with open("html.html", "w") as fd : fd.write(html_source)
elem = None

def screen() :
    p = '/tmp/screenie.png'
    driver.save_screenshot(p)
    im = cv2.imread(p)
    return im

if True :
    EKOT("Logging in...")
    identif = "/html/body/main/div[3]/div/div/div[2]/div[2]/form/div[2]"
    identif = '//*[@id="username"]'
    user = 'cabinetmedicalmelesse@orange.fr'

    EKOI(screen(), sz=600)

    accepter = '//*[@id="didomi-notice-agree-button"]'
    elem = driver.find_element(By.XPATH, accepter)
    assert(elem is not None)
    if elem is not None :
        # accepter les cookies
        elem.click()
    EKO()
    driver.implicitly_wait(5)
    EKO()
    EKOI(screen(), sz=600)    
    elem = driver.find_element(By.XPATH, identif)
    assert(elem is not None)    
    elem.send_keys(user)
    EKOI(screen(), sz=600)     
    suivant = '//*[@id="submit-button"]'
    EKOX(elem)
    elem = driver.find_element(By.XPATH, suivant)
    assert(elem is not None)
    EKOX(elem)
    elem.click()
    driver.implicitly_wait(15)
    time.sleep(5)
    EKOI(screen(), sz=600)

    pwdinput ='/html/body/div[4]/div/div[1]/div/div[1]/form/div[2]/div/div/input'
    #pwdinput = '//*[@id="password"]'
    
    elem = driver.find_element(By.XPATH, pwdinput)
    EKOI(screen(), sz=600)
    assert(elem is not None)
    mdp = 'Chenes2023*'
    elem.send_keys(mdp)
    EKOI(screen(), sz=600)

    sidentifier = '//*[@id="btnSubmit"]'
    elem = driver.find_element(By.XPATH, sidentifier)
    assert(elem is not None)
    elem.click()
    driver.implicitly_wait(5)
    EKOI(screen(), sz=600)

    driver.close()
"""

# https://www.zenrows.com/blog/selenium-avoid-bot-detection
# https://piprogramming.org/articles/How-to-make-Selenium-undetectable-and-stealth--7-Ways-to-hide-your-Bot-Automation-from-Detection-0000000017.html

#WebElement m = driver.findElement (By.xpath ("//*[contains(text(),'Get started ')]"));

debugging = True #False

no_christine = "0685848778"
no_secretariat = "0973017826"

# Initializing a list with two Useragents 
useragentarray = [ 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", 
]


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
        
        url = "https://espaceclientpro.orange.fr"
        self.url = "https://dro.orange.fr/authentification?TARGET=https://dro.orange.fr/detrompeur/B2B%3FcodeContexte%3DOPUS"

        test_page = "http://localhost/www_hd1/robot_test/example.html"
        EKO()
        browser_test = self.driver.get(test_page)
        #EKOX( self.driver.page_source)        
        EKOX(self.driver.find_element(By.ID, "log").text)
        EKO()
        #self.mail("coucou")
        #1/0
        browser = self.driver.get(self.url)        
        EKOX(self.driver.title)
        html_source = self.driver.page_source
        #with open("html.html", "w") as fd : fd.write(html_source)

        EKOX(hash(html_source))
                
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
        #EKON(x, txt)
        for i in range(50) :
            #EKOX(i)
            #EKOI(self.screen(), sz=800)            
            try :
                #self.driver.implicitly_wait(waitms/1000)                
                elem = self.driver.find_element(By.XPATH, x)
                #EKOX(elem)
                assert(elem is not None)
                elem.send_keys(txt)
                #EKOX(elem.text)
                #EKOX(elem.get_attribute("value"))
                #EKOI(self.screen(), sz=800)
                #EKON(txt, elem.get_attribute("value"))
                if elem.get_attribute("value") == txt :
                    #EKOT("######################## text %s entered in %s " % (txt, x))
                    break
            except Exception as e:
                pass
            time.sleep(0.2)
        #EKOI(self.screen(), sz=800) 
        #EKOX(elem is not None and  elem.get_attribute("value") == txt)
        assert(elem is not None and  elem.get_attribute("value") == txt)
        #EKO()
        return x
    
    def found(self, x) :
        try :
            elem = self.driver.find_element(By.XPATH, x)
            return elem
        except Exception as e  :
            return None

        
    def click(self, x, absentOK=False, waitms=0, mode=By.XPATH) :
        #EKOX(x)
        try :
            self.driver.implicitly_wait(waitms/1000)
            elem = self.driver.find_element(mode, x)
                    
        except Exception as e  :
            elem = None
            #EKON(absentOK)
            assert(absentOK)
            pass
        
        if elem is None :
            #EKOT("%s pas trouvé " % x)
            assert(absentOK)
            #EKOT("OK")
            return str(x) + " pas trouvé mais ok"
        else :
            assert(elem is not None)
            #EKOX(elem.text)
            #EKOT("#################### clicking %s " % elem.text)
            elem.click()
            #EKOT("clicked")
            return str(x) + " clicked"
        
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
        #EKON(S, K, ws)
        for sec in range(int(S)) :
            #EKOX(sec)
            #EKOI(self.screen(), sz=800)
            for _ in range(int(K)) :
                for ie, e in enumerate(l) :
                    if self.found(e) :
                        #EKOX(e)
                        return e
                    time.sleep(d)
        return None
        
    def login(self) :
        EKOT(" ############################# Logging in...")

        browser = self.driver.get(self.url)
        identif = "/html/body/main/div[3]/div/div/div[2]/div[2]/form/div[2]"
        identif = '//*[@id="username"]'
        user = 'cabinetmedicalmelesse@orange.fr'
        EKOI(self.screen(), sz=800)

        accepter = '//*[@id="didomi-notice-agree-button"]'
        self.click(accepter, absentOK=True)
        EKOI(self.screen(), sz=800)
        sidentifier = '//*[@id="btnSubmit"]'
        #self.waittextin(sidentifier, "S'identifier")
        we = self.wait_one([identif])
        EKOX(we)
        self.enter(identif, user)
        EKO()


        #time.sleep(5)
        EKOI(self.screen(), sz=800)  

            
        resteridentifie = '//*[@id="btnSubmit"]'
        try :
            suivant = '//*[@id="submit-button"]'
            self.click(suivant)
            EKOI(self.screen(), sz=800)
            pwdinput ='//*[@id="password"]'
            #time.sleep(2)
            fwo = self.wait_one([pwdinput, resteridentifie])
            EKOX(fwo)
            
            if self.found(pwdinput)  :
                EKOT("######################### entrée mot de passe")
                mdp = 'Chenes2023*'
                self.enter(pwdinput, mdp)
                EKOI(self.screen(), sz=800)            
                self.click(sidentifier)
                EKOI(self.screen(), sz=800)

                
                #time.sleep(5)
                EKOI(self.screen(), sz=800)  

                
                EKO()
            
            else : 
                EKO()
                self.click(resteridentifie)
        except Exception as e :
            assert(False)
        EKO()
        decouvrirplustard = '/html/body/div[4]/div/div[2]/div[2]/div[3]/div/div/div/a'
        ce = self.click(decouvrirplustard, absentOK=True)
        EKOX(ce)
        EKOT("########################## logged in!!")
        EKOI(self.screen(), sz=800)                    

    def find(self, mode, target) :
        try :
            e = self.driver.find_element(mode, target)
        except :
            e = None
        return e

        
    def check(self) :
        EKO()
        self.login()
        EKO()
        EKOI(self.screen(), sz=800)                    
        monnumero = "/html/body/mikado-root/mikado-logged-in-root/div/main/ng-component/mikado-homepage/div/div[1]/div[1]/div[2]/mikado-lines-summary/div[2]/mikado-group-item/div/div[2]/ul/li/mikado-common-lines-summary/div/a/div/div/span"

        #EKOX(self.find(By.LINK_TEXT, "Renvoi d'appel"))
        #EKOX(self.find(By.CLASS_NAME, "o-link-arrow mk-o-link"))        
        #EKOX(self.find(By.XPATH, "//*[@mikadokeyboardnavlink]"))

        #EKOX(self.find(By.CLASS_NAME, "items-list-item mw-100"))
        
        self.wait_one([monnumero], waitms=20000)
        self.driver.implicitly_wait(5)
        #time.sleep(4)
        EKOX(self.find(By.XPATH, monnumero).text)
        ce = self.click(monnumero, waitms=1000)
        EKOX(ce)
        EKOI(self.screen(), sz=800)                            
        gerermaligne = "/html/body/mikado-root/mikado-logged-in-root/div/main/ng-component/mikado-line-page/mikado-landline/div/div[1]/mikado-tab-bar/nav/ul/li[2]/button"

        we = self.wait_one([gerermaligne])
        EKOX(we)
        EKOI(self.screen(), sz=800)  
        EKOX(self.find(By.XPATH, "//*[@title='Afficher l'onglet Gérer votre ligne Fixe']"))

        renvoyer = "//*[@title='Renvoyer vos appels vers un numéro de votre choix']"
        self.wait_one([gerermaligne])        
        EKOX(self.find(By.XPATH, renvoyer))
        EKOX(self.find(By.XPATH, gerermaligne))

        
        ce = self.click(gerermaligne, waitms=1000)
        EKOX(ce)
        EKOI(self.screen(), sz=800)



        parametrer = "//*[@title='Paramétrer le Renvoi d'appel']"
        we = self.wait_one([parametrer])
        EKOX(we)
        EKOX( self.find(By.XPATH, parametrer).text)
        ce = self.click(parametrer, waitms=1000)
        EKOX(ce)
        

        annuler_renvoi = "//*[@title='Annuler le renvoi d\'appel en cours et remettre le paramétrage par défaut']"
        we = self.wait_one([annuler_renvoi])
        EKOX(we)
        EKOX( self.find(By.XPATH, parametrer).text)


        


        
        notification = "//*[@class='notification-content']"
        we = self.wait_one([notification], waitms=1000000)
        EKOX(we)
        EKOX( self.find(By.XPATH, notification).text)


        """
        active = "/html/body/mikado-root/mikado-logged-in-root/div/main/ng-component/mikado-line-page/mikado-landline/div/div[2]/mikado-landline-manage-tab/div/div[1]/ul/li[1]/a/div/div/div/small"
        EKOI(self.screen(), sz=800)          
        EKOX(self.driver.find_element(By.XPATH, active).text)
        EKOI(self.screen(), sz=800)          
        EKOX(self.driver.find_element(By.XPATH, active).text)
        EKOI(self.screen(), sz=800)          
        EKOX(self.driver.find_element(By.XPATH, active).text)
        EKOI(self.screen(), sz=800)
        EKOX(self.find(By.XPATH, "//*[@title='Paramétrer le Renvoi d'appel']"))
        return active, self.driver.find_element(By.XPATH, active).text
        """
        
    

    def renvoi(self) :
        self.login()
        e, _ = self.check()
        self.click(e, waitms=1000)
        time.sleep(4); EKOI(self.screen(), sz=800)              
        renvoyer = "//*[@title='Renvoyer tous les appels']"
        EKOX(self.find(By.XPATH, renvoyer))
        self.click(renvoyer)
        time.sleep(4); EKOI(self.screen(), sz=800)      
        cenumero = "//*[@title='Renvoyer tous les appels vers ce numéro']"
        self.click(cenumero)
        time.sleep(4); EKOI(self.screen(), sz=800)
        lenumero = "//*[@title='Indiquer le numéro vers lequel vous désirez renvoyer tous vos appels']"
        self.enter(lenumero, no_christine)
        validernumero = "//*[@title='Cliquer pour valider le paramétrage de votre renvoi d'appel']"
        self.click(validernumero)
        time.sleep(4); EKOI(self.screen(), sz=800)
        EKO()
        #renvoi = '/html/body/mikado-root/mikado-logged-in-root/div/main/ng-component/mikado-homepage/div/div[1]/div/div[2]/mikado-lines-summary/div[2]/mikado-group-item/div/div[2]/div/div/span/a/strong'
        #self.click(renvoi)
        #EKO()
        #self.click('/html/body/mikado-root/mikado-logged-in-root/div/main/ng-component/mikado-call-forwarding-page/div/div/div/mikado-entrypoint/div[1]/div/a')

class DummyRobotWeb(object):
    def __init__(self) :
        pass
    
    @cherrypy.expose
    def index(self):
        return "Hello World!"



class RobotWeb(object):
    def __init__(self, robot) :
        self.robot = robot
        self.no = 0
        
    @cherrypy.expose
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def check(self) :
        self.no += 1
        EKO()
        try :
            r = self.robot.check()
            EKO()
        except Exception as e :
            r = str(e)
        return str(self.no) + "\n" + r

    @cherrypy.expose
    def renvoi(self) :
        self.robot.renvoi()

    @cherrypy.expose
    def secretariat_actif(self) :
        reponse = self.check()
        reponses =  [ "Activé vers le 09 73 01 78 26" ]
        docheck(reponse in reponses)
        return reponses.index(reponse) == 0


    
if __name__ == '__main__':
    EKO()
    robot = Robot()
    if True :
        r = robot.check()
        EKOX(r)

    if False : 
        cherrypy.server.socket_host = '192.168.1.5' # la tour , '0.0.0.0' # put it here 
        cherrypy.quickstart(RobotWeb(robot))
        robot.driver.close()
        EKO()
    #cherrypy.server.socket_host = '192.168.1.32' #'0.0.0.0' # put it here 


