class User:
    """
    Class that generates new instances of user
    """


    UserList = [] #empty user list
    
    def __init__ (self,first_name,last_name,username,password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_user(self):

        '''
        test case to test if user objects is saved in UserList
        '''

        User.UserList.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the userlist
        '''

        User.UserList.remove(self)
    

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a user that matches that password.

        Args:
            password: user password to search for
        Returns :
            user of person that matches the password.
        '''

        for user in cls.UserList:
            if user.password == password:
                return user
            else:
               print("Wrong password")
               return False
    @classmethod           
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
           username: Phoneusername to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.UserList:
            if user.username == username:
                    return True

        return False

    @classmethod
    def display_user(cls):
        '''
        method that returns the UserList
        '''
        return cls.UserList
    
    