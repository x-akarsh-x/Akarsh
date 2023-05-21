*** Settings ***
Documentation    All The Keywords Related to MakeMyTrip Is Here
Library         SeleniumLibrary
Resource        ../Configuration/env_makemytrip.robot
Resource        PageElements/addresses_makemytrip.robot

*** Keywords ***
I Navigate To MakeTrip
        open browser        ${url}          ${browser}
        maximize browser window

I Remove The Ads
        wait until element is visible       ${ad.frame}
        select frame    ${ad.frame}
        click element   ${close.button}
        wait until element is enabled       ${2nd.close.button}
        click element   ${2nd.close.button}

I Go To Train Section
        click element       ${trains}

I Search for Trains
        [Arguments]    ${depart_city}    ${arrive_city}
        wait until element is visible   ${from}
        click element       ${from}
        wait until element is enabled       //input[@placeholder='From']
        input text          //input[@placeholder='From']          ${depart.city}
        wait until element is enabled   ${suggest.depart.city}
        click element       ${suggest.depart.city}
        wait until element is enabled       //input[@placeholder='To']
        input text          //input[@placeholder='To']          ${arrive.city}
        wait until element is enabled   ${suggest.depart.city}
        click element       ${suggest.depart.city}
        click element       ${date}
        click element       ${class}
        click element       ${search}