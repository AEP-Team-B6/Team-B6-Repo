 #Creating class Facility
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: #WICHTIG: alle Imports in diesem IF schreiben, da so verhindert wird, dass wenn man in file A, file B importiert und in file B, file A importiert es eine Schlaufe gibt.
    pass #from klassenfile import Klasse


class Facility:
    def __init__(self, facility_id: int, facility_name: str):
        self.__facility_id = facility_id
        self.__facility_name = facility_name

    @property
    def facility_id(self) -> int:
        return self.__facility_id

    @facility_id.setter
    def facility_id(self, new_facility_id: int):
        self.__facility_id = new_facility_id

    @property
    def facility_name(self) -> str:
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, new_facility_name: str):
        self.__facility_name = new_facility_name

    def __str__(self):
        """Rueckgabe der Einrichtung als formatierter String."""
        return f"Facility(ID: {self.__facility_id}, Name: {self.__facility_name})"