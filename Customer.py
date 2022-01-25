import User

class Customer(User.User):
    def __init__(self, username, email, gender,password, membership, address):
        super().__init__(username, email, gender, password)
        Customer.count_id += 1
        self.__customer_id = Customer.count_id
        self.__membership = membership
        self.__address = address

    def set_customer_id(self,customer_id):
        self.__customer_id = customer_id

    def get_customer_id(self):
        return self.__customer_id

    def set_membership(self, membership):
        self.__membership = membership

    def get_membership(self):
        return self.__membership

    def set_address(self,address):
        self.__address = address

    def get_address(self):
        return self.__address
