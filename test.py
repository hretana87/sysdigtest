from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox() #if a PATH has not been set up, it can be added as a parameter.
driver.get("https://app.sysdigcloud.com/")

try:
    #Since the id is dynamically generated, the best apprach is to use XPATH methodf
    #Wait up to 5 seconds for input field to be rendered
    username = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,".//input[@name='username']")))
    username.send_keys('hretana@test.com')
    
    # Just to show a pause between events
    time.sleep(2)
    
    #Wait up to 5 seconds for input field to be rendered
    password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,".//input[@name='password']")))
    password.send_keys('test_password')
    
    # Just to show a pause between events
    time.sleep(2)
    driver.find_element(By.XPATH,".//button[@data-id='submit-login']").click()
    
    #Check for error message presence
    message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,'login__error-display')))
    
    print("Test case successfully passed!!!")
    driver.close()
    
except:
        print("Something went wrong with the test...")
        driver.close()

