from selenium import webdriver

driver = webdriver.Chrome()

#save the url to navigate to in a variable
url = "http://automationpractice.com/"

#Navighate to the url
driver.get(url)

# Define function to verify that an element exists.
# Pass two parameters in (how to look for element, what xpath should be)

def element_exists(locator_attribute, locator_text):
    """
        Description: finds an element and returns true or false if element is found or not found
    """

    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if locator_attribute not in possible_locators:
        raise BaseException("The locator attribute is not in the approved attributes: &s" % possible_locators)

    # try to find the element

    try: #Try to find element and if found return True
        driver.find_element(locator_attribute, locator_text)
        return True
    except: # If can't find it, return False
        return False

# Function that will Fail if the element does not exist

def assert_element_exists(locator_attribute, locator_text):
    """

    :param locator_attribute:
    :param locator_text:
    :return:
    """

#If element exists returns a false, execute below function

    if not element_exists(locator_attribute, locator_text):
        raise AssertionError("The requested element with '%s' of '%s' does not exist" % (locator_attribute, locator_text))

    return

#Define function to check if the element is visible on the page. Pass the element itself to it.

def elemnet_visible(element):
    """

    :param element:
    :return:
    """

    if element.is_displayed():
        return True
    else:
        return False

# Requires that you find the element in a different step and then pass that element to the fuinction
    def assert_element_visible(element):
        """

        :param element:
        :return:
        """

        if not element_visible(element):
            raise AssertionError("The requested element is not dipslayed")

#Do not have to find the element before calling this function. Find and assert the element in this function
def find_and_assert_element_visible(locator_type, search_term):
    """

    :param locator_type:
    :param search_term:
    :return:
    """

    element = driver.find_element(locator_type, search_term)

    if not element.is_displayed():
        raise AssertionError("The requested element with '&s' of '&s' does not exist" % (locator_attribute, locator_text))

# Call the functions

# Call assert element exists with locator and text. For SignIn we used find_element_by_class_name("login")

#SignIn exists
assert_element_exists('class name', 'login')


