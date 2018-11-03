class BasePage(object):

    def __init__(self, context):
        self.browser = context.wdriver
        self.su = context.su

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                listWebElement = self.su.get_elements(*self.locator_dictionary[what])
                if len(listWebElement) == 1:
                    return listWebElement[0]
                else:
                    return listWebElement
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print ("No %s here!"%what)
