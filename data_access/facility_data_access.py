from __future__ import annotations

from data_access.base_data_access import BaseDataAccess
from model import Facility

class FacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    
    #Used in User Story 9
    def get_facility_by_id(self, facility_id) -> Facility:
        
        sql = """
        SELECT facility_id, facility_name FROM Facilities WHERE facility_id = ?    
        """

        params = tuple([facility_id])
        result = self.fetchone(sql, params)

        if result:
            facility_id, facility_name = result
            return Facility(facility_id=facility_id, facility_name=facility_name)
        else:
            return None
        
    
    # Used in User Story 10
    def update_facility(self, id:int, new_value):
        sql = """
        UPDATE Facilities SET facility_name = ? WHERE facility_id = ?
        """
        self.execute(sql, (new_value, id)) 