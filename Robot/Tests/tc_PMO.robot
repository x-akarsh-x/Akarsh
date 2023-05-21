*** Settings ***
Documentation    This Is The Feature File Of PMO
Resource            ../Resources/PMO/resource_PMO.robot

*** Variables ***
${lok.sabha}        https://sansad.in/ls

*** Test Cases ***
User Print Former Speaker Of Lok Sabha
        Given I Navigate To PMO Website
        Then I Go Through All Links Of Our Government
        Then I Switch To ${lok.sabha} Window
        When I Go To Former Speakers
        Then I Print All The Former Speakers