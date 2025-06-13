from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: #WICHTIG: alle Imports in diesem IF schreiben, da so verhindert wird, dass wenn man in file A, file B importiert und in file B, file A importiert es eine Schlaufe gibt.
    pass #from klassenfile import Klasse


class Address:
    def __init__(self, address_id: int, street: str, zip_code: int, city: str):
        self.__address_id = address_id
        self.__street = street
        self.__zip_code = zip_code
        self.__city = city
        
    @property
    def address_id(self) -> int:
        return self.__address_id

    @address_id.setter
    def address_id(self, new_address_id: int):
        self.__address_id = new_address_id

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, new_street: str):
        self.__street = new_street

    @property
    def zip_code(self) -> int:
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, new_zip_code: int):
        self.__zip_code = new_zip_code

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, new_city: str):
        self.__city = new_city
