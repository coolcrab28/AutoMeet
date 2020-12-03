import ntplib
from time import ctime

ntp_client = ntplib.NTPClient()
response = ntp_client.request('pool.ntp.org')
h = (ctime(response.tx_time).split()[3][:2])
m = (ctime(response.tx_time).split()[3][3:5])
s = (ctime(response.tx_time).split()[3][6:8])

time_table = {
  'Mon' : {1:'https://meet.google.com/gcz-dqvd-dqk',
           2:'https://meet.google.com/wue-ebpx-bby',
           3:'',
           4:''}
}

if (int(h)>=8) and (int(h)<=13):
  from selenium import webdriver
  import time 
  import getpass
  import os
  path = os.getcwd()

  options = webdriver.ChromeOptions()
  options.add_argument("--disable-infobars")
  options.add_experimental_option("prefs", { \
      "profile.default_content_setting_values.media_stream_mic": 2, 
      "profile.default_content_setting_values.media_stream_camera": 2,
      "profile.default_content_setting_values.geolocation": 2, 
      "profile.default_content_setting_values.notifications": 2 
    })

  username = input("Enter username/email: ")
  password = getpass.getpass(prompt='Password: ', stream=None)
  class_time = int(input("Enter class time in minutes: "))
  link = 'https://meet.google.com/the-meet-link'
  # class_time *= 60
  browser = webdriver.Chrome(options=options)
  def main(*b):
    login(username,password)
  def login(username, password):
      file = f"""file:///{path}/end.html"""
      browser.get(('https://stackoverflow.com/'))
      browser.find_element_by_xpath("/html/body/header/div/ol[2]/li[2]/a[2]").click()
      browser.find_element_by_xpath("//*[@id=\"openid-buttons\"]/button[1]").click()
      browser.find_element_by_id("identifierId").send_keys(username)
      browser.find_element_by_id("identifierNext").click()
      time.sleep(3)
      browser.find_element_by_name("password").send_keys(password)
      browser.find_element_by_id("passwordNext").click()
      time.sleep(5)
      join(link)
      
  def join(link):
      browser.get(link)
      time.sleep(3)
      browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()
      time.sleep(1)
      browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span').click()
      time.sleep(class_time)
      browser.get(file)
  login(username,password)

else:
  def main(*a):
    print("School closed! It is currently "+str(h)+':'+str(m)+':'+str(s))
