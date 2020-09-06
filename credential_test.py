import unittest #Importing Unittest module
from credentials import User # Importing User from credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    
    Arg:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before the test case
        '''
        self.new_user = User("Alexotieno", "alexotieno900@gmail", "alex123")