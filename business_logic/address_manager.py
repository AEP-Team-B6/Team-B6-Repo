import os

import model
import data_access

class AddressManager:
    def __init__(self) -> None:
        self.__address_da = data_access.AddressDataAccess()