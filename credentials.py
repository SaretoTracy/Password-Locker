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
def find_by_account_password(cls,account_password):
        '''
        Method that takes in a account_password and returns a account that matches that account_password.

        Args:
            account_password: user account_password to search for
        Returns :
            user of person that matches the account_password.
        '''

        for credentials in cls.Accountlist:
            if credentials.account_password == account_password:
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
