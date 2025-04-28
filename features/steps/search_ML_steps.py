from behave import given, when, then
from selenium import webdriver
from pages.search_ProductML import SearchPage
from pages.pageToSearch import SearchPage as results

@given ('The page of iphone 13')
def step_given_intu_login(context):
    context.driver = webdriver.Chrome() 
    context.driver.get('https://www.mercadolibre.com.co/')
    context.search_ProductML = SearchPage(context.driver)
    context.result_page = results(context.driver)

@when('I search iphone 13 on the bar')
def step_when_intu_login(context):
    context.search_ProductML.search('iphone 13') 

@then ('I should see the options that mercado libre has')
def step_then_ML(context):
    assert 'iphone 13' in context.result_page.isElementPresent().lower()