import Stock

class StockPaint(Stock.Stock):
    count_id = 0

    def __init__(self, stock_name, stock_count, colour, price, date_created, remarks):
        super().__init__(stock_name, stock_count)
        self.__colour = colour
        self.__price = price
        self.__date_created = date_created
        self.__remarks = remarks

    def get_colour(self):
        return self.__colour

    def get_price(self):
        return self.__price

    def get_date_created(self):
        return self.__date_created

    def get_remarks(self):
        return self.__remarks

    def set_colour(self, colour):
        self.__colour = colour

    def set_price(self, price):
        self.__price = price
        
    def set_date_created(self, date_created):
        self.__date_created = date_created

    def set_remarks(self, remarks):
        self.__remarks = remarks
