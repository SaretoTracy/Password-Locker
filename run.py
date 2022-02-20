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

def main():
    print("Hello Welcome to your password-locker. What is your name?")
    username = input()

    print(f"Hello {username}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list ")

        short_code = input().lower()

        if short_code == 'cc':
                print("New user")
                print("-"*10)

                print ("First name ....")
                first_name = input()

                print("Last name ...")
                last_name = input()

                print("Username ...")
                username = input()

                print("Password ...")
                password = input()


                save_user(create_user(first_name,last_name,username,password)) # create and save new user.
                print ('\n')
                print(f"New user {first_name} {last_name} created")
                print ('\n')

        elif short_code == 'dc':

                if display_user():
                        print("Here is a list of all your users")
                        print('\n')

                        for user in display_user():
                                print(f"{user.first_name} {user.last_name} .....{user.username}")

                        print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any users saved yet")
                        print('\n')

        elif short_code == 'fc':

                print("Enter the username you want to search for")

                search_username = input()
                if check_existing_user(search_username):
                        search_user = find_user(search_username)
                        print(f"{search_user.first_name} {search_user.last_name}")
                        print('-' * 20)

                        print(f"username.......{search_user.username}")
                        print(f"password.......{search_user.email}")
                else:
                        print("That user does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")
if __name__== "__main__":
    main()  