#Creating class Guest
class Guest:
    def __init__(self, guest_id:int, first_name:str, last_name:str, email:str, address:Address, bookings:list[Booking]):
        self.__guest_id = guest_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__address = address
        self.__bookings = bookings

    @property
    def guest_id(self):
        return self.__guest_id

    @guest_id.setter
    def guest_id(self, new_guest_id):
        self.__guest_id = new_guest_id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self.__first_name = new_first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def address(self, new_address:Address):
        if not isinstance(new_address, Address):
            raise TypeError("address must be an instance of Address")
        self.__address = new_address

    @property
    def bookings(self) -> list[Booking]:
        return self.__bookings

    @bookings.setter
    def bookings(self, new_bookings:Booking):
        if not isinstance(new_bookings, Booking):
            raise TypeError("bookings must be an instance of Bookings")
        self.__bookings = new_bookings
