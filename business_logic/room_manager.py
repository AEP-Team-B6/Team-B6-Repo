import os

import model
import data_access

class RoomManager:
    def __init__(self) -> None:
        self.__room_da = data_access.RoomDataAccess()