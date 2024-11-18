*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password confirmation  pekka123
    Submit Credentials

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  zalazana123
    Set Password confirmation  zalazana123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  jaakko
    Set Password  jaak123
    Set Password confirmation  jaak123
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Set Username  jaakko
    Set Password  jaakkooo
    Set Password confirmation  jaakkooo
    Submit Credentials
    Register Should Fail With Message  Password is invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  jaakko
    Set Password  jaakko123
    Set Password confirmation  jaakko321
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation don't match

Register With Username That Is Already In Use
    Set Username  pekka
    Set Password  pekka123
    Set Password confirmation  jaakko321
    Submit Credentials
    Register Should Fail With Message  Username already exists

*** Keywords ***
Register Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Password confirmation  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page