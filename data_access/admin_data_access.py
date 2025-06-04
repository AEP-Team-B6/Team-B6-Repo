#This DataAccessClass is solely built for User Story 10, it handles the change and update of master data
from __future__ import annotations

from data_access.base_data_access import BaseDataAccess


class AdminDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


# Now follow various methods that let an admin change specific master data values, the methods are linked via AdminDataManager

    def update_room_type(self, id:int, attribute:str, new_value):
        sql = f"""
        UPDATE Room_Type SET {attribute} = ? WHERE type_id = ?
        """
        self.execute(sql, (new_value, id))

    
    def update_facility(self, id:int, new_value):
        sql = """
        UPDATE Facilities SET facility_name = ? WHERE facility_id = ?
        """
        self.execute(sql, (new_value, id))


    def update_room(self, id:int, attribute:str, new_value):
        sql = f"""
        UPDATE Room SET {attribute} = ? WHERE room_id = ?
        """
        self.execute(sql, (new_value, id))


    def update_guest(self, id:int, attribute:str, new_value):
        sql = f"""
        UPDATE Guest SET {attribute} = ? WHERE guest_id = ?
        """
        self.execute(sql, (new_value, id))