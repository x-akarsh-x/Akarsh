*** Settings ***
Documentation    Example To Test Library
Library             SeleniumLibrary
Library             ../Library/TimeStamp.py

*** Keywords ***
Print Amazon Title And Timestamp
            open browser        https://www.amazon.in           chrome
            ${time}             TimeStamp.get_TimeStamp
            log to console      ${time}

*** Test Cases ***
Print
        Print Amazon Title And Timestamp