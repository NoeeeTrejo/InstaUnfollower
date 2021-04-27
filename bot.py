from selenium import webdriver
from time import sleep
import time
#from utility_methods.utility_methods import *
import urllib.request
import os

class Bot():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(2)


    def search(self, query):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(query)
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div/a").click()
        sleep(2)

    def follow_user(self, user):
        self.search(user)
        sleep(3)
        followButton = self.driver.find_elements_by_css_selector('button')
        followButton = followButton[0]
        followButton.click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div/img").click()
    def unfollow_user(self, user):
        self.search(user)
        sleep(3)
        followButton = self.driver.find_elements_by_css_selector('button')
        followButton = followButton[1]
        followButton.click()
        sleep(3)
        confirmButton = self.driver.find_element_by_xpath('//button[text() = "Unfollow"]')
        confirmButton.click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div/img").click()



    def find_buttons(self, button_text):
        buttons = self.driver.find_elements_by_xpath("//*[text()='{}']".format(button_text))
        return buttons
    
    def spamFollow(self, username, n):
        for i in range(n):
            self.follow_user(username)
            self.unfollow_user(username)
    
    def messageUser(self, username, message):
        self.search(username)
        buttons = self.find_buttons("Message")
        if not buttons: 
            self.follow_user(username)
            sleep(1.5)
            buttons = self.find_buttons("Message")
        buttons[0].click()
        sleep(1)
        text_box = self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        text_box.send_keys(message)
        sleep(0.4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()  

    def messageFileToUser(self, fileName, username):
        self.search(username)
        buttons = self.find_buttons("Message")
        if not buttons: 
            self.follow_user(username)
            sleep(1.5)
            buttons = self.find_buttons("Message")
        buttons[0].click()
        sleep(3)
        text_box = self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        file = open(fileName, "r")
        for line in file:
            sleep(0.2)
            text_box.send_keys(line)
            
    def profile_page(self):
        self.driver.get("https://instagram.com/" + self.username)




def main():
    # This small script goes through followed users and unfollows users
    myBot = Bot("username", "password")
    
    for i in range(28):
        myBot.profile_page()

        #Goes to following
        myBot.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").click()
        sleep(1)
        following_buttons = myBot.find_buttons('Following')
        for button in following_buttons:
            button.click()
            sleep(0.8)
            Unfollow_button = myBot.find_buttons('Unfollow')
            for other_button in Unfollow_button:
                other_button.click()
                sleep(3)
            sleep(0.8)
        button = myBot.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button')
        button.click()
        sleep(5)
            



    


if __name__ == '__main__':
    main()
