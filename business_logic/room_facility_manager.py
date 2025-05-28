import os

import model
import data_access

class RoomFacilityManager:
    def __init__(self) -> None:
        self.__roomfacility_da = RoomFacilityDataAccess()