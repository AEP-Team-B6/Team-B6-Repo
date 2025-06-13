#Creating class Hotel
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: #WICHTIG: alle Imports in diesem IF schreiben, da so verhindert wird, dass wenn man in file A, file B importiert und in file B, file A importiert es eine Schlaufe gibt.

    from model import Booking
    from model import Hotel

class Review:
    def __init__(self, review_id:int, rating:int, comment: str, booking: Booking, hotel: Hotel):

        if not (1<= rating <=10):
            raise ValueError("Rating must be between 1-10!")

        self.__review_id = review_id
        self.__rating = rating
        self.__comment = comment
        self.__booking = booking
        self.__hotel = hotel

    @property
    def review_id(self):
        return self.__review_id
    
    @review_id.setter
    def review_id(self, value):
        self.__review_id = value

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, rating: int):
        if not (1<= rating <=10):
            raise ValueError("Rating must be between 1-10!")
        self.__rating = rating  

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment
    
    @property
    def booking(self) -> Booking:
        return self.__booking

    @booking.setter
    def booking(self, booking: Booking):
        self.__booking = booking
    
    @property
    def hotel(self) -> Hotel:
        return self.__hotel
    
    @hotel.setter
    def hotel(self, hotel: Hotel):
        self.__hotel = hotel