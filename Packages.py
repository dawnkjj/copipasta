class Packages:
    count_id = 0

    def __init__(self, package_type, brand, installation, service, cost):
        Packages.count_id += 1
        self.__order_id = Packages.count_id
        self.__package_type = package_type
        self.__brand = brand
        self.__installation = installation
        self.__service = service
        self._cost = cost

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_order_id(self):
        return self.__order_id

    def set_package_type(self,package_type):
        self.__package_type = package_type

    def set_brand(self, brand):
        self.__brand = brand

    def set_installation(self, installation):
        self.__installation = installation

    def set_service(self, service):
        self.__service = service

    def set_cost(self, cost):
        self.__cost = cost

    def get_cost(self):
        return self.__cost

    def get_package_type(self):
        return self.__package_type

    def get_brand(self):
        return self.__brand

    def get_installation(self):
        return self.__installation

    def get_service(self):
        return self.__service


