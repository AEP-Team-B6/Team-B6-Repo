import os
import model
import data_access
from model import Hotel
from model import Room
from model import Room_Type
from model import Address


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()

    # User Story 1.1
    def find_hotel_by_city(self, city: str) -> list[Hotel]:
        return self.__hotel_da.find_hotel_by_city(city)
    
    #User Story 1.2
    def find_hotel_by_city_and_min_stars(self, city_and_min_stars: list) -> list[Hotel]:
        return self.__hotel_da.find_hotel_by_city_and_min_stars(city_and_min_stars)
    
    #User Story 1.3
    def find_hotel_by_city_and_guests(self, city_and_guests: list) -> list[list[Hotel], list[Room_Type], list[Room]]:
        return self.__hotel_da.find_hotel_by_city_and_guests(city_and_guests)
    
    #User Story 1.4
    def find_hotel_by_city_and_time(self, city_and_time: list) -> list[list[Hotel], list[Room_Type], list[Room]]:
        return self.__hotel_da.find_hotel_by_city_and_time(city_and_time)
    
    #User Story 1.5
    def find_hotel_by_search_params(self, search_params: list) -> list[list[Hotel], list[Room], list[Address], list[Room_Type]]:
        return self.__hotel_da.find_hotel_by_search_params(search_params)
    
    #User Story 1.6
    def read_all_hotels(self):
        return self.__hotel_da.get_all_hotels()
    
    #Used in User Story 9
    def read_hotel_by_id(self, hotel_id:int):
        return self.__hotel_da.get_hotel_by_id(hotel_id)
    
