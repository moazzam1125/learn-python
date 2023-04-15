''' Class is an object constructor '''

class Sample_class():
    ''' sample class example '''

    def __init__(self, name, catagery):
        ''' initiate class, assign values to objects '''
        self.name = name
        self.catagery = catagery
    
    def status(self):
        ''' check status '''
        status_msg = self.name.title() + " is working"
        return status_msg

test_class = Sample_class('object', 'class')
print(test_class.name.title() + " of " + test_class.catagery)
print(test_class.status())