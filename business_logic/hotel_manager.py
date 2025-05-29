import os

import model
import data_access

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()

    def find_hotel_by_city(self, city: str) -> None:
        return self.__hotel_da.find_hotel_by_city(city)