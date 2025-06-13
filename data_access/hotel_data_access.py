from __future__ import annotations

from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess
from model import Hotel
from model import Room
from model import Room_Type
from model import Address
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
   
    def find_hotel_by_search_params(self, search_params: list) -> list[list[Hotel], list[Room], list[Address], list[Room_Type]] | None:
        if search_params[3] is not None:
            iso_start_date = date_to_db(search_params[3]) # Umwandeln der Daten zu ISO Format
            iso_end_date = date_to_db(search_params[4])
        else:
            iso_start_date = search_params[3] # None in die isodates einfüllen
            iso_end_date = search_params[4]

        doubled_params = []
        for val in search_params[:3]:
            doubled_params.extend([val, val])

        sql = """
        SELECT DISTINCT
            h.hotel_id, h.name, h.stars,
            r.room_id, r.room_number,
            r.price_per_night, r.price_per_night_ls,
            a.address_id, a.city,
            rt.type_id, rt.description, rt.max_guests,
            GROUP_CONCAT(f.facility_name) AS facilities
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
        LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
        WHERE (? IS NULL OR a.city = ?)
          AND (? IS NULL OR h.stars >= ?)
          AND (? IS NULL OR rt.max_guests >= ?)
          AND (
            (? IS NULL OR ? IS NULL)
            OR r.room_id NOT IN (
                SELECT b.room_id FROM Booking b
                WHERE b.is_cancelled = 0
                  AND b.check_out_date > ?
                  AND b.check_in_date < ?
            )
          )
        GROUP BY h.hotel_id, r.room_id
        """

        params = tuple([ # Übergabe Parameter für SQL
            doubled_params[0], doubled_params[1],
            doubled_params[2], doubled_params[3],
            doubled_params[4], doubled_params[5],
            iso_start_date, iso_end_date,
            iso_start_date, iso_end_date
        ])
        result = self.fetchall(sql, params)

        if result: # Falls ein Ergebniss gefunden wurde
            l_hotels = []
            l_rooms = []
            l_addresses = []
            l_room_types = []
            hotel_dict = {} #erstellen eines Dictionary für hotels

            for row in result: #entpacken des Tuples
                (hotel_id, name, stars,
                 room_id, room_number, price_per_night,
                 price_per_night_ls, address_id, city,
                 type_id, description, max_guests,
                 facilities) = row

                address = Address(address_id=address_id, street=None, zip_code=None, city=city)
                l_addresses.append(address)

                #ein Hotel-Objekt pro hotel_id erzeugen
                if hotel_id not in hotel_dict: # Wenn Hotel bereits im Dict gespeichert ist, wird es nicht nochmals erstell.
                    hotel = Hotel(hotel_id=hotel_id, name=name, stars=stars, address=address, rooms=[])
                    l_hotels.append(hotel)
                    hotel_dict[hotel_id] = hotel # speichern des Hotels im Dictionary unter der Hotel_id
                hotel = hotel_dict[hotel_id] # (wieder) abholen des der hotel_id entsprechenden Objekts

                room_type = Room_Type(type_id=type_id, description=description, max_guests=max_guests) #Raumtyp mit allen Attributen erstellen
                l_room_types.append(room_type)

                # Facilities-String von Group Concat in Liste umwandeln
                if facilities:
                    facility_list = facilities.split(',') # Verwenden der Split Funktion um aus einem String (hier mit dem Separator , ) eine Liste zu erstellen.
                else:
                    facility_list = []
                room = Room(   #Raum mit allen Attributen erstellen
                    room_id=room_id,
                    room_number=room_number,
                    price_per_night=price_per_night,
                    room_type=room_type,
                    hotel=hotel,
                    price_per_night_ls=price_per_night_ls
                )
                room.room_facility = facility_list #noch die Facilities in das Raum-Objekt speichern

                l_rooms.append(room)
                hotel.rooms.append(room)

            return [l_hotels, l_rooms, l_addresses, l_room_types]
        else:
            return None

    
    # Used in User Story 1.5
    def find_hotel_by_search_paramsXXX(self, search_params: list) -> list[list[Hotel], list[Room], list[Address], list[Room_Type]]| None:

        if search_params[3] is not None:
            iso_start_date = date_to_db(search_params[3])
            iso_end_date = date_to_db(search_params[4])
        else:
            iso_start_date = search_params[3]
            iso_end_date = search_params[4]

        doubled_params = []
        for val in search_params[:3]:   # Alles bis (und nicht mit) Position 3 der Liste verdoppeln
            doubled_params.extend([val, val])

        sql = """
        SELECT DISTINCT 
            h.hotel_id, h.name, h.stars,
            r.room_id, r.room_number, 
            a.address_id, a.city,
            rt.type_id, rt.description, rt.max_guests
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE (? IS NULL OR a.city = ?)
        AND   (? IS NULL OR h.stars >= ?)
        AND   (? IS NULL OR rt.max_guests >= ?)
        AND   (
        (? IS NULL OR ? IS NULL)
            OR r.room_id NOT IN (
                SELECT b.room_id FROM Booking b
                WHERE b.is_cancelled = 0
                AND b.check_out_date > ?
                AND b.check_in_date < ?
            )
        )
        """
        params = tuple([
            doubled_params[0], doubled_params[1], 
            doubled_params[2], doubled_params[3], 
            doubled_params[4], doubled_params[5], 
            iso_start_date, iso_end_date, 
            iso_start_date, iso_end_date])
        result = self.fetchall(sql, params)

        if result:        
            l_hotels = []
            l_rooms = []
            l_addresses = []
            l_room_types = []
            for row in result: #TODO Listcomprahension
                hotel_id, name, stars, room_id, room_number, address_id, city, type_id, description, max_guests = row #tuple unpacking
                address = Address(address_id=address_id, street=None, zip_code=None, city=city)
                l_addresses.append(address)
                hotel = Hotel(hotel_id=hotel_id, name=name, stars=stars, address=address, rooms=None)
                l_hotels.append(hotel)
                room_type = Room_Type(type_id=type_id, description=description, max_guests=max_guests)
                l_room_types.append(room_type)
                room = Room(room_id=room_id, room_number=room_number, price_per_night=None, room_type=room_type, hotel=hotel)
                l_rooms.append(room)
            return [l_hotels, l_rooms, l_addresses, l_room_types]
        
        else:
            return None

    # Used in User Story 1.6 and 4
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
    
    
    # Used in User Story 3.1
    def add_hotel(self, name:str, address_id:int, stars:int) -> int:
        sql = """
        INSERT INTO Hotel (name, address_id, stars)
        VALUES (?, ?, ?)
        """
        params = (
            name,
            address_id,
            stars,
        )
        hotel_id, _ = self.execute(sql, params)

        sql = """
        SELECT MAX(hotel_id) FROM Hotel
        """
        hotel_id = self.fetchone(sql)[0]
        return hotel_id

   
    # Used in User Story 3.2
    def delete_hotel(self, hotel_id: int) -> bool:
        sql = "DELETE FROM Hotel WHERE hotel_id = ?"
        params = (hotel_id,)
        _, result = self.execute(sql, params)
        return result > 0  
    
    
    # Used in User Story 10 und 3.3
    def update_hotel(self, id:int, attribute:str, new_value):
        sql = f"""
        UPDATE Hotel SET {attribute} = ? WHERE hotel_id = ?
        """
        self.execute(sql, (new_value, id))
    
    
    # Used in User Story 4
    def find_hotel_by_name_and_time(self, name_and_time: list) -> list[Hotel]| None:
        if (name_and_time[0] is None) or (name_and_time[1] is None) or (name_and_time[2] is None):
            raise ValueError("Bitte geben Sie die gewünschten Parameter ein")

        iso_start_date = date_to_db(name_and_time[1])
        iso_end_date = date_to_db(name_and_time[2])

        sql = """
        SELECT DISTINCT 
            h.hotel_id, h.name, h.stars, 
            r.room_id, r.room_number, 
            rt.type_id, rt.description, rt.max_guests
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON h.hotel_id = r.hotel_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE h.name = ?
        AND r.room_id NOT IN (
            SELECT b.room_id FROM Booking b
            WHERE b.is_cancelled = 0
            AND b.check_out_date > ? AND b.check_in_date < ?
            )
        """
        params = tuple([name_and_time[0], iso_start_date, iso_end_date])
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
                room = Room(room_id=room_id, room_number=room_number, price_per_night=None, room_type=room_type, hotel=hotel, price_per_night_ls=None)
                l_rooms.append(room)
            return [l_hotels, l_room_types, l_rooms]

        else:
            return None
    

    # Used in User Story 9
    def get_hotel_by_id(self, hotel_id: int) -> Hotel:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.zip_code, a.city
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE h.hotel_id = ?
        """
        result = self.fetchone(sql, (hotel_id,))
        if result:
            hotel_id, name, stars, address_id, street, zip_code, city = result
            address = Address(address_id=address_id, street=street, zip_code=zip_code, city=city)
            return Hotel(hotel_id=hotel_id, name=name, stars=stars, address=address, rooms=[])
        return None