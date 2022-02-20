#!/usr/bin/env python3
from credentials  import Credentials
from user import User
# functions that implement the behaviours we have created in user
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

def delete_user(User):
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
    
# functions that implement the behaviours we have created in credentials
def create_account(account_name,account_username,account_password):
    '''
    Function to create a new account
    '''
    new_credentials = Credentials(account_name,account_username,account_password)
    return new_credentials

def save_credentials(Credentials):
    '''
    Function to save user
    '''
    Credentials.save_credentials()

def delete_credentials(Credentials):
    '''
    Function to delete a user
    '''
    Credentials.delete_account()

def find_account(account_password):
    '''
    Function that finds a user by password and returns the user
    '''
    return Credentials.find_by_account_password(account_password)

def check_existing_account(account_username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return Credentials.account_exist(account_username)

def display_credentials():
    '''
    Function that returns all the saved users
    '''
    return Credentials.display_credentials()


def main(): #main function that calls all the other function
    while True:
        print("Hello Welcome to your password-locker. Write Signup or Login to start")
        print("Signup -or- Login")
        option = input()
        
        if option == "Signup":
                print("Create an account")
                print("*️⃣" *10)
                print("Enter your First name")
                first_name=input()
                print("Enter your Last name")
                last_name=input()
                print("Enter your Username")
                username=input()
                print("Set your password")
                password=input()
                print("🔒" *10)

                save_user(create_user(first_name, last_name, username, password))
                print("Your accout was succesfully created.These are you details")
                
                print(f"Name:{first_name} {last_name} \nUsername: {username} \nPassword: {password}")
                print("Login into your account with these details")
                print("🔒" *10)
                #    print("Signup -or- Login")
                #    option = input()
        elif option == "Login":
                print("Enter your Username")
                username=input()
                print("Enter you user password")
                password=input()
        if find_user(password):
                print("🔓" *10)
                print(" You can create multiple credential account (CA) or view your accounts(VA), or display account(DA)")
                choice= input()
                if choice == "CA":
                    print("Create Credential account")
                    print("*️⃣4️" *10)
                    print("Enter your account_name")
                    account_name=input()
                    print("Enter your  account_username")
                    account_username=input()
                    print("Enter your password")
                    account_password=input()
                    print("🔒" *10)

                    save_credentials(create_account(account_name,account_username,account_password))
                    print("Your accout was succesfully created.These are you details")
                    
                    print(f"AccountName:{account_name} \nAccountUsername: {account_username} \nAccount_Password:{account_password}")

                else:
                        print("That Account does not exist")

                


   
if __name__== "__main__":
    main()  