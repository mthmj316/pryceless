'''
Created on 29.06.2020

@author: mthoma
'''
NO_PRECIDING_SIBLING_EXPECTED_RESULT = (
    '/**\n'
    '* Test if the siblings of the tag with id==login_password.\n'
    '* expected preceding sibling id==\n'
    '* expected following sibling id==login_name\n'
    '* Hint if id==<empty> the corresponding sibling doesn\'t exists.\n'
    '*/\n'
    '@ParameterizedTest\n'
    '@CsvSource({",preceding-sibling::*[1]", "login_name,following-sibling::*[1]"})\n'
    'public void testLoginPasswordSibling(final String expectedSiblingId, final String xpath){\n'
    '\tfinal WebElement tag = DRIVER.findElement(By.id("login_password"));\n'
    '\tif(expectedSiblingId == null) {\n'
    '\t\tassertThrows(org.openqa.selenium.NoSuchElementException.class, () -> tag.findElement(By.xpath(xpath)));\n'     
    '\t} else {\n'
    '\t\tfinal WebElement sibling = tag.findElement(By.xpath(xpath));\n'
    '\t\tassertEquals(expectedSiblingId, sibling.getAttribute("id"),"wrong sibling");\n'
    '\t}\n'
    '}'
    )

NO_FOLLOWING_SIBLING_EXPECTED_RESULT = (
    '/**\n'
    '* Test if the siblings of the tag with id==login_password.\n'
    '* expected preceding sibling id==login_error_message\n'
    '* expected following sibling id==\n'
    '* Hint if id==<empty> the corresponding sibling doesn\'t exists.\n'
    '*/\n'
    '@ParameterizedTest\n'
    '@CsvSource({"login_error_message,preceding-sibling::*[1]", ",following-sibling::*[1]"})\n'
    'public void testLoginPasswordSibling(final String expectedSiblingId, final String xpath){\n'
    '\tfinal WebElement tag = DRIVER.findElement(By.id("login_password"));\n'
    '\tif(expectedSiblingId == null) {\n'
    '\t\tassertThrows(org.openqa.selenium.NoSuchElementException.class, () -> tag.findElement(By.xpath(xpath)));\n'     
    '\t} else {\n'
    '\t\tfinal WebElement sibling = tag.findElement(By.xpath(xpath));\n'
    '\t\tassertEquals(expectedSiblingId, sibling.getAttribute("id"),"wrong sibling");\n'
    '\t}\n'
    '}'
    )
NO_SIBLING_EXPECTED_RESULT = (
    '/**\n'
    '* Test if the siblings of the tag with id==login_password.\n'
    '* expected preceding sibling id==\n'
    '* expected following sibling id==\n'
    '* Hint if id==<empty> the corresponding sibling doesn\'t exists.\n'
    '*/\n'
    '@ParameterizedTest\n'
    '@CsvSource({",preceding-sibling::*[1]", ",following-sibling::*[1]"})\n'
    'public void testLoginPasswordSibling(final String expectedSiblingId, final String xpath){\n'
    '\tfinal WebElement tag = DRIVER.findElement(By.id("login_password"));\n'
    '\tif(expectedSiblingId == null) {\n'
    '\t\tassertThrows(org.openqa.selenium.NoSuchElementException.class, () -> tag.findElement(By.xpath(xpath)));\n'     
    '\t} else {\n'
    '\t\tfinal WebElement sibling = tag.findElement(By.xpath(xpath));\n'
    '\t\tassertEquals(expectedSiblingId, sibling.getAttribute("id"),"wrong sibling");\n'
    '\t}\n'
    '}'
    )

SIBLING_EXPECTED_RESULT = (
    '/**\n'
    '* Test if the siblings of the tag with id==login_password.\n'
    '* expected preceding sibling id==login_error_message\n'
    '* expected following sibling id==login_name\n'
    '* Hint if id==<empty> the corresponding sibling doesn\'t exists.\n'
    '*/\n'
    '@ParameterizedTest\n'
    '@CsvSource({"login_error_message,preceding-sibling::*[1]", "login_name,following-sibling::*[1]"})\n'
    'public void testLoginPasswordSibling(final String expectedSiblingId, final String xpath){\n'
    '\tfinal WebElement tag = DRIVER.findElement(By.id("login_password"));\n'
    '\tif(expectedSiblingId == null) {\n'
    '\t\tassertThrows(org.openqa.selenium.NoSuchElementException.class, () -> tag.findElement(By.xpath(xpath)));\n'     
    '\t} else {\n'
    '\t\tfinal WebElement sibling = tag.findElement(By.xpath(xpath));\n'
    '\t\tassertEquals(expectedSiblingId, sibling.getAttribute("id"),"wrong sibling");\n'
    '\t}\n'
    '}'
    )
