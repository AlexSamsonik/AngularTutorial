*** Settings ***
Documentation  Login Functionality
Library  SeleniumLibrary

*** Variables ***
${pesel}            86000015000
${id_input_pesel}   id:inputPesel
${id_user_pesel}    id:userPesel

*** Test Cases ***
Verify Successful Login to AngularApp
    [documentation]  This test case verifies that user is able to successfully Login to AngularApp
    [tags]  Smoke
    Open Browser  http://localhost:4200/  Chrome
    Wait Until Element Is Visible  ${id_input_pesel}
    Input Text  id:inputPesel  ${pesel}
    Click Element  id:buttonLogin
    Element Should Be Visible  ${id_user_pesel}
    Element Text Should Be  ${id_user_pesel}   ${pesel}
    Close Browser

*** Keywords ***
