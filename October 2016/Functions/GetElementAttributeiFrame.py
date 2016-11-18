from selenium import webdriver

driver = webdriver.Chrome()

#save the url to navigate to in a variable
url = "http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_textarea"

#Navighate to the url
driver.get(url)

# Switching focus to the iframe (sort of a seperate window). Will be covered in later sections.
my_frame = driver.find_element('id', 'iframeResult')
driver.switch_to.frame(my_frame)

box = driver.find_element_by_tag_name('textarea')

box_text = box.get_attribute('value')
print box_test

