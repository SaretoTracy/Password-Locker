#!/usr/bin/env python3
from credentials  import Credentials
from user import User
import random
import string
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
    Credentials.delete_credentials()

def find_account(account_name):
    '''
    Function that finds a user by password and returns the user
    '''
    return Credentials.find_by_account_name (account_name)

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

def generate_password():
        '''
        Function to generate a random password
        '''
        password_list = []
        characters_upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
        characters_lower = 'abcdefghijklmnopqrstuvwxyz'.lower()
        numbers = '0123456789'
        symbols = '!@#$%&*'
        for i in range(3):
            password_list.append(random.choice(characters_upper))
            password_list.append(random.choice(characters_lower))
            password_list.append(random.choice(numbers))
            password_list.append(random.choice(symbols))
        passwordgen = ''.join(password_list)
        return passwordgen

def main(): #main function that calls all the other function
    while True:
        print("Hello Welcome to your password-locker. Write signup or login to start")
        print("signup -or- login")
        option = input()
        
        if option == "signup":
                print("Create an account")
        
                print("🔒" *20)
                print("Enter your First name")
                first_name=input()
                print("Enter your Last name")
                last_name=input()
                print("Enter your Username")
                username=input()
                print("Set your password")
                password=input()
                print("\n")
                

                save_user(create_user(first_name, last_name, username, password))
                print("Your accout was succesfully created.These are you details")
                print("🔒" *20)
                
                print(f"Name:{first_name} {last_name} \nUsername: {username} \nPassword: {password}")
                print("Login into your account with these details")
                

                print("🔒" *20)
        elif option == "login":
                print("Enter your Username")
                username=input()
                print("Enter you user password")
                password=input()
        
                
                print("🔓" *20)
                while True:
                    print(" You can create multiple credential account (CA) \n view your accounts(VA) \nfind account(FA) \n delete account(DA) \n exit account (EXT")
                    choice= input()
                    if choice == "CA":
                        print("Create Credential account")
                        print("🔒" *20)
                        print("\n")
                        print("Enter your account_name")
                        account_name=input()
                        print("Enter your  account_username")
                        account_username=input()
                        print("\n")
                        print("Generate new password (G) Create new passord (C)")
                        action =input()
                        if action == "G":
                           passwordgen = generate_password()
                           print("🔒" *5)
                           print("Your password is: " + passwordgen)
                           print("🔒" *5)
                           save_credentials(create_account(account_name,account_username,passwordgen))
                           
                        elif action=="C":
                            print("Enter your password")
                            account_password=input()
                            print("\n")
                            print("🔒" *20)

                            save_credentials(create_account(account_name,account_username,account_password))
                            print("\n")
                        print("Your accout was succesfully created.These are you details")
                        
                        # print(f"AccountName:{account_name} \nAccountUsername: {account_username} \nAccount_Password:{account_password}")

                            
                    elif choice == "VA":
                        print("Enter account you want to view")
                        if display_credentials():
                            print("\n")
                            
                            for Credential in display_credentials():
                                print("Here is a list pf your Account")
                                print("\n")
                                print("🔐" *20)
                                print("\n")
                                print(f"{Credential.account_name} \n{Credential.account_username} \n{Credential.account_password}")
                                print("\n")
                                print("🔐" *20)
                        else:
                            print("That account does not exist")

                    elif choice == 'FA':
                        print('Enter the ACCOUNT name you want to search for')
                        account_name = input()
                        if check_existing_account(account_name):
                            search_account = find_account(account_name)
                            print(f"{account_name} {account_username} {account_password}")
                            print('-'*20)
                            print(f"Account name: {search_account.account_name}")
                            print(f"Account username: {search_account.account_username}")
                        else:
                                print("That account does not exist")

                    elif choice == 'DA':
                        
                        print("Enter the account name you want to delete:")
                        account_name = input()
                        if find_account(account_name):
                            delete_credentials(find_account(account_name))
                            print(f"{account_name} account has been deleted")
                            print('\n')
                        else:
                            print("That credential does not exist")
                            print('\n')

                    #exit app
                    elif choice == 'EXT':
                        print('Thank you for considering our service. Goodbye for now see you later!')
                        break
                    else:
                        print('I really didnt get that. Please use the short codes')

                                

                            


   
if __name__== "__main__":
    main()  