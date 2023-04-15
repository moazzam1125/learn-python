'''
Unittest
---------
Python unit testing framework, testing proves that code works as it’s supposed.

- 'unit test' verifies that one specific aspect of a function’s behavior is correct.
- 'test case' is a collection of unit tests that together prove that a function behaves as it’s supposed.
** test case with 'full coverage' includes a full range of unit tests covering all the possible ways you can use a function.
'''

import unittest

## TestCase

# setUp() method

class Store_class():
    ''' example class for setUp() '''

    def __init__(self):
        ''' initiate attributes of class '''
        self.sector = []
        
    def store_list(self, sector):
        ''' store items in list '''
        self.sector.append(sector)

class Test_Storeclass(unittest.TestCase):
    ''' TestCase for setUp() method '''

    def setUp(self):
        ''' Setup create objects once, for use in all test methods '''
        self.my_list_store = Store_class()
        self.sector = ['setUp method', 'methods', 'unittest']
    
    def test_store_single(self):
        ''' Test store_list to store single item '''
        self.my_list_store.store_list(self.sector[0])
        self.assertIn(self.sector[0], self.my_list_store.sector)
    
    def test_store_triple(self):
        ''' Test store_list to store three items '''
        for block in self.sector:
            self.my_list_store.store_list(block)
        for block in self.sector:
            self.assertIn(block, self.my_list_store.sector)

#unittest.main()

# Function test

def test_name(fname, sname):
    ''' Test of function for formattting '''
    get_name = fname + " " + sname
    return get_name

class FunctionTestCase(unittest.TestCase):
    ''' TestCase for functions '''

    def test_testname(self):
        """ test for function 'test_name' """
        test_function = test_name('test_name', 'function')
        self.assertEqual(test_function, 'test_name function')   # see assert methods

#unittest.main()

# Class Test

class Tclass():
    ''' Test of class for append list '''

    def __init__(self, name):
        ''' initiate class attributes '''
        self.name = name
        self.sector = []
    
    def append_list(self, sector):
        ''' store sectors in list '''
        self.sector.append(sector)

class Test_Tclass(unittest.TestCase):
    ''' TestCase for class '''

    def test_tclass(self):
        ''' Test of tclass '''
        name = 'unittest'
        block_tclass = Tclass(name)
        block_tclass.append_list('class test')
        self.assertIn('class test', block_tclass.sector)

unittest.main()