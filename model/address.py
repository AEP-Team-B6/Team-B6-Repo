#Creating class Address
class Address:
    def __init__(self, adress_id: int, street: str, city: str, zip_code: int):
        self.__adress_id = adress_id
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code


    @property
    def address_id(self):
        return self.__adress_id

    @address_id.setter
    def address_id(self, new_address_id):
        self.__adress_id = new_address_id

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, new_street):
        self.__street = new_street

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        self.__city = new_city

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, new_zip_code):
        self.__zip_code = new_zip_code

