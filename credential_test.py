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

    # def test_init(self):
    #     '''
    #     test_init test case to test if the object is initialized properly
    #     '''

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if object utilizes proper instantiation
        '''
        self.assertEqual(self.new_user.user_name,"Alexotieno")
        self.assertEqual(self.new_user.email,"alexotieno900@gmail.com")
        self.assertEqual(self.new_user.password,"alex123")
