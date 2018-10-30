from selenium import webdriver
from colorama import init
init()
import os
from lib.pagefactory import on
from selenium.webdriver.chrome.options import Options
from ConfigParser import SafeConfigParser
import json

def before_all(context):
     print("Loading configs.ini")
     # Loading configs.ini
     config = SafeConfigParser()
     config.read('./resources/Configs.ini')
     context.host = config.get('config', 'host')
     context.user = config.get('config', 'user')
     context.passwd = config.get('config', 'passwd')
     context.browser = config.get('config', 'browser')
     context.env = config.get('config', 'env')
     context.timeout = config.getint('config', 'timeout')
     print("context.host: %s" % context.host)
     print("context.user: %s" % context.user)
     print("context.passwd: %s" % context.passwd)
     print("context.timeout: %s" % context.timeout)

     # Loading testdata.json
     with open('./resources/TestData.json', 'r') as f:
            context.testdata = json.load(f)

def before_feature(context, feature):
    print("\nFeature being executed: %s" % feature.name)

# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    # behave -D browser=chrome -D env=bs
    if 'browser' in context.config.userdata.keys():
     if context.config.userdata['browser'] is not None:
      context.browser = context.config.userdata['browser']

    if 'env' in context.config.userdata.keys():
     if context.config.userdata['env'] is not None:
      context.env = context.config.userdata['env']

    print("context.browser: %s" % context.browser)
    print("context.env: %s" % context.env)

    BROWSER = context.browser;
    ENV = context.env;
    # Set up webdriver before each scenario
    if BROWSER == 'chrome':
        context.wdriver = webdriver.Chrome()
    elif BROWSER == 'firefox':
        context.wdriver = webdriver.Firefox()
    elif BROWSER == 'headless':
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        context.wdriver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        print("Browser you entered: [" + BROWSER + "] is invalid value")

    # Clear cookies before each scenario
    context.wdriver.delete_all_cookies();
    context.wdriver.maximize_window()

def after_scenario(context, scenario):
    print("   Scenario Status: %s" % (scenario.status))
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    # Destroy webdriver after each scenario
    context.wdriver.quit()

def after_feature(context, feature):
     print("\nExecution Feature [" + feature.name + "] is complete.")

def after_all(context):
    print("All done!")
