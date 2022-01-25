class User:
    count_id = 0

    def __init__(self, username, email, gender, password):
        User.count_id +=1
        self.__user_id = User.count_id
        self.__username = username
        self.__email = email
        self.__gender = gender
        self.__password = password

    def get_user_id(self):
        return self.__user_id

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def get_password(self):
        return self.__password


    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_gender(self, gender):
        self.__gender = gender

    def set_password(self, password):
        self.__password = password




