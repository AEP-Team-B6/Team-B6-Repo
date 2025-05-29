from __future__ import annotations

from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess
from model import Hotel


class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

#User Story 1.6
    def get_all_hotels(self) -> list[Hotel]:
        sql = """
        SELECT hotel_id, name, stars, address_id FROM Hotel
        """
        rows = self.fetchall(sql)

        address_da = AddressDataAccess()

        hotels = []
        for hotel_id, name, stars, address_id in rows:
            address = address_da.read_address_by_id(address_id)
            hotels.append(Hotel(hotel_id, name, stars, address, rooms=[]))  #TODO rooms später befüllen wird in US 1.6 nicht benötigt
        return hotels