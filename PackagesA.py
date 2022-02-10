import Packages

class PackageA(Packages.Packages):
    def __init__(self, package_type, brand, installation, service, product1, product2, product3, design, cost):
        super().__init__(package_type, brand, installation, service, cost)
        self.__product1 = product1
        self.__product2 = product2
        self.__product3 = product3
        self._design = design


    def set_product1(self,product1):
        self.__product1 = product1

    def set_product2(self,product2):
        self.__product2 = product2

    def set_product3(self,product3):
        self.__product3 = product3

    def set_design(self,design):
        self.__design = design


    def get_design(self):
        return self.__design

    def get_product1(self):
        return self.__product1

    def get_product2(self,):
        return self.__product2

    def get_product3(self):
        return self.__product3
