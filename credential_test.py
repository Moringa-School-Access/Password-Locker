import unittest # Importing unittest Module
from credential import Credential  # Importing Credential Class

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Arg:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Alex", "Otieno", "Alexotieno1717", "Alex123", "Alexotien900@gmail.com") #New credential

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.first_name, "Alex")
        self.assertEqual(self.new_credential.last_name, "Otieno")
        self.assertEqual(self.new_credential.user_name, "Alexotieno1717")
        self.assertEqual(self.new_credential.password, "Alex123")
        self.assertEqual(self.new_credential.email, "alexotieno900@gmail.com")

    def test_save_credential(self):
        '''
        Test if credential object is saved in credential_list
        '''
        self.new_credential.save_credential() #Saving new credential
        self.assertEqual(len(Credential.credential_list), 1)