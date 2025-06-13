import pandas as pd

import data_access


class RoomTypeManager:
    def __init__(self) -> None:
        self.__roomtype_da = data_access.RoomTypeDataAccess()


    # Used in User Story 10
    def update_room_type(self, id, attribute, new_value):
        """Aktualisiert ein Attribut eines Zimmertyps."""
        return self.__roomtype_da.update_room_type(id, attribute, new_value)

    # Userstory Vis 1
    def get_stays_per_room_type(self) -> pd.DataFrame:
        """Gibt die Anzahl Aufenthalte pro Zimmertyp als DataFrame zurueck."""
        return self.__roomtype_da.get_stays_per_room_type()
        