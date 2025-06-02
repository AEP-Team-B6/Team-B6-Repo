from __future__ import annotations

from data_access.base_data_access import BaseDataAccess
from data_access.room_facility_data_access import RoomFacilityDataAccess
from data_access.facility_data_access import FacilityDataAccess
from data_access.hotel_data_access import HotelDataAccess
from model import Room
from model import Room_Type
from model import Hotel


class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


    # User Story 9
    def get_room_details(self) -> list[Room]:
        sql = """
        SELECT Room.room_id, room_number, price_per_night, Room.type_id, hotel_id, description, max_guests FROM Room
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        """

        rows = self.fetchall(sql)

        roomfacility_da = RoomFacilityDataAccess()
        facility_da = FacilityDataAccess()
        hotel_da = HotelDataAccess()

        rooms = []
        for room_id, room_number, price_per_night, type_id, hotel_id, description, max_guests in rows:
            room_type = Room_Type(type_id, description, max_guests)
            hotel = hotel_da.get_hotel_by_id(hotel_id)
            
            room = Room(room_id, room_number, price_per_night, room_type, hotel)

            facility_ids = roomfacility_da.get_facility_ids_by_room(room_id)
            for fid in facility_ids:
                facility = facility_da.get_facility_by_id(fid)
                if facility:
                    room.add_facility(facility)  # Diese Methode solltest du im Room-Modell haben

            rooms.append(room)

        return rooms 