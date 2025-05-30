import os
import model
from model import Hotel
import data_access

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()

    # User Story 1.1
    def find_hotel_by_city(self, city: str) -> list[Hotel]:
        return self.__hotel_da.find_hotel_by_city(city)
    
    #User Story 1.2
    def find_hotel_by_min_stars(self, min_stars: int) -> list[Hotel]:
        return self.__hotel_da.find_hotel_by_min_stars(min_stars)
    
    #User Story 1.6
    def read_all_hotels(self):
        return self.__hotel_da.get_all_hotels()
