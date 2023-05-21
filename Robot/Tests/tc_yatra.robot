*** Settings ***
Documentation    All Test Cases For Ticket Booking In Yatra Is Here
Resource            ../Resources/resource_yatra.robot

*** Test Cases ***
Yatra Ticket Booking
        Given I Navigate To Yatra Website
        When I Select The Trip
        Then I Select The Date
        And I Select The Class And Search