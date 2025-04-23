#Creating class Hotel

class Hotel:
    def __init__(self, hotel_id:int, name:str, stars:int, address:Address, rooms:Room):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address = address
        self.__rooms = rooms

    @property
    def hotel_id(self):
        return self.__hotel_id

    @hotel_id.setter
    def hotel_id(self, new_hotel_id):
        self.__hotel_id = new_hotel_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, new_stars):
        self.__stars = new_stars

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def address(self, new_address:Address):
        if not isinstance(new_address, Address):
            raise TypeError("address must be an instance of Address")
        self.__address = new_address

    @property
    def rooms(self) -> Room:
        return self.__rooms

    @rooms.setter
    def rooms(self, new_rooms:Room):
        if not isinstance(new_rooms, Room):
            raise TypeError("room must be an instance of Room")
        self.__rooms = new_rooms
