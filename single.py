from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://music.163.com/#/user/home?id=50359783')

browser.quit()