from selenium import webdriver
driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver')
driver.get('https://www.facebook.com/')
username_input = '//*[@id="email"]'
password_input = '//*[@id="pass"]'
login_submit = '//*[@id="u_0_b"]'
with open('passwordfile.txt', 'r') as myfile:
    password = myfile.read().replace('\n', '')
driver.find_element_by_xpath(username_input).send_keys("7550249736")
driver.find_element_by_xpath(password_input).send_keys(password)
driver.find_element_by_xpath(login_submit).click()

