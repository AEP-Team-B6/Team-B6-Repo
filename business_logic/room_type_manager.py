import os

import model
import data_access

class RoomTypeManager:
    def __init__(self) -> None:
        self.__roomtype_da = RoomTypeDataAccess()