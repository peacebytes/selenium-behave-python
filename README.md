# How to set up
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.text
```

# How to run
(Defaul on browser:Chrome, env: local)
```
behave
```

# Execute testing specific feature files and selected browser
```
behave features/testcases/Smoketest.feature -D BROWSER=firefox
```

# How assertion to be done?
Values comparison including complex data structure. See usage at:
Ref: https://pypi.org/project/compare/
Use: https://pythonhosted.org/compare/#api-reference

# Behave settings
https://behave.readthedocs.io/en/latest/behave.html#cmdoption-capture

# Report
https://pypi.python.org/pypi/allure-behave/
