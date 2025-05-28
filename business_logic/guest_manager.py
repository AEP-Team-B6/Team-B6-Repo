import os

import model
import data_access

class GuestManager:
    def __init__(self) -> None:
        self.__guest_da = GuestDataAccess()