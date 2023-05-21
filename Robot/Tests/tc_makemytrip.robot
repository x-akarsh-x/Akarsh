*** Settings ***
Documentation    All Test Cases Related To MakeMyTrip Are Here
Resource         ../Resources/makemytrip/resource_makemytrip.robot

*** Variables ***
${depart.city}      Delhi
${arrive.city}      Mumbai

*** Test Cases ***
User Search For Trains
    Given I Navigate To MakeTrip
    Then I Remove The Ads
    Then I Go To Train Section
    And I Search for Trains     ${depart.city}      ${arrive.city}