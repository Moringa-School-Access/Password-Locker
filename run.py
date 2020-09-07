#!/usr/bin/env python3.8
from credential import Credential
from user import User
import random

def create_credentials(fname,lname,user_name,password,email):
    '''
    Function of creating new credential
    '''
    new_credential = Credential(fname,lname,user_name,password,email)
    return new_credential

def create_user(user_name,email,password):
    '''
    function of creating new user
    '''
    new_user = User(user_name, email, password)
    return new_user

def save_credential(credential):
    '''
    Function that save credential
    '''
    credential.save_credential()

def save_user(user):
    '''
    Function that saves user details
    '''
    user.save_user()

def delete_credential(credential):
    '''
    Function that delete credential
    '''
    credential.delete_credential()

def find_credential(email):
    '''
    Function that finds credential by email
    '''
    return Credential.find_email(email)

def checking_existing_credentials(email):
    '''
    Function that check if credentials exists with that email and return a Boolean
    '''
    return Credential.credential_exit(email)

def display_credential():
    '''
    Function that return all saved credential
    '''
    return Credential.display_credential()

def display_user():
    '''
    Functio that display user
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your credential List. Whats your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like ")
    print('\n')

    while True:
        print("Use thes short codes : \n cc - create account with a user_defined password \n dc - display credential \n cg -create account with" 
              "auto-generated password \n ex -exit ") 
        short_code = input().lower()

        if short_code == "cc":
            print("user_name")
            print("-" * 10)
            print("What account would like to create credentials for?")
            site = input()
            print("----------------")
                            
            print("First name ....")
            fname = input()

            print("Last name ...")
            lname = input()

            print("Enter username ...")
            user_name = input()

            print("Email Address ...")
            email = input()

            print("Enter a password")
            password = input()

            save_user(create_user(user_name, email, password))
            save_credential(create_credentials(fname, lname, user_name, password, email))
            print("\n")
            print(f"A new {site} account by {fname} has successfully been created")
            print(f"The username is {user_name} and the password is {password} ")
            print("\n")
        elif short_code == "dc":
            if display_credential   ():
               print("Here is a list of all your user credentials accounts")
               print("/n")

               for credentials in display_credential():
                   print(f"{credentials.first_name} {credentials.last_name} {credentials.user_name} has credentials for this {site}")
               print("\n")
            else:
                print("\n")
                print("It looks like no account credentials exist at the moment. Consider creating one or more ")
                print("\n")

        elif short_code == "cg":
            print("New user")
            print("-" * 10)
            print("Which account would you like to create?")
            site = input()
            print("----------------")

            print("First name ....")
            fname = input()

            print("Last name ...")
            lname = input()

            print("Enter username ...program will generate a password for you")
            user_name = input()

            print("Email Address ...")
            email = input()

            password_generator = "12345678910!@#$%^&*()+-?><abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            password = "".join(random.sample(password_generator, 8))
            print("Password")

            save_user(create_user(user_name, email, password))
            save_credential(create_credentials(fname, lname, user_name, email, password))
            print("\n")
            print(f"the username is {user_name} and the password is {password}")
            print("\n")
        elif short_code == "ex":                
            print("Bye ....")
            break
        else:
            print("Invalid command")

if __name__ == '__main__':
    main()

