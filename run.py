#!/usr/bin/env python3
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
    user.delete_user()