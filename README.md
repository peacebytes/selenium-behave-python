# How to set up
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

# How to load virtual environment with all dependencies
```
source venv/bin/activate
nvm install 10.9
nvm use 10.9
pip install -r requirements.text
```

# How to run
Chrome
```
behave features/testcases/CompleteShoppingCart.feature
```
Firefox
```
behave features/testcases/CompleteShoppingCart.feature -D BROWSER=firefox
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
