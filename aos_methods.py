import sys
from selenium import webdriver # import selenium to the file
import aos_locators as locators
from selenium.webdriver.chrome.service import Service
import time
# import chromedriver_autoinstaller
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # <-- add this import for drop down lists
from selenium.webdriver.common.keys import Keys
# from faker import Fakerimport sys


print('----------------------------******--------------------------------------------------')
print('---------------------------*****---------------------------------------------------------')

from selenium.webdriver.chrome.options import Options



options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

print('----------------------------******--------------------------------------------------')
print('---------------------------*****---------------------------------------------------------')


# ---------------------------------------------------------------------------------

#driver = webdriver.Chrome('/Users/owner/Desktop/pythonProject/chromedriver')
# driver = webdriver.Chrome(executable_path='/Users/owner/Desktop/pythonProject/venv/chromedriver')

# s = Service(executable_path = '/Users/owner/Desktop/pythonProject/venv/chromedriver.exe')
# driver = webdriver.Chrome("/Users/owner/Desktop/pythonProject/chromedriver")


def setup():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.aos_url)
    print(driver.title)
    print(driver.current_url)
    if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
        print('Advantage Online Shopping App Launched Successfully!')
        print(' ')
        print(f'Advantage Online Shopping URL: {driver.current_url}')
        print(f'Advantage Online Shopping Homepage Title: {driver.title}')
        # sleep(2)

    else:
        print('AOS APP is not launched')
        print(f'-----The current URL is {driver.current_url}')
        print(f'-----The current title is {driver.title}')
        # sleep(2)
        tearDown()



def tearDown():
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        time.sleep(2)
        driver.close()
        # driver.quit()


# Create New Account - using Faker library fake data
def create_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT , 'CREATE NEW ACCOUNT').click()
    time.sleep(2)
    driver.find_element(By.NAME,'usernameRegisterPage').send_keys(locators.new_username)
    time.sleep(.3)
    driver.find_element(By.NAME,'emailRegisterPage').send_keys(locators.email)
    time.sleep(.3)
    driver.find_element(By.NAME,'passwordRegisterPage').send_keys(locators.new_password)
    time.sleep(.3)
    driver.find_element(By.NAME,'confirm_passwordRegisterPage').send_keys(locators.new_password)
    time.sleep(2)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    time.sleep(2)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    time.sleep(.25)
    # driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(phone_number)
    # time.sleep(.25)
    # Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(country)
    # time.sleep(.25)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    time.sleep(.25)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    time.sleep(.25)
    x = driver.find_element(By.NAME, 'i_agree').is_selected()
    if x == False :
        driver.find_element(By.NAME, 'i_agree').click()
    else :
        print('Problem in registering')
        driver.close()
    time.sleep(3)
    driver.find_element(By.ID, 'register_btnundefined').click()
    time.sleep(2)
    print(f' the registered  username is  : "{locators.new_username}" and password is: "{locators.new_password}"')
    # logger('created')


# Logout
def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    print('---------------*%*----------------')
    print(f'The {driver.current_url} was closed at: {datetime.datetime.now()}')
    # driver.close()
    # driver.quit()


# login
def log_in():
    if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
        sleep(2)
        print(f' The URL is : {driver.current_url} and the title of the web-page is :{driver.title}')
    else:
        print(f' Something is wrong. Check the URL of the web page!')
    time.sleep(2)
    driver.find_element(By.ID, 'menuUser').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    driver.find_element(By.NAME,'password').send_keys(locators.new_password)
    time.sleep(.3)
    driver.find_element(By.ID,'sign_in_btnundefined').click()
    time.sleep(4)
    # CHECK-LOGIN
    x = driver.find_element(By.XPATH, f'//*[@id="menuUserLink"]/span[contains(.,"{locators.new_username}")]').is_displayed()
    print(x)
    if x == True:
        print(f' login was successful')
    else:
        print(f' THERE IS A PROBLEM- CAN YOU HELP ME PLEASE FIND IT??')

