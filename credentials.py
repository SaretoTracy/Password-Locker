import random
import string

class Credentials:
    """
    Class that generates new instances of credentials
    """
    Accountlist= [] #empty credential list
    
    def __init__ (self,account_name,account_username,account_password):
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password


    def save_credentials(self):

        '''
        test case to test if accounts objects is saved in accountlist
        '''

        Credentials.Accountlist.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credential from the accountlist
        '''

        Credentials.Accountlist.remove(self)
    

    @classmethod
    def find_by_account_name(cls,account_name):
            '''
            Method that takes in a account_name and returns a account that matches that account_name.

            Args:
                account_name: user account_name to search for
            Returns :
                user of person that matches the account_name.
            '''

            for credentials in cls.Accountlist:
                if credentials.account_name == account_name:
                    return credentials

    

    @classmethod           
    def account_exist(cls,account_username):
            '''
            Method that checks if a account exists from the account list.
            Args:
            accountname: Phoneaccountname to search if it exists
            Returns :
                Boolean: True or false depending if the account exists
            '''
            for credentials in cls.Accoubtlist:
                if credentials.account_username == account_username:
                        return True

            return False

    @classmethod
    def display_credentials(cls):
            '''
            method that returns the accountList
            '''
            return cls.Accountlist
    
    