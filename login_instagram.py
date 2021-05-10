from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://www.instagram.com/accounts/login")
    login_credentials = driver.find_elements_by_css_selector("._2hvTZ.pexuQ.zyHYP")
    login_credentials[0].send_keys("ENTER YOUR USERNAME")
    login_credentials[1].send_keys("ENTER YOUR PASSWORD")
    
    click_login = driver.find_element_by_css_selector("._0mzm-.sqdOP.L3NKy").click()
    print ("LOG IN SUCCESS")
except:
    print ("SOMETHING WENT WRONG")