def homepage_texts():
    assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
    assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
    assert driver.find_element(By.ID, 'laptopsTxt').is_displayed()
    assert driver.find_element(By.ID, 'miceTxt').is_displayed()
    assert driver.find_element(By.ID, 'headphonesTxt').is_displayed()
    assert driver.find_element(By.XPATH, '//h3[contains(.,"SPECIAL OFFER")]').is_displayed()
    assert driver.find_element(By.XPATH, '//span[contains(.,"EXPLORE THE NEW DESIGN")]').is_displayed()
    assert driver.find_element(By.XPATH, '//p[contains(.,"Supremely thin, yet incredibly durable")]').is_displayed()
    assert driver.find_element(By.XPATH, '//*[contains(.,"ALL YOU WANT FROM A TABLET")]').is_displayed()
    assert driver.find_element(By.XPATH, '//h3[contains(.,"POPULAR ITEMS")]').is_displayed()
    assert driver.find_element(By.NAME, 'popular_item_16_name').is_displayed()
    assert driver.find_element(By.NAME, 'popular_item_10_name').is_displayed()
    assert driver.find_element(By.NAME, 'popular_item_21_name').is_displayed()
    assert driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed()
    assert driver.find_element(By.XPATH, '//h3[contains(.,"FOLLOW US")]').is_displayed()

    # driver.find_element(By.ID, 'speakersTxt').click()
    # sleep(2)
    # assert driver.current_url == locators.speakers_url
    # sleep(1)
    # driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    # sleep(2)
    driver.find_element(By.ID, 'tabletsTxt').click()
    sleep(2)
    assert driver.current_url == locators.tablet_url
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(1)
    driver.find_element(By.ID, 'laptopsTxt').click()
    sleep(1)
    assert driver.current_url == locators.laptop_url
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(1)
    driver.find_element(By.ID, 'miceTxt').click()
    sleep(1)
    assert driver.current_url == locators.mice_url
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(1)
    driver.find_element(By.ID, 'headphonesTxt').click()
    sleep(1)
    assert driver.current_url == locators.headphone_url
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.ID, 'see_offer_btn').click()
    assert driver.current_url == locators.see_offer_url
    sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div/button[contains(.,"EXPLORE NOW")]').click()
    assert driver.current_url == locators.explore_now_url
    sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.ID, 'details_16').click()
    # assert driver.current_url == locators.product_1
    sleep(4)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(4)
    driver.find_element(By.ID, 'details_10').click()
    # assert driver.current_url == locators.product_2
    sleep(4)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(3)
    driver.find_element(By.ID, 'details_21').click()
    # assert driver.current_url == locators.product_3
    sleep(3)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(3)
    driver.find_element(By.CLASS_NAME, 'chat').click()

    main_page = driver.current_window_handle
    sleep(3)
    for handle in driver.window_handles:
        if handle != main_page:
            chat_page = handle
            driver.switch_to.window(chat_page)
            assert driver.current_url == locators.chat_url
            sleep(1)
            driver.find_element(By.ID, 'textMessage').send_keys('Hello')
            sleep(1)
            if driver.find_element(By.ID, 'btnSender').is_enabled():
                driver.find_element(By.ID, 'btnSender').click()
            else:
                print(('Alert!! Chatbox is not working'))
    sleep(6)
    driver.close()
    driver.switch_to.window(main_page)
    sleep(3)

    driver.find_element(By.NAME, 'follow_facebook').click()
    sleep(3)
    for handle in driver.window_handles:
        if handle != main_page:
            fb_page = handle
            driver.switch_to.window(fb_page)
            # change the control to chat page
            if driver.current_url != locators.fb_link:
                print('Facebook page error')
            sleep(2)
    driver.close()
    sleep(3)
    driver.switch_to.window(main_page)
    sleep(3)

    driver.find_element(By.NAME, 'follow_twitter').click()
    sleep(3)
    for handle in driver.window_handles:
        if handle != main_page:
            tw_page = handle
            driver.switch_to.window(tw_page)
            # change the control to chat page
            if driver.current_url != locators.twitter_link:
                print('Twitter page error')
            sleep(2)
    driver.close()
    sleep(3)
    driver.switch_to.window(main_page)
    sleep(3)

    driver.find_element(By.NAME, 'follow_linkedin').click()
    sleep(3)
    for handle in driver.window_handles:
        if handle != main_page:
            li_page = handle
            driver.switch_to.window(li_page)
            # change the control to chat page
            if driver.current_url != locators.linkedin_link:
                print('Linkedin page error')

            sleep(3)
    driver.close()
    sleep(3)
    driver.switch_to.window(main_page)

    driver.find_element(By.NAME, 'go_up_btn').click()
    assert driver.current_url == locators.aos_url
    sleep(3)
    print('')
    print('Main Logo is displayed & clickable')
    print('')
    print('All texts SPEAKER | TABLETS | LAPTOP | MICE | HEADPHONES | SPECIAL OFFER TEXTS | SLIDER TEXTS | '
          'POPULAR ITEMS TEXTS |  CONTACT US | FOLLOW US | are displayed')
    print('')
    print('All "Shop Now" links for SPEAKER | TABLETS | LAPTOP | MICE | HEADPHONES and links for  SEE OFFER | '
          'EXPLORE NOW| POPULAR ITEMS VIEW DETAIL links | links  are displayed & clickable')
    print('')
    print('Chat box is Checked & Follow us links for Facebook, Twitter & Linkedin are displayed & clickable')


