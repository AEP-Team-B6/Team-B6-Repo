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

#Creating class Invoice
class Invoice:
    def __init__(invoice_id:int, booking:Booking, issue_date:datetime, total_amount:float):
        self.__invoice_id = invoice_id
        self.__booking = booking
        self.__issue_date = issue_date
        self.__total_amount = total_amount

    @property
    def invoice_id(self):
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, new_invoice_id):
        self.__invoice_id = new_invoice_id

    @property
    def booking(self) -> Booking:
        return self.__booking

    @booking.setter
    def booking(self, new_booking:Booking):
        if not isinstance(new_booking, Booking):
            raise TypeError("booking must be an instance of Booking")
        self.__booking = new_booking

    @property
    def issue_date(self):
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, new_issue_date):
        self.__issue_date = new_issue_date

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, new_total_amount):
        self.__total_amount = new_total_amount
