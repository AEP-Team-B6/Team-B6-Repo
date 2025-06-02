import os

import data_access

class FacilityManager:
    def __init__(self) -> None:
        self.__facility_da = data_access.FacilityDataAccess()


    # Used in User Story 9
    def read_facility_by_id(self, facility_id:int):
        return self.__facility_da.get_facility_by_id(facility_id)