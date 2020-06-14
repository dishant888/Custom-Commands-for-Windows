from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyperclip
from credentials import email,password
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys

options = Options()
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
browser = ''

def invite(invitationLink):

    name = ' '.join(sys.argv[1:])
    to = f"//span[@title='{name}']"
    # open new tab
    browser.execute_script("window.open('');")

    # switch control to new tab
    browser.switch_to.window(browser.window_handles[1])

    # open web whatsapp in new tab
    browser.get('http://web.whatsapp.com/')

    # wait untill whatsapp loads and find group or person
    WebDriverWait(browser, 200).until(EC.presence_of_element_located((By.XPATH, to)))
    group = browser.find_elements_by_xpath(to)[0].click()

    # search message text box and press enter key to send msg
    message = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    message.send_keys(invitationLink + Keys.ENTER)
    sleep(2)
    # switch back too google meet
    browser.switch_to.window(browser.window_handles[0])

def start():

    global browser
    browser = webdriver.Chrome(executable_path='C:\\Users\\user\\downloads\\chromedriver_win32\\chromedriver.exe',options=options)
	# Open url
    browser.get('https://meet.google.com/new')

    # check if redirected to google login page
    if "https://accounts.google.com/signin/" in browser.current_url:
        # login into google account
        browser.find_elements_by_xpath("//input[@name='identifier']")[0].send_keys(email)
        browser.find_elements_by_xpath("//div[@id='identifierNext']")[0].click()
        WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
        passwordInput = browser.find_elements_by_xpath("//input[@name='password']")[0]
        passwordInput.send_keys(password)
        browser.find_elements_by_xpath("//div[@id='passwordNext']")[0].click()


    # create and join meeting
    WebDriverWait(browser, 20).until(
    	EC.visibility_of_element_located((By.XPATH, "//span[text()='Join now']"))
	)
    browser.find_element_by_xpath("//span[text()='Join now']").click()

    # copy meeting url
    WebDriverWait(browser, 15).until(
    	EC.visibility_of_element_located((By.XPATH, "//span[text()='Copy joining info']"))
	)
    browser.find_element_by_xpath("//span[text()='Copy joining info']").click()
    # meeting url saved into variable(meetingUrl)
    meetingUrl = pyperclip.paste()

    # send invitation to whatsapp
    invite(meetingUrl)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        start()
    else:
        print('Invalid arguments received')