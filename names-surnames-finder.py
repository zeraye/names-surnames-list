from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path='D:\SeleniumDrivers\chromedriver.exe')  # it can be different path
driver.get('') # website name eg. 'https://namecensus.com/data/1000.html'
driver.implicitly_wait(20)

file = open('', 'r+')  # file name eg. 'surnames-list.txt'


def read(x):
    i = 2
    while i < x:
        i += 1
        file.write(driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[2]/div[2]/div/table/tbody/tr[{}]/td[1]'.format(i)).text + '\n')


file.close()
