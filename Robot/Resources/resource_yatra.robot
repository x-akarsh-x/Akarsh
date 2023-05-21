*** Settings ***
Documentation       Step Defination Of Keywords Of Feature File "Yatra" Is Here
Library    SeleniumLibrary
Resource    ../Configuration/${ENV}_yatra.robot

*** Keywords ***
Given I Navigate To Yatra Website
        open browser            ${url}       ${broswer}
        maximize browser window
        log title
        click button            //button[text()='Ok,I Agree']

When I Select The Trip
        wait until keyword succeeds     10s     2s      click element           //a[@title='Round Trip']
        wait until element is enabled       //input[@id='BE_flight_origin_city']    10s
        click element           //input[@id='BE_flight_origin_city']
        clear element text      //input[@id='BE_flight_origin_city']
        input text              //input[@id='BE_flight_origin_city']           ${depart.city}
        press keys               //input[@id='BE_flight_origin_city']       RETURN
        click element           //input[@id='BE_flight_arrival_city']
        clear element text      //input[@id='BE_flight_arrival_city']
        input text              //input[@id='BE_flight_arrival_city']           ${arrive.city}
        press keys               //input[@id='BE_flight_arrival_city']       RETURN

Then I Select The Date
        wait until element is visible       //input[@id='BE_flight_arrival_date']       10s
        click element           //input[@id='BE_flight_arrival_date']
        wait until element is enabled       ${date}
        click element           ${date}

And I Select The Class And Search
        click element           //span[contains(@class, 'flight_passengerBox')]
        click element           (//span[contains(@class, 'ddSpinnerPlus')])[1]
        click element           //span[text()='Economy']
        capture page screenshot
        click element           //input[@value = 'Search Flights']