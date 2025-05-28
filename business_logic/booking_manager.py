import os

import model
import data_access

class BookingManager:
    def __init__(self) -> None:
        self.__booking_da = BookingDataAccess()