from selenium import webdriver
import time 
from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(U'go to site')
def open_picabo(context):
    context.driver= webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.pickaboo.com/")
    context.driver.find_element(By.ID,'rcc-confirm-button').click()
    time.sleep(1)


# sinario 1
    
@when(U'Click on login page')
def step_impl2(context):
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()
    time.sleep(5)

@Then(U'Input login detials')
def step_impl1(context):
    context.driver.find_element(By.XPATH, '//*[@placeholder="Mobile Number/Email"]').send_keys('01749653931')
    context.driver.find_element(By.XPATH, '//*[@placeholder="Password"]').send_keys('sadisadi')
    time.sleep(5)

@when(U'Click on login button')
def valid_Login_Attempt(context):
   context.driver.find_element(By.XPATH, "//button[contains(@class, 'custom-buttons')]").click()
   time.sleep(5)

@Then(U'Click on Smartphone option')
def Smartphone(context):
   context.driver.find_element(By.XPATH, "//div[normalize-space()='Smartphones']").click()
   time.sleep(5)

@when(U'Click on Redmi Note 13 phone')
def Smartphone(context):
   context.driver.find_element(By.XPATH, "//body/div[@id='__next']/main/section[3]/section[1]/div[1]/div[1]/div[2]/div[1]").click()
   time.sleep(5)

# sinario 2
@when('Input search')
def search(context):
    context.driver.find_element(By.CLASS_NAME, "searchInput ").send_keys('Laptop')
    time.sleep(5)

@when('Click on submit icon')
def submit(context):
    context.driver.find_element(By.XPATH, "//img[@alt='search img']").submit()
    time.sleep(5)

@when('click on product option')
def product(context):
    context.driver.find_element(By.XPATH, "//*[@id='__next']/main/section/div[2]/div/div[2]/div[2]/div[5]").click()
    time.sleep(5)

@when('Click on color option')
def Color(context):
    context.driver.find_element(By.XPATH, "//div[@class='color-box-selected']//center//img").click()
    time.sleep(5)

@when('Click on Add to Cart button')
def AddToCart(context):
    context.driver.find_element(By.XPATH, "//span[normalize-space()='ADD TO CART']").click()
    time.sleep(5)

@when('Click on shopping icon')
def AddToCart(context):
    context.driver.find_element(By.XPATH, "//img[@alt='cart']").click()
    time.sleep(5)




# sinario 3
@then('slider found')
def Slider(context):
    context.driver.find_element(By.XPATH, "//div[@class='slick-slide slick-active slick-current']//div//div[@class='home-banner_slider_single a-tag']")
    assert True

@then('Click on slider')
def Slider2(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='3']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[normalize-space()='3']").click()
    time.sleep(1)

# sinario 5
@then('Verify the presence of the Support button')
def Support1(context):
    context.driver.find_element(By.XPATH, "//section[@class='LogoHomeSlider__StyledSlider-sc-1drhg8f-0 kXbXVo logo-slider pt-10 pb-20 shadow-bottom']//div[@class='swiper-container swiper-container-initialized swiper-container-horizontal']")
    assert True

@then('Click on the Support button')
def Support2(context):
    context.driver.find_element(By.XPATH, "//img[@src='https://storage.googleapis.com/pickaboo-prod/media/dcastalia_hybridslider/image/EMI.png']").click()
    time.sleep(7)

# sinario 6

