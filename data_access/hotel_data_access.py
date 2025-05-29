from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess


class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

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
        