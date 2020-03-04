from selenium import webdriver
driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver')
driver.get('https://academicscc.vit.ac.in/student/stud_login.asp')
username_input = '/html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input'
password_input = '/html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input'
login_submit = '/html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[6]/td/input[1]'
captcha_link = ''
with open('passwordfile.txt', 'r') as myfile:
    password = myfile.read().replace('\n', '')
driver.find_element_by_xpath(username_input).send_keys("7550249736")
driver.find_element_by_xpath(password_input).send_keys(password)
driver.find_element_by_xpath(login_submit).click()

events = '//*[@id="navItem_2344061033"]/a/div'
birthdays = '//*[@id="u_fetchstream_6_1"]/div[3]/a/span'
driver.find_element_by_xpath(events).click()
driver.find_element_by_xpath(birthdays).click()
