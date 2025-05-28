import os

import model
import data_access

class FacilityManager:
    def __init__(self) -> None:
        self.__facility_da = FacilityDataAccess()