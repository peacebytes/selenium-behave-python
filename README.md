# README #

### What is this? ###

This repository is used for automated functional test of web application.

Based on:
- selenium
- behave
- python

* Note: Python version >= 3.7
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
behave -D browser=chrome -D env=local
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
On Jenkins: feeding cucumber-report with json file at `reports/results.json`.
