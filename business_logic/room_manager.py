import os

import model
import data_access
from model import Room

class RoomManager:
    def __init__(self) -> None:
        self.__room_da = data_access.RoomDataAccess()

        
    # User Story 9
    def read_room_details(self):
        return self.__room_da.get_room_details()
