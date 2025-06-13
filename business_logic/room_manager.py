import data_access


class RoomManager:
    def __init__(self) -> None:
        self.__room_da = data_access.RoomDataAccess()


    # Used in User Story 4
    def read_room_details_by_room_number(self, room_number:int):
        """Liefert Details zu einem bestimmten Zimmer anhand der Zimmernummer."""
        return self.__room_da.get_room_details_by_room_number(room_number)
    
    # Used in User Story 9
    def read_room_details(self):
        """Liefert eine Liste aller Zimmer mit ihren Details."""
        return self.__room_da.get_room_details()
    
        # TODO: Festlegen, welche Detailfelder konkret zurueckgegeben werden sollen

    # Used in User Story 10
    def update_room(self, id, attribute, new_value):
        """Aktualisiert ein Attribut eines Zimmers."""
        return self.__room_da.update_room(id, attribute, new_value)