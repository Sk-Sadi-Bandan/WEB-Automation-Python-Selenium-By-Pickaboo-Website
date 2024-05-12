Feature: pikaboo testing

    # Scenario: Login with valid user and password
    #     Given go to site
    #     When Click on login page
    #     Then Input login detials
    #     When Click on login button
    #     Then Click on Smartphone option
    #     When Click on Redmi Note 13 phone

    Scenario: Validate Availability search
        Given go to site
        When Input search
        And Click on submit icon
        And click on product option
        And Click on color option
        And Click on Add to Cart button
        And Click on shopping icon

    Scenario: Validate Availability slider
        Given go to site
        Then slider found
        Then Click on slider

    Scenario: Validate Availability and Functionality of Support Button
        Given go to site
        Then Verify the presence of the Support button
        Then Click on the Support button
