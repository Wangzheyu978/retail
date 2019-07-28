import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import csv
class doubanwlwz_spider():
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.set_headless()
        driver = webdriver.Chrome(options=opt)
        driver=webdriver.Chrome()
        self.getInfo(driver)
    def getInfo(self,driver):
        driver = driver
        driver.get("http://www.douban.com/")
        driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        bottom1 = driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
        bottom1.click()
        input1 = driver.find_element_by_xpath('//*[@id="username"]')
        input1.clear()
        input1.send_keys("18164570365")
        input2 = driver.find_element_by_xpath('//*[@id="password"]')
        input2.clear()
        input2.send_keys("bradt783560445")
        bottom = driver.find_element_by_class_name('account-form-field-submit')
        bottom.click()
        time.sleep(1)
        search_window = driver.current_window_handle
        count=0
        data = []
        for page in range(30):
            driver.get('https://movie.douban.com/subject/26100958/comments?start={}'.format(page*20))
            for x in range(1, 21):
                try:
                    time1 = driver.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[3]'.format(str(x))).get_attribute('title')
                except:
                    time1 = driver.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[2]'.format(str(x))).get_attribute('title')
            for i in range(1,21):
                name=driver.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/a'.format(str(i))).text
                comment = driver.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/p/span'.format(str(i))).text
                time1= driver.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[{}]'.format(str(i),2|3)).get_attribute('title')
                agreepeople = driver.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[1]/span'.format(str(i))).text
                rate = driver.find_element_by_xpath( '//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[2]'.format(str(i))).get_attribute('title')
                rating = driver.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[2]'.format(str(i))).get_attribute('class')
                userInfo = driver.find_element_by_xpath( '//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/a'.format(str(i))).get_attribute('href')
                print(name,comment,agreepeople,rate,rating,time1)
                driver.get(userInfo)
                try:
                    location = driver.find_element_by_xpath('//*[@id="profile"]/div/div[2]/div[1]/div/a').text
                except :
                    location= '找不到'
                count=count+1
                print(location)
                data.append([name,agreepeople,rate,rating,time1,comment,location])
                df=pd.DataFrame(data,columns=['name','agreepeople','rate','rating','time','comment','location'])
                df.to_csv('C:/Users/csh/Desktop/douban/aaa.csv', encoding='utf_8_sig')

                driver.back()



AAA=doubanwlwz_spider()