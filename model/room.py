#Creating class Room
class Room:
    def __init__(self, room_id:int, room_number:int, price_per_night:float, room_type:Room_Type, hotel:Hotel):
        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__room_type = room_type  # Fixed: Use the parameter room_type instead of Room_Type
        self.__room_facility = []
        self.__hotel = hotel
    
    @property
    def room_id(self):
        return self.__room_id

    @room_id.setter
    def room_id(self, new_room_id):
        self.__room_id = new_room_id

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, new_room_number):
        self.__room_number = new_room_number

    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, new_price):
        self.__price_per_night = new_price

    @property 
    def room_type(self) -> Room_Type:
        return self.__room_type

    @room_type.setter
    def room_type(self, new_room_type:Room_Type):
        if not isinstance(new_room_type, Room_Type):
            raise TypeError("room_type must be an instance of Room_Type")
        self.__room_type = new_room_type

    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @hotel.setter
    def hotel(self, new_hotel:Hotel):
        if not isinstance(new_hotel, Hotel):
            raise TypeError("hotel must be an instance of Hotel")
        self.__hotel = new_hotel
