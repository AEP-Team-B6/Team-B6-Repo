import os
import model
import data_access
from model import Hotel
from model import Room
from model import Room_Type


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()

    # User Story 1.1
    def find_hotel_by_city(self, city: str) -> list[Hotel]:
        return self.__hotel_da.find_hotel_by_city(city)
    
    #User Story 1.2
    def find_hotel_by_min_stars(self, min_stars: int) -> list[Hotel]:
        return self.__hotel_da.find_hotel_by_min_stars(min_stars)
    
    #User Story 1.3
    def find_hotel_by_city_and_guests(self, city_and_guests: list) -> list[list[Hotel], list[Room_Type], list[Room]]:
        return self.__hotel_da.find_hotel_by_city_and_guests(city_and_guests)
    
    #User Story 1.6
    def read_all_hotels(self):
        return self.__hotel_da.get_all_hotels()
