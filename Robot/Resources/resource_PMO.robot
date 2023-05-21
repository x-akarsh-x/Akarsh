*** Settings ***
Documentation    All Step Definition Keywords Of Feature File 'PMO' Is Here
Library         SeleniumLibrary
Resource        PageElements/homepage_PMO.robot
Resource        PageElements/lok.sabha_PMO.robot
Resource        ../Configuration/env_PMO.robot

*** Keywords ***
I Navigate To PMO Website
            open browser        ${url}          ${browser}
            maximize browser window
            log title

I Go Through All Links Of Our Government
            wait until page contains element        ${government.links}         10s
            ${number.of.links}      get element count       ${government.links}
            FOR     ${i}    IN RANGE        1       ${number.of.links}+1
                click element       (${government.links})[${i}]
            END

I Switch To ${lok.sabha} Window
            ${handles}      get window handles
            FOR     ${handle}   IN      @{handles}
                switch window       ${handle}
                ${page.url}       get location
                IF      '${page.url}' == '${lok.sabha}'     BREAK
            END

I Go To Former Speakers
            wait until element is visible       ${current.speaker}          10s
            click element       ${current.speaker}
            wait until element is visible       ${former}           10s
            click button        ${former}

I Print All The Former Speakers
             wait until page contains element       ${speakers}
             ${speakers.list}       get webelements     ${speakers}
             FOR    ${speaker}    IN    @{speakers.list}
                ${text}    get text    ${speaker}
                log    ${text}
                log to console    ${text}
             END