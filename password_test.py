import unittest # Importing the unittest module
from credentials import Credentials
from user import User


class TestCredentials(unittest.TestCase):
    '''hfbhbhfbvhbfhvbhfvb
    '''
    def setUp(self):
        """fhghgithgu"""
        self.new_credentials =Credentials("pintres", "pepe" , "pipi")

    def test_init(self):
        "gfhugehthguthgu"

        self.assertEqual(self.new_credentials.account_name,"pintres")
        self.assertEqual(self.new_credentials.account_username,"pepe")
        self.assertEqual(self.new_credentials.account_password,"pipi") 

    def test_find_by_account_name(self):
        '''
        Test case to check if we can find an account by username and display information
        '''
        self.new_credentials.save_credentials()
        test_account = Credentials("Pintres", "pepe", "pipi")
        test_account.save_credentials()

        found_account = Credentials.find_by_account_name('pepe')
        self.assertEqual(found_account.account_name,test_account.account_name)

class TestUser(unittest.TestCase): #subclass class that inherits from unittest.TestCase

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    '''
#user account
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.UserList = []

    def setUp(self): #first test, test to see if our objects are being instantiated correctly.
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Tracy","Sareto","Tate","Tracy@2022") # create user object
   

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Tracy")
        self.assertEqual(self.new_user.last_name,"Sareto")
        self.assertEqual(self.new_user.username,"Tate")
        self.assertEqual(self.new_user.password,"Tracy@2022")

   

    def test_save_user(self): #second test
        ''' test case to test if user objects is saved in UserList'''  
        self.new_user.save_user() 
        self.assertEqual(len(User.UserList),1) 

    def test_save_multiple_user(self): #third test
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our UserList
            '''
            self.new_user.save_user()
            test_user = User("Test","user","Tate","Tracy@2022") # new user
            test_user.save_user()
            self.assertEqual(len(User.UserList),2)

    def test_delete_user(self): #fourth test
            '''
            test_delete_user to test if we can remove a user from our userlist
            '''
            self.new_user.save_user()
            test_user = User("Test","user","Tate","Tracy@2022") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.UserList),1)
    
    def test_find_user_by_password(self): #fifth test
        '''
        test to check if we can find a user by user password and display information
        '''

        self.new_user.save_user()
        test_user = User("Tracy","Sareto","Tate","Tracy@2022") # new user
        test_user.save_user()

        find_user = User.find_by_password("Tracy@2022")
        self.assertEqual(find_user.password,test_user.password)  
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Tracy","Sareto","Tate","Tracy@2022") # new user
        test_user.save_user()

        user_exists = User.user_exist("Tate")

        self.assertTrue(user_exists) 
         

    def test_display_all_user(self):
        '''
        method that returns a list of all user saved
        '''

        self.assertEqual(User.display_user(),User.UserList)  

    
    
     

    
    
if __name__ == '__main__':
    unittest.main()


