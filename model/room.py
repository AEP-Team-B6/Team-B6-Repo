#Creating class Room
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: #WICHTIG: alle Imports in diesem IF schreiben, da so verhindert wird, dass wenn man in file A, file B importiert und in file B, file A importiert es eine Schlaufe gibt.
    from room_type import Room_Type 
    from hotel import Hotel 
    from facility import Facility


class Room:
    def __init__(self, room_id:int, room_number:int, price_per_night:float, room_type:Room_Type, hotel:Hotel, price_per_night_ls:float):
        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__room_type = room_type  # Fixiert: Nutzt den Parameter room_type anstelle von Room_Type
        self.__hotel = hotel
        self.__price_per_night_ls = price_per_night_ls
        self.__room_facility: list[Facility] = []

    @property
    def room_id(self) -> int:
        return self.__room_id

    @room_id.setter
    def room_id(self, new_room_id: int):
        self.__room_id = new_room_id

    @property
    def room_number(self) -> int:
        return self.__room_number

    @room_number.setter
    def room_number(self, new_room_number: int):
        self.__room_number = new_room_number

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, new_price: float):
        self.__price_per_night = new_price

    @property 
    def room_type(self) -> Room_Type:
        return self.__room_type

    @room_type.setter
    def room_type(self, new_room_type:Room_Type):
        if not isinstance(new_room_type, Room_Type):
            raise TypeError("room_type muss vom Typ Room_Type sein")
        self.__room_type = new_room_type

    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @hotel.setter
    def hotel(self, new_hotel:Hotel):
        if not isinstance(new_hotel, Hotel):
            raise TypeError("hotel muss vom Typ Hotel sein")
        self.__hotel = new_hotel

    @property
    def price_per_night_ls(self) -> float:
        return self.__price_per_night_ls

    @price_per_night_ls.setter
    def price_per_night_ls(self, new_price_ls: float):
        self.__price_per_night_ls = new_price_ls

    @property
    def room_facility(self) -> list[Facility]:
        return self.__room_facility

    @room_facility.setter
    def room_facility(self, room_facility: list[Facility]):
        self.__room_facility = room_facility
    
    #Used in User Story 9 
    # Fügt eine Ausstattung (Facility) zum Raum hinzu.
    # Diese Methode gehört in die Room-Klasse, da sie das Verhalten und den Zustand des Objekts verändert
    # und nicht mit der Datenbank kommuniziert. Sie ist Teil der Geschäftslogik und unterstützt die Kapselung.
    def add_facility(self, facility: Facility):
        self.__room_facility.append(facility)