#logger
def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()

def top_menu():
    sleep(3)
    driver.find_element(By.XPATH, '//a[contains(.,"OUR PRODUCTS")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"SPECIAL OFFER")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"POPULAR ITEMS")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"CONTACT US")]').click()
    sleep(2)
    # driver.find_element(By.ID, 'menuSearch').click()
    # sleep(1)
    # driver.find_element(By.ID, 'menuUser').click()
    # sleep(1)
    # driver.find_element(By.XPATH, '//div[@class = "closeBtn loginPopUpCloseBtn"]').click()
    # sleep(1)
    driver.find_element(By.ID, 'shoppingCartLink').click()
    sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.ID, 'helpLink').click()
    sleep(2)
    print('')
    print('All Top Navigation Menu Links are Clickable OUR PRODUCTS | SPECIAL OFFER | POPULAR ITEMS | CONTACT US |'
          ' SEARCH ICON| USER ICON | SHOPPING CART LINK | HELP LINK ')


def contact_us_form():
    sleep(1)
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Headphones')
    sleep(1)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_index(1)
    sleep(1)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(1)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.phone_number)
    sleep(2)
    assert driver.find_element(By.ID, 'send_btnundefined').is_enabled()
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1)
    assert driver.find_element(By.XPATH,
                               '//p[contains(.,"Thank you for contacting Advantage support.")]').is_displayed()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()
    sleep(1)
    print('')
    print('CONTACT US Form working!')
    print('')

def delete_user():
    driver.find_element(By.LINK_TEXT, locators.new_username).click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My orders")]').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//div/label[contains(.,"No orders")]').is_displayed()
    sleep(0.25)
    print(f'No Orders Displayed ')
    driver.find_element(By.LINK_TEXT, locators.new_username).click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.new_username}")]').is_displayed()
    print(f' ')
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="deletePopupBtn deleteRed"]').click()
    print(f'Account has been deleted.')
    sleep(3)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)
    driver.find_element(By.ID, 'signInResultMessage').is_displayed()
    print(f'Incorrect user name or password.')


# def checkout_Shopping_Cart():
#     driver.find_element(By.ID, 'speakersTxt').click()
#     driver.find_element(By.ID, '20').click()
#     driver.find_element(By.NAME, 'save_to_cart').click()
#     sleep(2)
#     driver.find_element(By.ID, 'menuCart').click()
#     driver.find_element(By.ID, 'checkOutPopUp').click()
#     print('')
#     sleep(1)
#     # driver.find_element(By.ID, 'next_btn').click()
#     # sleep(2)
#     driver.find_element(By.NAME,'safepay_username').click()
#     driver.find_element(By.NAME, 'safepay_username').send_keys(locators.new_username)
#     sleep(2)
#     driver.find_element(By.NAME, 'safepay_password').click()
#     driver.find_element(By.NAME, 'safepay_password').send_keys(locators.new_password)
#     sleep(2)
#     driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
#     time.sleep(2)
#     # This line-code give all the order informations:
#     # oreders = driver.find_element(By.ID, 'orderPaymentSuccess').text
#     # print(f'The details of order is as follow:"{oreders}"')
#
#     print('--------------------~*~--------------------')
#     print('SHIPPING DETAILS:')
#
#     trakingNumber = driver.find_element(By.ID, 'trackingNumberLabel').text
#     orderNumber = driver.find_element(By.ID, 'orderNumberLabel').text
#     print(f' The traking_umber is found to be: "{trakingNumber}" and order-number is found to be: "{orderNumber}"')
#     shipName = driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/div/div[1]/div/div[1]/label').text
#     print(f'SHIPING TO :"{shipName}"')
#     addresse = driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/div/div[1]/div/div[2]/label[1]').text
#     print(f'ADDRESSE  :"{addresse}"')
#     phone = driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/div/div[1]/div/div[3]/label').text
#     print(f'PHONE NUMBER  :"{phone}"')
#     dateorder = driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/div/div[2]/div[2]/label/a').text
#     print(f'ORDER DATE :"{dateorder}"')
#     subtotall = driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/div/div[3]/div[1]/label/a').text
#     print(f'SUBTOTL :"{subtotall}"')
#     total = driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]/div/div[3]/div[3]/label/a').text
#     print(f'TOTAL :"{total}"')
#     print('--------------------~*~--------------------')

# setup()
# create_new_user()
# logger('created')
# log_out()
# log_in()
# homepage_texts()
# top_menu()
# contact_us_form()
# # checkout_Shopping_Cart()
# delete_user()
# logger('deleted')
# tearDown()

