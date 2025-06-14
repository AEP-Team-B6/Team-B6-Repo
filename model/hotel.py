#Creating class Hotel
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: #WICHTIG: alle Imports in diesem IF schreiben, da so verhindert wird, dass wenn man in file A, file B importiert und in file B, file A importiert es eine Schlaufe gibt.
    from address import Address
    from room import Room
    from review import Review

class Hotel:
    def __init__(self, hotel_id:int, name:str, stars:int, address:Address, rooms: list[Room], reviews: list[Review]):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address = address
        self.__rooms = rooms if rooms else []
        self.__reviews = reviews if reviews else []

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @hotel_id.setter
    def hotel_id(self, new_hotel_id: int):
        self.__hotel_id = new_hotel_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, new_stars: int):
        self.__stars = new_stars

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def address(self, new_address:Address):
        if not isinstance(new_address, Address):
            raise TypeError("address muss vom Typ Address sein")
        self.__address = new_address

    @property
    def rooms(self) -> list[Room]:
        return self.__rooms

    @rooms.setter
    def rooms(self, new_rooms: list[Room]):
        if not isinstance(new_rooms, list) or not all(isinstance(r, Room) for r in new_rooms):
            raise TypeError("rooms muss eine Liste von Room-Objekten sein")
        self.__rooms = new_rooms

    @property
    def reviews(self) -> list[Review]:
        return self.__reviews
    
    @reviews.setter
    def reviews(self, new_reviews: list[Review]):
        if not isinstance(new_reviews, list) or not all(isinstance(r, Review) for r in new_reviews):
            raise TypeError("reviews muss eine Liste von Review-Objekten sein")
        self.__reviews = new_reviews

    def add_review(self, review: Review):
        """Fügt dem Hotel eine neue Bewertung hinzu."""
        self.__reviews.append(review)