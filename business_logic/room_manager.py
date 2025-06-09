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
    

    # Used in User Story 10
    def update_room(self, id, attribute, new_value):
        self.__room_da.update_room(id, attribute, new_value)


    #Used in User Story 4
    def read_room_details_by_room_number(self, room_number:int):
        return self.__room_da.get_room_details_by_room_number(room_number)
