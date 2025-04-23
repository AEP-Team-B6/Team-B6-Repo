from datetime import datetime, date

#Creating class Booking
class Booking:
    def __init__(self, booking_id:int, guest:Guest, room:Room,check_in_date:datetime, check_out_date:datetime, is_cancelled:bool, total_amount:float):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount

    @property
    def booking_id(self):
        return self.__booking_id

    @booking_id.setter
    def booking_id(self, new_booking_id):
        self.__booking_id = new_booking_id

    @property
    def guest(self) -> Guest:
        return self.__guest

    @guest.setter
    def guest(self, new_guest:Guest):
        if not isinstance(new_guest, Guest):
            raise TypeError("guest must be an instance of Guest")
        self.__guest = new_guest

    @property
    def room(self) -> Room:
        return self.__room

    @room.setter
    def room(self, new_room:Room):
        if not isinstance(new_room, Room):
            raise TypeError("room must be an instance of Room")
        return self.__room

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, new_check_in_date):
        self.__check_in_date = new_check_in_date

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, new_check_out_date):
        self.__check_out_date = new_check_out_date

    @property
    def is_cancelled(self):
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, new_is_cancelled):
        self.__is_cancelled = new_is_cancelled

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, new_total_amount):
        self.__total_amount = new_total_amount
