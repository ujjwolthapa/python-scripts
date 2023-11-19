from selenium import webdriver
import subprocess
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

password_process = subprocess.run('pass default',shell=True,capture_output=True,text=True)
password = password_process.stdout.strip()
username = "ujjwolthapa0@gmail.com"
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)
driver.get("https://facebook.com")
driver.maximize_window()
driver.find_element("id","email").send_keys(username)
driver.find_element("id","pass").send_keys(password)
driver.find_element("name","login").click()


