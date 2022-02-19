from typing_extensions import Self
import unittest # Importing the unittest module
from user import User
class TestUser(unittest.TestCase): #subclass class that inherits from unittest.TestCase

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
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

    def save_user(self):
        ''' test case to test if user objects is saved in UserList'''  
        self.new_user.save_user() 
        self.assertEqual(len(User.UserList),1) 
if __name__ == '__main__':
    unittest.main()


