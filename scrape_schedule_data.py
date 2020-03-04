from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


def setup_driver():
    driver = webdriver.Firefox()
    driver.get("https://quiz2020.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=7215&cmid=8&page=2")

    return driver


def login(driver):
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    username.send_keys(<USERNAME>)
    password.send_keys(<PASSWORD>)
    driver.find_element_by_id("loginbtn").click()
    
    
def setup_soup(driver):
    content = driver.page_source
    return BeautifulSoup(content, "lxml")


def get_login_token(soup):
    login = soup.findAll("input", {"name" : "logintoken"})
    return login[0]["value"]


def get_info(soup):
    info = []
    trs = soup.findAll("tr", {"class" : ""})
    for person in trs[1:-3]:
        item = person.text.split("\n")
        _id = item[1]
        time = get_minutes(item[3])
        duration = item[4]
        person_info = (_id, time, duration)
        info.append(person_info)
    return info


def get_minutes(time):
    time = time.split(":")
    return 60 * int(time[0]) + int(time[1])
        

def main():
    driver = setup_driver()
    login(driver)
    soup = setup_soup(driver)
    info = get_info(soup)
    

main()