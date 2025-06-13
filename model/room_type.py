#Creating class Room_Type
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: #WICHTIG: alle Imports in diesem IF schreiben, da so verhindert wird, dass wenn man in file A, file B importiert und in file B, file A importiert es eine Schlaufe gibt.
    pass #from klassenfile import Klasse


class Room_Type:
    def __init__(self, type_id:int, description:str, max_guests:int):
        self.__type_id = type_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def type_id(self) -> int:
        return self.__type_id

    @type_id.setter
    def type_id(self, new_type_id: int):
        self.__type_id = new_type_id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description: str):
        self.__description = new_description

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, new_max_guests: int):
        self.__max_guests = new_max_guests
