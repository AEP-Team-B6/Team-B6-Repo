import data_access


class FacilityManager:
    def __init__(self) -> None:
        self.__facility_da = data_access.FacilityDataAccess()


    # Used in User Story 9
    def read_facility_by_id(self, facility_id:int):
        """Liest eine Einrichtung anhand ihrer ID aus."""
        return self.__facility_da.get_facility_by_id(facility_id)

    # Used in User Story 10
    def update_facility(self, id, new_value):
        """Aktualisiert eine Einrichtung mit einem neuen Wert."""
        return self.__facility_da.update_facility(id, new_value)