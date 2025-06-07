from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess


class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


    # Used in User Story 10
    def update_guest(self, id:int, attribute:str, new_value):
        sql = f"""
        UPDATE Guest SET {attribute} = ? WHERE guest_id = ?
        """
        self.execute(sql, (new_value, id))