'''
Created on 29.06.2020

@author: mthoma
'''
JAVA_DOC_TEST_TAG_NAME = '/**\n* Test if the tag with id==%s has the tag name==%s.\n*/'
JAVA_DOC_TEST_PARENT = '/**\n* Test if the tag with id==%s has the parent with the id==%s.\n*/'
JAVA_DOC_TEST_SIBLINGS = ('/**\n'
                          '* Test if the siblings of the tag with id==%s.\n'
                          '* expected preceding sibling id==%s\n'
                          '* expected following sibling id==%s\n'
                          '* Hint if id==<empty> the corresponding sibling doesn\'t exists.\n'
                          '*/'
                          )
JAVA_DOC_TEST_ATTRIBUTES = ('/**\n'
                            '* Test of the attributes for the tag with id==%s\n'
                            '*/'
                            )

JAVA_DOC_TEST_CSS_RULES = ('/**\n'
                            '* Test of the css rules for the tag with id==%s\n'
                            '*/'
                            )

SELENIUM_GET_ATTRIBUTE = '%s.getAttribute("%s")'
SELENIUM_GET_VARIABLE_ATTRIBUTE = '%s.getAttribute(%s)'
SELENIUM_GET_CSS_VALUE = '%s.getCssValue(%s)'
SIBLING_CSV_SOURCE_ANNOTATION = '@CsvSource({"%s,preceding-sibling::*[1]", "%s,following-sibling::*[1]"})'

JUNIT_ASSERT_EQUALS = 'assertEquals(%s, %s, %s);'

NO_SUCH_ELEMENT_EXCEPTION_CLASS = 'org.openqa.selenium.NoSuchElementException.class'