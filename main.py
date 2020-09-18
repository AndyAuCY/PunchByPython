import datetime
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('headless')
browser = webdriver.Chrome(options = option)
curTime = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
#yourname = input('输入你的账号：')
#yourpassword = input('输入你的密码：')
#yourlocation = input('输入你的所在地：')
#yourtemp = input('输入你的体温：')
#账号+密码+所在地+体温
with open('info.txt', 'r', encoding='utf-8') as file:
    info = file.readline()
yourname = info.split('+')[0]
yourpassword = info.split('+')[1]
yourlocation = info.split('+')[2] + curTime
yourtemp = info.split('+')[3].split('\n')
try:
    browser.get("http://eswis.gdpu.edu.cn//login.aspx")
except Exception as e:
    print('无法打开网页，请看看连接网络了吗')
    browser.close()
    exit()
#browser.minimize_window()
#定位到账号输入框
username = browser.find_element_by_id('log_username')
password = browser.find_element_by_id('log_password')

try:
    username.send_keys(yourname)
    print('账号已经成功输入')
except Exception as e:
    print('账号输入失败')
    browser.close()
    exit()

try:
    password.send_keys(yourpassword)
    print('密码已经成功输入')
except Exception as e:
    print('密码输入失败')
    browser.close()
    exit()

logon = browser.find_element_by_id('logon')
try:
    logon.click()
    print('登录成功')
except Exception as e:
    print('登录失败')
    browser.close()
    exit()

dailyIssue = browser.find_element_by_link_text('日常管理')
try:
    dailyIssue.click()
    print('点击进入日常管理')
except Exception as e:
    print('无法进入日常管理')
    browser.close()
    exit()

punch = browser.find_element_by_link_text('健康打卡')
try:
    punch.click()
    print('点击进入健康打卡')
except Exception as e:
    print('无法进入健康打卡')
    browser.close()
    exit()

fillInInfo = browser.find_element_by_id('ctl00_cph_right_ok_submit')
try:
    fillInInfo.click()
    print('点击开始填报信息')
except Exception as e:
    print('无法填报信息')
    browser.close()
    exit()

chooseYes = browser.find_element_by_id('ctl00_cph_right_e_atschool_0')
try:
    chooseYes.click()
    print('点击在校')
except Exception as e:
    print('无法点击在校')
    browser.close()
    exit()


location = browser.find_element_by_id('ctl00_cph_right_e_location')
try:
    location.send_keys(yourlocation)
    print('成功输入所在地')
except Exception as e:
    print('无法输入所在地')
    browser.close()
    exit()

symptom = browser.find_element_by_id('ctl00_cph_right_e_observation_0')
try:
    symptom.click()
    print('选择无症状')
except Exception as e:
    print('无法选择无症状')
    browser.close()
    exit()

health = browser.find_element_by_id('ctl00_cph_right_e_health_0')
try:
    health.click()
    print('选择无不适')
except Exception as e:
    print('无法选择无不适')
    browser.close()
    exit()

temperature = browser.find_element_by_id('ctl00_cph_right_e_temp')
try:
    temperature.send_keys(yourtemp)
    print('填写体温')
except Exception as e:
    print('无法填写体温')
    browser.close()
    exit()

submitInfo = browser.find_element_by_id('ctl00_cph_right_e_submit')
try:
    submitInfo.click()
    print('打卡')
except Exception as e:
    print('无法打卡')
    browser.close()
    exit()

#处理对话框
alert = browser.switch_to.alert
print(alert.text)
log = open("log.txt", "a", encoding='utf-8')
log.write(yourname + ' ' + alert.text + ' ' + curTime + '\n')
log.close()
alert.accept()

browser.close()
print('打卡完毕，关闭浏览器')