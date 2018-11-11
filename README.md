# README #

### What is this? ###

This repository is an example for automated functional test of web application.

Based on:
- selenium
- behave
- python

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
```

### How to create virtual env
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

### How to set up dependencies
```
pip install -r requirements.text
```

### How to run
(Defaul on browser:headless, env: local)
```
behave
```

### More options to test on local?
Put `@skip` on top of feature files to skip executing them
```
behave
```

Put `@wip` on top of on-going (work in progress) feature files and only execute them
```
behave --tags @wip
```

Running on browser: chrome, env: local
```
behave -D browser=chrome
```

Execute testing specific feature files and selected browser
```
behave features/testcases/Smoketest.feature -D browser=firefox
```

### How do I execute test on Browserstack?
Chrome
```
behave -D browser=chrome -D env=bs
```
Firefox
```
behave -D browser=firefox -D env=bs
```

### How to deal with test data?
Test data is stored at `resources\TestData.json`

Examples of usage in Step Definition files:
- If test data is an array:
```
context.testdata['addresses'][1]['alias']
```
- If test data is an object:
```
context.testdata['address']['alias']
```

### How to set and use global variables?
In any step definition file, set global variable by using `context`. For example:
```
context.a = 1
context.b = 9
```
Again, in step definition files, use global variable by using `context`. For example:
```
context.sum = int(context.a) + int(context.b)
```
* Notes: `context` is retained within a test scenario only.

### How assertion to be done?
Values comparison including complex data structure. See usage at:
https://pythonhosted.org/compare/#api-reference

### Reports
On local: execute this command to see 1 report for each feature file.
```
junit2html reports/TESTS-testcases.Smoketest.xml reports/behave.Smoketest.html
google-chrome reports/behave.Smoketest.html
```
On Jenkins: Build with these command lines:
```
pip install -r requirement.text
behave
export PYTHONPATH=.
python convert2cucumber.py reports/output.json
```
Then use Cucumber Report plugin to generate HTML report.

### Steps to add new test cases
- Adding feature file to folder `features\testcases`. See existing feature files and try to reuse defined steps.
- Adding new Page Object to `features\lib\pages`. Copy existing ones and start from there. For example: `MyAddress.py`
- Updating `features\lib\pages\__init__.py` to include new page object
- Updating `features\environment.py` line `78` to initialize new page objects.
- Adding new Step Definition file for new Page Object at `features\steps`. Copy existing step files and start from tehre. For example: `MyAddressSteps.py`
