from __future__ import annotations
import pandas as pd

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

    # Uses Story Vis 1
    def get_stays_per_room_type(self) -> pd.DataFrame:
        #TODO: Die anzahl der Zimmer pro Zimmertyp ebenfalls übergeben, damit dann eine Besuchsrate unabhängig vom Vorkommen der Zimmer gebildet werden kann.
        sql = """ 
        SELECT 
            rt.type_id, 
            rt.description, 
            SUM(JULIANDAY(b.check_out_date) - JULIANDAY(b.check_in_date)) AS stays
        FROM Booking b
        JOIN Room r ON b.room_id = r.room_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE b.is_cancelled = 0
        GROUP BY rt.type_id
        """
        params = tuple()
        df = pd.read_sql(sql, self._connect(), params=params) #würde auch mit fetchall funktionieren, jedoch haben wir keine Inputparameter, daher ist read besser
        if df is None:
            print("Fehler: Kein DataFrame zurückgegeben!")
        return df