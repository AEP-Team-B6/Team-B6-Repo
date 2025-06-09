import os

import model
import data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_da = data_access.GuestDataAccess()


    # Used in User Story 10
    def update_guest(self, id, attribute, new_value):
        self.__guest_da.update_guest(id, attribute, new_value)


    # Used in User Story 4
    def read_all_guests(self):
        return self.__guest_da.get_all_guests()