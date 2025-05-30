from __future__ import annotations

from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess
from model import Hotel
from model import Room
from model import Room_Type
import sqlite3

from datetime import date, datetime

# Adapter: Python date → str für DB
def date_to_db(d: date) -> str:
    return d.isoformat()

# Konverter: str aus DB → Python date
def db_to_date(s: bytes) -> date:
    return datetime.strptime(s.decode(), "%Y-%m-%d").date()

# Registrierung
sqlite3.register_adapter(date, date_to_db)
sqlite3.register_converter("DATE", db_to_date)


class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
 
    
    #User Story 1.1
    def find_hotel_by_city(self, city: str) -> list[Hotel]| None:
        if city is None:
            raise ValueError("Bitte geben sie die gewünschte Stadt ein")

        sql = """
        SELECT h.hotel_id, h.name, h.stars FROM Hotel h 
        JOIN Address a ON h.address_id = a.address_id
        where a.city = ?
        """
        params = tuple([city])
        result = self.fetchall(sql, params)
        if result:        
            l_hotels = []
            for row in result: #TODO Listcomprahension
                hotel_id, name, stars = row #tuple unpacking
                hotel = Hotel(hotel_id=hotel_id, name=name, stars=stars, address=None, rooms=None)
                l_hotels.append(hotel)
            return l_hotels

        else:
            return None


    #User Story 1.2
    def find_hotel_by_min_stars(self, min_stars: int) -> list[Hotel]:
        if min_stars is None:
            raise ValueError("Bitte geben Sie die gewünschte Anzahl Sterne an")

        sql = """
        SELECT hotel_id, name, stars FROM Hotel  
        where stars >= ?
        """
        params = tuple([min_stars])
        result = self.fetchall(sql, params)
        if result:        
            l_hotels = []
            for row in result: #TODO Listcomprahension
                hotel_id, name, stars = row #tuple unpacking
                hotel = Hotel(hotel_id=hotel_id, name=name, stars=stars, address=None, rooms=None)
                l_hotels.append(hotel)
            return l_hotels

        else:
            return None
        

    #User Story 1.3
    def find_hotel_by_city_and_guests(self, city_and_guests: list) -> list[Hotel]| None:
        if (city_and_guests[0] is None) or (city_and_guests[1] is None):
            raise ValueError("Bitte geben Sie die gewünschten Parameter ein")

        sql = """
        SELECT DISTINCT h.hotel_id, h.name, h.stars, r.room_id, r.room_number, rt.type_id, rt.description, rt.max_guests
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE a.city = ? AND rt.max_guests >= ?
        """
        params = tuple([city_and_guests[0], city_and_guests[1]])
        result = self.fetchall(sql, params)
        if result:        
            l_hotels = []
            l_rooms = []
            l_room_types = []
            for row in result: #TODO Listcomprahension
                hotel_id, name, stars, room_id, room_number, type_id, description, max_guests = row #tuple unpacking
                hotel = Hotel(hotel_id=hotel_id, name=name, stars=stars, address=None, rooms=None)
                l_hotels.append(hotel)
                room_type = Room_Type(type_id=type_id, description=description, max_guests=max_guests)
                l_room_types.append(room_type)
                room = Room(room_id=room_id, room_number=room_number, price_per_night=None, room_type=room_type, hotel=hotel)
                l_rooms.append(room)
            return [l_hotels, l_room_types, l_rooms]

        else:
            return None
        

    #User Story 1.4
    def find_hotel_by_city_and_time(self, city_and_time: list) -> list[Hotel]| None:
        if (city_and_time[0] is None) or (city_and_time[1] is None) or (city_and_time[2] is None):
            raise ValueError("Bitte geben Sie die gewünschten Parameter ein")

        iso_start_date = date_to_db(city_and_time[1])
        iso_end_date = date_to_db(city_and_time[2])

        sql = """
        SELECT DISTINCT 
            h.hotel_id, h.name, h.stars, 
            r.room_id, r.room_number, 
            rt.type_id, rt.description, rt.max_guests
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE a.city = ?
        AND r.room_id NOT IN (
            SELECT b.room_id FROM Booking b
            WHERE b.is_cancelled = 0
            AND b.check_out_date > ? AND b.check_in_date < ?
            )
        """
        params = tuple([city_and_time[0], iso_start_date, iso_end_date])
        result = self.fetchall(sql, params)
        if result:        
            l_hotels = []
            l_rooms = []
            l_room_types = []
            for row in result: #TODO Listcomprahension
                hotel_id, name, stars, room_id, room_number, type_id, description, max_guests = row #tuple unpacking
                hotel = Hotel(hotel_id=hotel_id, name=name, stars=stars, address=None, rooms=None)
                l_hotels.append(hotel)
                room_type = Room_Type(type_id=type_id, description=description, max_guests=max_guests)
                l_room_types.append(room_type)
                room = Room(room_id=room_id, room_number=room_number, price_per_night=None, room_type=room_type, hotel=hotel)
                l_rooms.append(room)
            return [l_hotels, l_room_types, l_rooms]

        else:
            return None
    

    #User Story 1.6
    def get_all_hotels(self) -> list[Hotel]:
        sql = """
        SELECT hotel_id, name, stars, address_id FROM Hotel
        """
        rows = self.fetchall(sql)

        address_da = AddressDataAccess()

        hotels = []
        for hotel_id, name, stars, address_id in rows: #TODO Listcomprahension
            address = address_da.read_address_by_id(address_id)
            hotels.append(Hotel(hotel_id, name, stars, address, rooms=[]))  #TODO rooms später befüllen wird in US 1.6 nicht benötigt
        return hotels