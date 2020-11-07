import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

##TimeDelays
timeDelay0 = random.randrange(1, 3)
timeDelay = random.randrange(3, 6)
timeDelay2 = random.randrange(6, 10)
timeDelayBig = random.randrange(50, 70)

##email
eml = "dkacausevic95@gmail.com"

##passwort insta und google
psdg = "Oberbeul_95"


##driver initiallisieren
##Chrome Driver starten und Benachrichtigungen deaktivieren
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
time.sleep(timeDelay)


###Defs
def log_in():
    ##Anmelden
    ##Seite laden und Fenster vergrößern
    driver.maximize_window()
    driver.get("https://rivalregions.com")
    time.sleep(timeDelay)

    ##Google-Anmeldung
    driver.find_element_by_xpath("//*[@id='sa_add2']/div[2]/a[2]/div").click()
    time.sleep(timeDelay)

    ##Email
    driver.find_element_by_id("identifierId").send_keys(eml, Keys.ENTER)
    time.sleep(timeDelay2)

    ##Passwort
    driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(psdg, Keys.ENTER)
    time.sleep(timeDelay2)

def radio_checken():
    while True:
        ##Verschmutzung aufrufen
        driver.get("https://rivalregions.com/#listed/nuclear")
        time.sleep(timeDelay)
        driver.refresh()
        time.sleep(timeDelay2)

        try:
            #Auf Region gehen
            driver.find_element_by_xpath("//*[@id='list_tbody']/tr[1]/td[2]").click()
            time.sleep(timeDelay2)

            #Säubern
            try:

                avdo = driver.find_element_by_xpath("//*[@id='header_slide_inner']/div[3]/div[1]/div[4]").get_attribute("innerHTML")
                avdo2 = driver.find_element_by_xpath("//*[@id='header_slide_inner']/div[3]/div[1]/div[5]").get_attribute("innerHTML")
                avdo3 = driver.find_element_by_xpath("//*[@id='header_slide_inner']/div[3]/div[1]/div[3]").get_attribute("innerHTML")
               
                if avdo == "Antirad":
                    driver.find_element_by_xpath("//*[@id='header_slide_inner']/div[3]/div[1]/div[4]").click()
                    time.sleep(timeDelay)   
                elif avdo2 == "Antirad":
                    driver.find_element_by_xpath("//*[@id='header_slide_inner']/div[3]/div[1]/div[5]").click()
                    time.sleep(timeDelay)  
                elif avdo3 == "Antirad":
                    driver.find_element_by_xpath("//*[@id='header_slide_inner']/div[3]/div[1]/div[3]").click()
                    time.sleep(timeDelay)  
                else:
                    driver.find_element_by_xpath("//*[@id='header_slide_inner']/div[3]/div[1]/div[6]").click()
                    time.sleep(timeDelay)

            except:
                print("Nee")  

        except:

            time.sleep(60)
    
    





###Ausführung

log_in()
radio_checken()
#while True:
    










