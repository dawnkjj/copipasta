class Reward:
    count_id = 0

    def __init__(self, first_name, last_name, phone_no, email, remarks,reward_type):
        Reward.count_id += 1
        self.__reward_id = Reward.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__reward_type = reward_type
        self.__remarks = remarks
        self.__email = email
        self.__phone_no = phone_no


    def get_reward_id(self):
        return self.__reward_id

    def get_email(self):
        return self.__email

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_remarks(self):
        return self.__remarks

    def get_phone_no(self):
        return self.__phone_no

    def set_phone_no(self, phone_no):
        self.__phone_no = phone_no

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def set_email(self, email):
        self.__email = email

    def set_reward_id(self, reward_id):
        self.__reward_id = reward_id

    def get_reward_type(self):
        return self.__reward_type

    def set_reward_type(self, reward_type):
        self.__reward_type = reward_type
