 #Creating class Facility
class Facility:
    def __init__(self, facility_id: int, facility_name: str):
        self.__facility_id = facility_id
        self.__facility_name = facility_name

    @property
    def facility_id(self):
        return self.__facility_id

    @facility_id.setter
    def facility_id(self, new_facility_id):
        self.__facility_id = new_facility_id

    @property
    def facility_name(self):
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, new_facility_name):
        self.__facility_name = new_facility_name

    def __str__(self):
        return f"Facility(ID: {self.__facility_id}, Name: {self.__facility_name})"
