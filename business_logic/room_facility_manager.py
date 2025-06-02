import os

import data_access

class RoomFacilityManager:
    def __init__(self) -> None:
        self.__roomfacility_da = data_access.RoomFacilityDataAccess()


    # Used in User Story 9
    def read_facility_ids_by_room(self, room_id:int):
        return self.__roomfacility_da.get_facility_ids_by_room(room_id)