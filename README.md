# How to set up
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.text
```

# How to run
Chrome
```
behave features/testcases/CompletePurchase.feature
```
Firefox
```
behave features/testcases/CompletePurchase.feature -D BROWSER=firefox
```
# Troubleshooting with webdrivers
Check where webdriver being used
```
which geckodriver
which chromedriver
```

# How to do assertions
Values comparison including complex data structure
Ref: https://pypi.org/project/compare/
Use: https://pythonhosted.org/compare/#api-reference

# Print standard output
https://www.python-course.eu/python3_formatted_output.php
To print multiple lines, 2 choices:
- no color output, use plain instead
- adding \n at the end of output statement

# Behave settings
https://behave.readthedocs.io/en/latest/behave.html#cmdoption-capture

# Todo
1. Environment: See http://www.seleniumframework.com/python-frameworks/road-map-and-future-state/
- URL
- Username
- Password
self.timeout = 30 in class BasePage(object):
2. Config
- Browser capabilities
- Browserstack
3. Html report
4. Adding more page objects, steps, features
5. Using tag to auto-load AUT and do systemLogin
