#!/usr/bin/env python3
from click import option
from user import User
# functions that implement the behaviours we have created
def create_user(first_name,last_name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,username,password)
    return new_user

def save_user(User):
    '''
    Function to save user
    '''
    User.save_user()

def delete_user(user):
    '''
    Function to delete a user
    '''
    User.delete_user()

def find_user(password):
    '''
    Function that finds a user by password and returns the user
    '''
    return User.find_by_password(password)

def check_existing_user(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

def main(): #main function that calls all the other function
    print("Hello Welcome to your password-locker. Write Signup or Login to start")
    print("Signup -or- Login")
    option = input()
    
    if option == "Signup":
       print("Create an account")
       print("*️⃣4️" *10)
       print("Enter your First name")
       first_name=input()
       print("Enter your Last name")
       last_name=input()
       print("Enter your Username")
       username=input()
       print("Set your password")
       password=input()

    
if __name__== "__main__":
    main()  