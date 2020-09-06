import unittest #Importing Unittest module
from user import User # Importing User from credential

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

    def test_save_user(self):
        '''
        test case to test if the user object is saved in users array
        '''
        self.new_user.save_user() # Saving new user
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
        this test-case method gives users the ability to save multiple account details
        '''
        self.new_user.save_user()
        test_user = User("Mercyline", "aokomercyline@gmail.com", "mercy123")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_display_all_user(self):
        '''
        Method that return a list of all users saved
        '''
        self.assertEqual(User.display_users(), User.user_list)

if __name__ == '__main__':
    unittest.main()

