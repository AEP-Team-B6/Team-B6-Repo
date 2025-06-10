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
    
    # Used in User Story 1.2
    def find_hotel_by_city_and_min_stars(self, city_and_min_stars: list) -> list[Hotel]:
        return self.__hotel_da.find_hotel_by_city_and_min_stars(city_and_min_stars)
    
    # Used in User Story 1.3
    def find_hotel_by_city_and_guests(self, city_and_guests: list) -> list[list[Hotel], list[Room_Type], list[Room]]:
        return self.__hotel_da.find_hotel_by_city_and_guests(city_and_guests)
    
    # Used in User Story 1.4
    def find_hotel_by_city_and_time(self, city_and_time: list) -> list[list[Hotel], list[Room_Type], list[Room]]:
        return self.__hotel_da.find_hotel_by_city_and_time(city_and_time)
    
    # Used in User Story 1.5
    def find_hotel_by_search_params(self, search_params: list) -> list[list[Hotel], list[Room], list[Address], list[Room_Type]]:
        return self.__hotel_da.find_hotel_by_search_params(search_params)
    
    # Used in User Story 1.6
    def read_all_hotels(self):
        return self.__hotel_da.get_all_hotels()
    
    # Used in User Story 3.1
    def add_hotel(self, hotel: Hotel) -> int:
        return self.__hotel_da.add_hotel(
            name=hotel.name,
            address_id=hotel.address.address_id,
            stars=hotel.stars)
    
    # Used in User Story 3.2
    def delete_hotel(self, hotel_id: int) -> bool:
         return self.__hotel_da.delete_hotel(hotel_id)
    
    # Used in User Story 4
    def find_hotel_by_name_and_time(self, name_and_time: list) -> list[list[Hotel], list[Room_Type], list[Room]]:
        return self.__hotel_da.find_hotel_by_name_and_time(name_and_time)
        
    #Used in User Story 9
    def read_hotel_by_id(self, hotel_id:int):
        return self.__hotel_da.get_hotel_by_id(hotel_id)
    
    # Used in User Story 10 und 3.3
    def update_hotel(self, id, attribute, new_value):
        return self.__hotel_da.update_hotel(id, attribute, new_value)