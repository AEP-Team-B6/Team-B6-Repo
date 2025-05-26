#Creating class Room_Facility
from __future__ import annotations

class Room_Facility:
    def __init__(self, room: Room, facility: Facility):
        self.__room = room
        self.__facility = facility

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, room: Room):
        self.__room = room

    @property
    def facility(self):
        return self.__facility

    @facility.setter
    def facility(self, facility: Facility):
        self.__facility = facility
