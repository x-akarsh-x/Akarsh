*** Settings ***
Documentation    All The Address Of The Locators Used In Resources Of MakeMyTrip

*** Variables ***
${ad.frame}                 //iframe[@title = 'notification-frame-b8a69a19']
${close.button}             //a[@class = 'close']
${2nd.close.button}         //span[contains(@class, 'close_grey')]
${trains}                   //li[@class='menu_Trains']
${from}                     //input[@id='fromCity']
${suggest.depart.city}      (//ul[@role='listbox']//li)[1]
${to}                       //input[@id='toCity']
${search}                   //a[text()='Search']