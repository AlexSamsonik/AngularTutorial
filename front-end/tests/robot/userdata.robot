*** Settings ***
Documentation  UserData Update Functionality
Library    SeleniumLibrary

*** Variables ***
${id_user_pesel}            id:userPesel
${id_user_data_posts}       id:userDataPosts
${id_user_data_likes}       id:userDataLikes
${id_user_data_followers}   id:userDataFollowers

*** Test Cases ***
Verify Successful Update
    [Documentation]  This test case verifies that user data is to successfully updated
    [Tags]  Smoke
    Open Browser  http://localhost:4200/userdata?pesel=86598914789  Firefox
    ${number_of_posts}    Get Text    ${id_user_data_posts}
    ${number_of_likes}    Get Text    ${id_user_data_likes}
    ${number_of_followers}    Get Text    ${id_user_data_followers}
    Click Element  id:buttonUpdate
    Wait Ready State Complete
    Element Text Should Not Be    ${id_user_data_posts}    ${number_of_posts}
    Should Be True    ${number_of_posts}>=0
    Should Be True    ${number_of_posts}<=99
    Element Text Should Not Be    ${id_user_data_likes}    ${number_of_likes}
    Should Be True    ${number_of_likes}>=1000
    Should Be True    ${number_of_likes}<=9999
    Element Text Should Not Be    ${id_user_data_followers}   ${number_of_followers}
    Should Be True    ${number_of_followers}>=100
    Should Be True    ${number_of_followers}<=999
    Close Browser

*** Keywords ***
Wait Ready State Complete
    ${state}   Execute Javascript    return document.readyState
    Should Be Equal As Strings    ${state}    complete
