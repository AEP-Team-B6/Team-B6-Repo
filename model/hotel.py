#Creating class Hotel
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: #WICHTIG: alle Imports in diesem IF schreiben, da so verhindert wird, dass wenn man in file A, file B importiert und in file B, file A importiert es eine Schlaufe gibt.
    from address import Address
    from room import Room
    from review import Review

class Hotel:
    def __init__(self, hotel_id:int, name:str, stars:int, address:Address, rooms:Room, reviews:Review):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address = address
        self.__rooms = rooms if rooms else []
        self.__reviews = reviews if reviews else []

    #def __str__(self): #TODO möglicherweise muss hier noch etwas gemacht werden 
    #    return f"{self.name} ({self.stars} Sterne)"

    #def __repr__(self): #TODO möglicherweise muss hier noch etwas gemacht werden 
    #    return self.__str__()

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

    def add_review(self, review: Review):
        self.__reviews.append(review)

    @property
    def reviews(self) -> list[Review]:
        return self.__reviews
