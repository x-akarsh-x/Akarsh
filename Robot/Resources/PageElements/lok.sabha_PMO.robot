*** Settings ***
Documentation    All The Address Of The Locators Used In Resources Of PMO "lok sabha"

*** Variables ***
${current.speaker}          (//p[contains(text(), 'Speaker')])[1]
${former}                   //button[text()='Former']
${speakers}                 //p[@class = 'MuiTypography-root MuiTypography-body1 style_memberName__Srgzp mui-style-sqip12']