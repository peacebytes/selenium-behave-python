
# How to create virtual env
For Linux
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

For Windows
```
pip install virtualenv
virtualenv venv
source venv/Scripts/activate
```

# How to set up dependencies
```
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

# How to set and use global variables?
In any step definition file, set global variable by using `context`. For example:
```
context.a = 1
context.b = 9
```
Agin, in step definition files, use global variable by using `context`. For example:
```
context.sum = int(context.a) + int(context.b)
```

* Notes: `context` is retained within a test scenario only.

# How assertion to be done?
Values comparison including complex data structure. See usage at:
Ref: https://pypi.org/project/compare/
Use: https://pythonhosted.org/compare/#api-reference

# Behave settings
https://behave.readthedocs.io/en/latest/behave.html#cmdoption-capture

# Report
https://pypi.python.org/pypi/allure-behave/
