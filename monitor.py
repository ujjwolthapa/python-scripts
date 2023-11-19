from selenium import webdriver
import subprocess
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

password = "passw0rd"
username = "admin"
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)
driver.get("http://10.13.194.140")
driver.maximize_window()
# using id and name
    # driver.find_element("id","username").send_keys(username)
    # driver.find_element("id","password").send_keys(password)
    # driver.find_element("name","submit").click()
# using xpath
driver.find_element("xpath","/html/body/div/div[1]/div/div/div/div/div[2]/form/fieldset/div[2]/div/input").send_keys(username)
driver.find_element("xpath","//*[@id='password']").send_keys(password)
driver.find_element("xpath", "//*[@id='submit']").click()


