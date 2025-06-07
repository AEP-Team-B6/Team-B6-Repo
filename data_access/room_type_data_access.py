from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess


class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


    # Used in User Story 10
    def update_room_type(self, id:int, attribute:str, new_value):
        sql = f"""
        UPDATE Room_Type SET {attribute} = ? WHERE type_id = ?
        """
        self.execute(sql, (new_value, id))