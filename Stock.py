class Stock:
    count_id = 0

    def __init__(self, stock_name, stock_count):
        Stock.count_id += 1
        self.__stock_id = Stock.count_id
        self.__stock_name = stock_name
        self.__stock_count = stock_count

    def get_stock_id(self):
        return self.__stock_id

    def get_stock_name(self):
        return self.__stock_name

    def get_stock_count(self):
        return self.__stock_count

    def set_stock_id(self, stock_id):
        self.__stock_id = stock_id

    def set_stock_name(self, stock_name):
        self.__stock_name = stock_name

    def set_stock_count(self, stock_count):
        self.__stock_count = stock_count
