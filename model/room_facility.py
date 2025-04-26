#Creating class Room_Facility
class Room_Facility:
    def __init__(self, room: Room, facility: Facility):
        self.__room = room
        self.__facility = facility

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, room: Room):
        self.__room = room

    @property
    def facility(self):
        return self.__facility

    @facility.setter
    def facility(self, facility: Facility):
        self.__facility = facility

#Noah - Facility
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
