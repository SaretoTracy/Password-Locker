import unittest # Importing the unittest module
from user import User
from credentials import Credentials
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

    def save_user(self): #second test
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

        found_user = User.find_by_password("Tracy@2022")
        self.assertEqual(found_user.password,test_user.password)  
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

#user credential accounts
    # def tearDown(self):
    #         '''
    #         tearDown method that does clean up after each test case has run.
    #         '''
    #         User.UserList = []

    # def setUp(self): #first test, test to see if our objects are being instantiated correctly.
    #     '''
    #     Set up method to run before each test cases.
    #     '''
    #     self.new_user = User("Tracy","Sareto","Tate","Tracy@2022") # create user object


    # def test_init(self):
    #     '''
    #     test_init test case to test if the object is initialized properly
    #     '''

    #     self.assertEqual(self.new_user.first_name,"Tracy")
    #     self.assertEqual(self.new_user.last_name,"Sareto")
    #     self.assertEqual(self.new_user.username,"Tate")
    #     self.assertEqual(self.new_user.password,"Tracy@2022")

    # def save_user(self): #second test
    #     ''' test case to test if user objects is saved in UserList'''  
    #     self.new_user.save_user() 
    #     self.assertEqual(len(User.UserList),1) 

    # def test_save_multiple_user(self): #third test
    #         '''
    #         test_save_multiple_user to check if we can save multiple user
    #         objects to our UserList
    #         '''
    #         self.new_user.save_user()
    #         test_user = User("Test","user","Tate","Tracy@2022") # new user
    #         test_user.save_user()
    #         self.assertEqual(len(User.UserList),2)

    # def test_delete_user(self): #fourth test
    #         '''
    #         test_delete_user to test if we can remove a user from our userlist
    #         '''
    #         self.new_user.save_user()
    #         test_user = User("Test","user","Tate","Tracy@2022") # new user
    #         test_user.save_user()

    #         self.new_user.delete_user()# Deleting a user object
    #         self.assertEqual(len(User.UserList),1)
    
    # def test_find_user_by_password(self): #fifth test
    #     '''
    #     test to check if we can find a user by user password and display information
    #     '''

    #     self.new_user.save_user()
    #     test_user = User("Tracy","Sareto","Tate","Tracy@2022") # new user
    #     test_user.save_user()

    #     found_user = User.find_by_password("Tracy@2022")
    #     self.assertEqual(found_user.password,test_user.password)  
    # def test_user_exists(self):
    #     '''
    #     test to check if we can return a Boolean  if we cannot find the user.
    #     '''

    #     self.new_user.save_user()
    #     test_user = User("Tracy","Sareto","Tate","Tracy@2022") # new user
    #     test_user.save_user()

    #     user_exists = User.user_exist("Tate")

    #     self.assertTrue(user_exists) 
         

    # def test_display_all_user(self):
    #     '''
    #     method that returns a list of all user saved
    #     '''

    #     self.assertEqual(User.display_user(),User.UserList)    


    
if __name__ == '__main__':
    unittest.main()


