# utils/constants.py

class TestData:
    # --- Credentials ---
    VALID_USER = "standard_user"
    LOCKED_USER = "locked_out_user"
    WRONG_USER = "wrong_user"
    VALID_PASS = "secret_sauce"
    WRONG_PASS = "wrong_pass"

    # --- Error Messages ---
    ERROR_REQUIRED_USER = "Epic sadface: Username is required"
    ERROR_REQUIRED_PASS = "Epic sadface: Password is required"
    ERROR_LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."
    ERROR_WRONG_DATA = "Epic sadface: Username and password do not match any user in this service"

    # --- Inventory Items ---
    BACKPACK = "Sauce Labs Backpack"
    ONESIE = "Sauce Labs Onesie"
    SHIRT_RED = "Test.allTheThings() T-Shirt (Red)"
    
    # --- Sorting Options ---
    SORT_LOW_TO_HIGH = "Price (low to high)"
    SORT_HIGH_TO_LOW = "Price (high to low)"
    SORT_A_TO_Z = "Name (A to Z)"
    SORT_Z_TO_A = "Name (Z to A)"

    # --- Parametrization List for Login ---
    INVALID_LOGIN_DATA = [
        (VALID_USER, WRONG_PASS, ERROR_WRONG_DATA),
        (WRONG_USER, VALID_PASS, ERROR_WRONG_DATA),
        (WRONG_USER, WRONG_PASS, ERROR_WRONG_DATA),
        ("", "", ERROR_REQUIRED_USER),
        ("", VALID_PASS, ERROR_REQUIRED_USER),
        (VALID_USER, "", ERROR_REQUIRED_PASS)
    ]

    # --- Checkout flow data ---
    FIRST_NAME = "John"
    LAST_NAME =  "Doe"
    POSTAL_CODE = "11200"

    CHECKOUT_PAGE_TITLE = "Checkout: Complete!"
    CHECKOUT_COMPLETE_MESSAGE = "Thank you for your order!"