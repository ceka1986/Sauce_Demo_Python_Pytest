# utils/constants.py

class TestData:
    # --- Credentials ---
    VALID_USER = "standard_user"
    LOCKED_USER = "locked_out_user"
    WRONG_USER = "wrong_user"
    VALID_PASS = "secret_sauce"
    WRONG_PASS = "wrong_pass"

    # --- Error Messages ---
    ERR_MATCH = "Epic sadface: Username and password do not match any user in this service"
    ERR_REQUIRED = "Epic sadface: Username is required"
    ERR_LOCKED = "Epic sadface: Sorry, this user has been locked out"

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
        (VALID_USER, WRONG_PASS, ERR_MATCH),
        (WRONG_USER, VALID_PASS, ERR_MATCH),
        (WRONG_USER, WRONG_PASS, ERR_MATCH),
        ("", "", ERR_REQUIRED)
    ]