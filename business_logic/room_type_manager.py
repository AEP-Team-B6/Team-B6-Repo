import os

import model
import data_access

class RoomTypeManager:
    def __init__(self) -> None:
        self.__roomtype_da = data_access.RoomTypeDataAccess()


    # Used in User Story 10
    def update_room_type(self, id, attribute, new_value):
        return self.__roomtype_da.update_room_type(id, attribute, new_value)

        