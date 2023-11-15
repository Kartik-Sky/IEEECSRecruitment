import pyautogui
from PIL import ImageGrab 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def moveit(key):
    pyautogui.keyDown(key)
    return

def birdieorcactus(data):
    
    for i in range(300, 390):
        for j in range(410, 563):
            if data[i, j] < 100:
                moveit("down")
                time.sleep(0.1)
                pyautogui.keyUp("down")
                return

    for i in range(310, 400):
        for j in range(563, 670):
            if data[i, j] < 100:
                moveit("up")
                time.sleep(0.2)
                pyautogui.keyDown("down")
                pyautogui.keyUp("down")
                return
    return


options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Skywalker2')
options.add_argument('--force-ligh-mode')
driver = webdriver.Chrome(options=options)
cookies = driver.get_cookies()
try:
    driver.get("chrome://dino")
    
except WebDriverException:
    pass
driver.maximize_window()
time.sleep(1)
moveit("up")
time.sleep(1)
moveit('up')

while True:
    image = ImageGrab.grab().convert('L')  
    data = image.load()
    birdieorcactus(data)
    
