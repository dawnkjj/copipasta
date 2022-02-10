class RequestForm:
    count_id = 0

    def __init__(self,type_of_services,type_of_installation,type_of_items,type_of_brands,items_available):
        RequestForm.count_id += 1
        self.__request_id = RequestForm.count_id
        self.__type_of_services = type_of_services
        self.__type_of_installation = type_of_installation
        self.__type_of_items = type_of_items
        self.__type_of_brands = type_of_brands
        self.__items_available = items_available
        self.__remarks = ""
        self.__startdate = ""
        self.__enddate = ""
        self.__workcompletion_status = ""
        self.__customer_id = ""
        self.__amount = 0
        self.__payment_status = ""

        #administrator update line 12-15, after customer pay, update line 18 to "Paid"
        # after creating update line 16,17


    def get_request_id(self):
        return self.__request_id

    def get_type_of_services(self):
        return self.__type_of_services

    def get_type_of_installation(self):
        return self.__type_of_installation

    def get_type_of_items(self):
        return self.__type_of_items

    def get_type_of_brands(self):
        return self.__type_of_brands

    def get_items_available(self):
        return self.__items_available

    def get_amount(self):
        return self.__amount

    def get_remarks(self):
        return self.__remarks

    def get_startdate(self):
        return self.__startdate

    def get_enddate(self):
        return self.__enddate

    def get_workcompletion_status(self):
        return self.__workcompletion_status

    def get__customer_id(self):
        return self.__customer_id

    def get_payment_status(self):
        return self.__payment_status

    def set_request_id(self,request_id):
        self.__request_id = request_id

    def set_type_of_services(self,type_of_services):
        self.__type_of_services = type_of_services

    def set_type_of_installation(self,type_of_installation):
        self.__type_of_installation = type_of_installation

    def set_type_of_items(self,type_of_items):
        self.__type_of_items = type_of_items

    def set_type_of_brands(self,type_of_brands):
        self.__type_of_brands = type_of_brands

    def set_items_available(self,items_available):
        self.__items_available = items_available

    def set_amount(self,set_amount):
        self.__amount = set_amount

    def set_remarks(self,remarks):
        self.__remarks = remarks

    def set_startdate(self,startdate):
        self.__startdate = startdate

    def set_enddate(self,enddate):
        self.__enddate = enddate

    def set_customer_id(self,customer_id):
        self.__customer_id = customer_id

    def set_workcompletion_status(self,workcompletion_status):
        self.__workcompletion_status = workcompletion_status

