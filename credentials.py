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

    Credential_list = [] # Empty credential list

    def __init__(self, username, password=None):
        '''
        __init method help us define the property of our object
        
        Arg:
            username: New username.
            password: New password.
        '''

        self.username = username
        self.password = password if password else Credential.password_generator()

    def save_credential(self):
        
        '''
        save_credential method saves credential objects into credential_list
        
        ''' 

    