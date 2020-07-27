from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.emiratesholidays.com/sa_en/")
    driver.maximize_window()
    driver.implicitly_wait(5)

# HOME PAGE

    # cookies
    try:
        driver.find_element_by_xpath("//button[contains(text(),'Accept and continue browsing')]").click()
    except:
        pass

    # Destination
    driver.find_element_by_xpath("//input[@placeholder='Enter a destination or hotel name']").send_keys('Mal')
    driver.find_element_by_xpath("//div[@class ='search-unit-field destination']//li[2]").click()

    # Departure airport
    try:
        Select(driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/airport-multi-select-unified[1]/div[1]/select[1]")).select_by_index(3)
    except:
        pass

    # Date from
    driver.find_element_by_xpath("//input[@placeholder = 'Check-In']").click()
    driver.find_element_by_xpath("//a[contains(text(),'31')]").click()

    # Occupancy
    driver.find_element_by_xpath("//input[@class ='input-occupancy']").click()
    Select(driver.find_element_by_xpath("//select[@ng-model='room.Adults']")).select_by_value("number:1")       # Number of adults

    driver.find_element_by_xpath("//button[contains(@class,'button secondary')]").click()       #Button Done

    time.sleep(3)
    # Search button
    driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()

    # Cabin First
    # Select(driver.find_element_by_xpath("//body/div/div[@class='site-content-min-width']/div/div[@class='content-wrapper zero-padding overflow']/div[@class='search-unit-bar']/div[@class='search-unit-container']/div[@class='search-panel search-panel-unified inline-cabin holidays']/div[@class='search-unit-field cabin']/select[1]")).select_by_value("number:4")

    time.sleep(15)


#SEARCH RESULTS PAGE

    #Select Hotel
    driver.find_element_by_xpath("//li[1]//div[1]//div[4]//div[1]//div[2]//a[1]").click()

    time.sleep(10)


#HOTEL PAGE

    #Select Room
    driver.find_element_by_xpath("//table[1]//tbody[1]//tr[1]//td[3]//div[1]//a[1]").click()

    time.sleep(10)


# OPTIONS PAGE

    # Select Room
    try:
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[3]/cross-sell-transfers[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[6]/td[1]/label[1]/div[1]").click()
    except:
        pass

    driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[1]/label[1]/div[1]").click()
    driver.find_element_by_xpath("//input[contains(@value,'Continue to next step')]").click()

    time.sleep(10)


#BOOKING PAGE

    # Contact Details
    Select(driver.find_element_by_xpath("//div[@class='form-field-cell fields']//select[@name='title']")).select_by_index(1)        #Title
    driver.find_element_by_xpath("//div[@class='form-field-cell fields']//input[@placeholder='First Name']").send_keys('Mila')      #First Name
    driver.find_element_by_xpath("//div[@class='form-field-cell fields']//input[@placeholder='Last Name']").send_keys('Smith')        #Last Name
    driver.find_element_by_xpath("//input[@placeholder='Phone Number']").send_keys('96541259687')       #Phone Number
    driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys('ohornovych@travelrepublic.co.uk')      #Email
    driver.find_element_by_xpath("//input[@placeholder='Address']").send_keys('Second')     #Address
    driver.find_element_by_xpath("//input[@placeholder='City/Town']").send_keys('Racoon')       #City
    driver.find_element_by_xpath("//input[@placeholder='Post Code']").send_keys('AAAA')     #Post code

    # Room
    # Select(driver.find_element_by_xpath("//div[@class='contacts-fields']//select[@name='title']")).select_by_index(1)        #Title
    # driver.find_element_by_xpath("//div[@class='contacts-fields']//input[@placeholder='First Name']").send_keys('Milaa')        #First Name
    # driver.find_element_by_xpath("//div[@class='contacts-fields']//input[@placeholder='Last Name']").send_keys('Smithh')     #Last Name
    Select(driver.find_element_by_xpath("//select[@name='day']")).select_by_index(1)        #Day
    Select(driver.find_element_by_xpath("//select[@name='month']")).select_by_index(1)        #Month
    Select(driver.find_element_by_xpath("//select[@name='year']")).select_by_index(40)        #Year

    #Payment
    Select(driver.find_element_by_xpath("//select[@name='paymentType']")).select_by_value("number:113")        # Payment Type

    # Step to iframe
    driver.switch_to.frame("pciFrame_cc")
    driver.find_element_by_xpath("//input[@placeholder='Card Number']").send_keys('4111111111111111')       #Card Number
    driver.switch_to.default_content()

    Select(driver.find_element_by_xpath("//select[@name='expiryMonth']")).select_by_index(1)        # expiryMonth
    Select(driver.find_element_by_xpath("//select[@name='expiryYear']")).select_by_index(3)        # expiryYear

    # Step to iframe
    driver.switch_to.frame("pciFrame_cvv")
    driver.find_element_by_xpath("//input[@placeholder='Security Code']").send_keys('123')       # Security Code
    driver.switch_to.default_content()

    # # Book now
    # driver.find_element_by_xpath("//button[contains(text(),'Book Now')]").click()       # Book now


    time.sleep(50)

    driver.close()

if __name__ == '__main__':
    main()
