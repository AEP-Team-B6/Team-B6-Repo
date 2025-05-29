import os
import model
import data_access

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()

    # User Story 1.1
    def find_hotel_by_city(self, city: str) -> None:
        return self.__hotel_da.find_hotel_by_city(city)
    
    #User Story 1.6
    def read_all_hotels(self):
        return self.__hotel_da.get_all_hotels()
