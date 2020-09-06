import random


# User Class
class User:
    '''
    Create User that generate new instance of user
    '''

    user_list = [] # Empty User list    

    def __init__(self, user_name, email, password):
        '''
        __init__ method that helps us define the property of our object

        Arg:
            loginUser: New User Login
            loginPassword: New User Password
        '''

        self.user_name = user_name
        self.email = email
        self.password = password

    def save_user(self):

        '''
        save_credential method save user object into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        '''
        display_users method that return the class list
        '''

        return cls.user_list



# Class Credentials
class Credential:

    '''
    class that create new instance of credential
    '''

    credential_list = [] # Empty credential list

    def __init__(self, first_name, last_name, user_name, password, email):
        '''
        __init__ method help us define the property of our object
        
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credential(self):
        
        '''
        save_credential method saves credential objects into credential_list
        
        ''' 

        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method delete credential saved in the credential_list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_email(cls, email):
        '''
        find_email method takes an email and return an email the matches the credential
        
        Arg:
            email: email to search for
        Return:
            Credentials of person that matches the email.
        '''

        for credential in cls.credential_list:
            if credential.email == email:
                return credential
    
    @classmethod
    def credential_exit(cls, email):
        '''
        Method that check if credential exit from credential_list

        Arg:
            email: email to search for email exit
        Returns:
            Boolean : True or False
        '''
        for credential in cls.credential_list:
            if credential.email == email:
                return True

        return False

    @classmethod
    def display_credential(cls):
        '''
        display_credential method that retuns the list of credential_list
        '''
        return cls.credential_list

    