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
    
    
    #User Story 1.1
    def find_hotel_by_city(self, city: str) -> list[hotel]| None:
        if city is None:
            raise ValueError("Please enter a City")

        sql = """
        SELECT h.hotel_id, h.name, h.stars FROM Hotel h 
        JOIN Address a ON h.address_id = a.address_id
        where a.city = ?
        """
        params = tuple([city])
        result = self.fetchall(sql, params)
        if result:        
            l_hotels = []
            for row in result:
                hotel_id, name, stars = row #tuple unpacking
                hotel = model.Hotel(hotel_id=hotel_id, name=name, stars=stars, address=None, rooms=None)
                l_hotels.append(hotel)
            return l_hotels

        else:
            return None