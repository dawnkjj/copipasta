class Login:
    def __init(self, username, password):
        self._username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password
