import os

import model
import data_access
from model.address import Address

class AddressManager:
    def __init__(self) -> None:
        self.__address_da = data_access.AddressDataAccess()


    #Used in User Story 1.6
    def read_address_by_id(self, address_id:int):
        return self.__address_da.read_address_by_id(address_id)
    
    #Userstory 3.1
    def create_address(self, address: Address):
        return self.__address_da.add_address(address)