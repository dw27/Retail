from selenium import webdriver

driver = webdriver.Firefox()

#save the url to navigate to in a variable
url = "http://automationpractice.com/"

#Navighate to the url
driver.get(url)

# Look for 70% off sale add on the top of the page

sale_add = driver.find_element_by_class_name('img-responsive')

# Extract the text and store it in a variable

sale_add_text = sale_add.text

print '======================================================'
print sale_add_text
print '======================================================'

# Can also pass locator_type, locator_text. This one assumes we already found the element
# Verify that the field is NOT empty

def assert_element_not_empty(element):
    """

    :return:
    """

    element_text = element.text

    if sale_add_text == '':
        raise AssertionError('The element does not contain any text')
    else:
        print "The element does contain: %s " % element_text


# Function  that verifies that the element contains a specific text. Ex: Sale 70%

def assert_element_contains_text(element, text):
    """

    :param element:
    :param text:
    :return:
    """

    element_text = element.text

    if text in sale_add_text:
        print('The element contains the text: % s' % element_text)
    else:
        raise AssertionError("The element does not contain: %s" % element_text)

    return

# Call function and check for Sale 70%
assert_element_contains_text('sale_add_text', 'Sale 70%')