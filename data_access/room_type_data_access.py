from __future__ import annotations
import pandas as pd

from data_access.base_data_access import BaseDataAccess


class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # Used in User Story 10
    def update_room_type(self, id:int, attribute:str, new_value):
        """Aktualisiert ein Attribut eines Zimmertyps anhand der ID."""
        # Hinweis: Attribut wurde im Input bereits validiert.
        
        sql = f"""
        UPDATE Room_Type SET {attribute} = ? WHERE type_id = ?
        """
        self.execute(sql, (new_value, id))

    # Used in User Story Vis 1
    def get_stays_per_room_type(self) -> pd.DataFrame:
        """
        Gibt die Gesamtzahl der gebuchten Naechte pro Zimmertyp zurueck.
        Hinweis: Die Zahl der verfuegbaren Zimmertypen fehlt aktuell (siehe TODO).
        """
        # TODO: Anzahl der Zimmer pro Zimmertyp ebenfalls abfragen, um Aufenthaltsrate zu berechnen.
        
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
        params = ()
        df = pd.read_sql(sql, self._connect(), params=params) # Würde auch mit fetchall funktionieren, jedoch haben wir keine Inputparameter, daher ist read besser
        if df is None:
            print("Fehler: Kein DataFrame zurückgegeben!")
        return df