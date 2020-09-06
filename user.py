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



