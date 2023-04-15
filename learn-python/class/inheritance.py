''' takes all attributes and methods of parent class '''

class Parent():
    ''' parent class '''

    def __init__(self, name, catagery):
        ''' initiate parent class '''
        self.name = name
        self.catagery = catagery

class Child(Parent):
    ''' child class of parent '''

    def __init__(self, name, catagery, repo):
        ''' initiate attributes of parent class '''
        super().__init__(name, catagery)        # super() calls parent attributes
        self.repo = repo
    
    def status(self):
        ''' check status '''
        status_msg = self.name.title() + " of " + self.catagery + " is working"
        return status_msg

test_inherit = Child('inheritance', 'class', 'learn-python')
print(test_inherit.name.title() + " of " + test_inherit.catagery + " in " + test_inherit.repo)
print(test_inherit.status())

# Instances as Attributes

class Instance_catagery():
    ''' parent class, instance '''

    def __init__(self, catagery='class'):
        ''' initiate attributes of instance '''
        self.catagery = catagery
    
    def discribe(self):
        ''' discribing catagery '''
        discription = self.catagery
        return discription

class Instance_attribute():
    ''' child class, used instance as attribute '''

    def __init__(self, sector):
        ''' initiate attributes of parent class '''
        self.sector = sector
        self.catagery = Instance_catagery()     # instance as attribute, used here

test_instance = Instance_attribute('Instance as Attribute')
print(test_instance.sector + " of " + test_instance.catagery.discribe())    # get attribute