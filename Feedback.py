import Name


class Feedback(Name.Name):
    count_id = 0

    def __init__(self, first_name, last_name, email, web_rating, service_rating, feedback):
        super().__init__(first_name, last_name)
        Feedback.count_id += 1
        self.__user_id = Feedback.count_id
        self.__email = email
        self.__web_rating = web_rating
        self.__service_rating = service_rating
        self.__feedback = feedback
        self.__status = ""

    def get_user_id(self):
        return self.__user_id

    def get_email(self):
        return self.__email

    def get_web_rating(self):
        return self.__web_rating

    def get_service_rating(self):
        return self.__service_rating

    def get_feedback(self):
        return self.__feedback

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_email(self, email):
        self.__email = email

    def set_web_rating(self, web_rating):
        self.__web_rating = web_rating

    def set_service_rating(self, service_rating):
        self.__service_rating = service_rating

    def set_feedback(self, feedback):
        self.__feedback = feedback

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status


















