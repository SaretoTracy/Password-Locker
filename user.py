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

    