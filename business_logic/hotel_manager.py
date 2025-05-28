import os

import model
import data_access

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = HotelDataAccess()