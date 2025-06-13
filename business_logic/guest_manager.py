import data_access


class GuestManager:
    def __init__(self) -> None:
        self.__guest_da = data_access.GuestDataAccess()


    # Used in User Story 4
    def read_all_guests(self):
        """Liest alle Gaeste aus dem System (z. B. zur Auswahl bei Buchung)."""
        return self.__guest_da.get_all_guests()
    
    # Used in User Story 10
    def update_guest(self, id, attribute, new_value):
        """Aktualisiert einen Gast anhand eines Attributs und Werts."""
        return self.__guest_da.update_guest(id, attribute, new_value)