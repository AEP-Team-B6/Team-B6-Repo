from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: #WICHTIG: alle Imports in diesem IF schreiben, da so verhindert wird, dass wenn man in file A, file B importiert und in file B, file A importiert es eine Schlaufe gibt.
    from address import Address
    from booking import Booking

class Guest:
    def __init__(self, guest_id:int, first_name:str, last_name:str, email:str, address:Address, bookings:list[Booking]):
        self.__guest_id = guest_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__address = address
        self.__bookings = bookings

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @guest_id.setter
    def guest_id(self, new_guest_id: int):
        self.__guest_id = new_guest_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name: str):
        self.__first_name = new_first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name: str):
        self.__last_name = new_last_name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, new_email: str):
        self.__email = new_email

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def address(self, new_address:Address):
        if not isinstance(new_address, Address):
            raise TypeError("address muss vom Typ Address sein")
        self.__address = new_address

    @property
    def bookings(self) -> list[Booking]:
        return self.__bookings

    @bookings.setter
    def bookings(self, new_bookings: list[Booking]):
        if not isinstance(new_bookings, list) or not all(isinstance(b, Booking) for b in new_bookings):
            raise TypeError("bookings muss eine Liste von Booking-Objekten sein")
        self.__bookings = new_bookings
