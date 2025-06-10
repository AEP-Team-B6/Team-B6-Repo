from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess
from model import Booking
from model import Guest
from model import Room
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

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


    # Used in User Story 4
    def create_new_booking(self, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount) -> Booking:
        sql = """
        INSERT into Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, ?, ?) 
        """

        params = tuple([guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount])

        last_row_id, _ = self.execute(sql, params)

        return last_row_id
    

    # Used in User Story 8
    def get_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking
        """

        rows = self.fetchall(sql)
        return [
            Booking(booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
            for booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount in rows
            ]
    

    # Used in User Story 2.1 DB
    def get_booking_by_guest_id(self, guest_id:int) -> list[Booking]:

        sql = """
        SELECT 
            booking_id, 
            guest_id, 
            room_id, 
            check_in_date, 
            check_out_date, 
            is_cancelled, 
            total_amount 
        FROM Booking 
        WHERE guest_id = ?
        """
        params = ([guest_id])
        result = self.fetchall(sql, params)
        if result:        
            l_rooms = []
            l_guests = []
            l_bookings = []
            for row in result: #TODO Listcomprahension
                booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount = row #tuple unpacking
                #create Room Object with room_id in it
                room = Room(room_id=room_id, room_number=None, price_per_night=None, room_type=None, hotel=None)
                #create Guest Object with guest_id in it
                guest = Guest(guest_id=guest_id, first_name=None, last_name=None, email=None, address=None, bookings=None)
                #create Booking Object with guest and room and append to Bookings list                
                booking = Booking(booking_id=booking_id, 
                                  guest=guest, room=room, 
                                  check_in_date=check_in_date, 
                                  check_out_date=check_out_date, 
                                  is_cancelled=is_cancelled, 
                                  total_amount=total_amount)
                l_bookings.append(booking)
            return l_bookings


    # Used in User Story 2.1 DB #TODO Check ob redundant US 4
    def create_booking(self, booking:Booking) -> int:
        iso_start_date = date_to_db(booking.check_in_date)
        iso_end_date = date_to_db(booking.check_out_date)
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (booking.guest.guest_id, booking.room.room_id, iso_start_date, iso_end_date, booking.is_cancelled, booking.total_amount)
        self.execute(sql,params)

        sql = """
        SELECT MAX(booking_id) FROM Booking
        """
        booking_id = self.fetchone(sql)[0]
        return booking_id
    

    # Used in User Story 2.1 DB
    def update_booking(self, booking:Booking) -> Booking:
        if booking.check_in_date is not None:
            iso_start_date = date_to_db(booking.check_in_date)
            iso_end_date = date_to_db(booking.check_out_date)
        else:
            iso_start_date = None
            iso_end_date = None
            
        sql = """
        UPDATE Booking
        SET
            guest_id        = CASE WHEN ? IS NOT NULL THEN ? ELSE guest_id END,
            room_id         = CASE WHEN ? IS NOT NULL THEN ? ELSE room_id END,
            check_in_date   = CASE WHEN ? IS NOT NULL THEN ? ELSE check_in_date END,
            check_out_date  = CASE WHEN ? IS NOT NULL THEN ? ELSE check_out_date END,
            is_cancelled    = CASE WHEN ? IS NOT NULL THEN ? ELSE is_cancelled END,
            total_amount    = CASE WHEN ? IS NOT NULL THEN ? ELSE total_amount END
        WHERE booking_id = ?;
        """

        params = tuple([
            booking.guest.guest_id, booking.guest.guest_id,
            booking.room.room_id, booking.room.room_id,
            booking.check_in_date, booking.check_in_date,
            booking.check_out_date, booking.check_out_date,
            booking.is_cancelled, booking.is_cancelled,
            booking.total_amount, booking.total_amount,
            booking.booking_id])

        self.execute(sql, params)
        
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking WHERE booking_id = ?
        """
        params = tuple([booking.booking_id])
        result = self.fetchall(sql, params)

        if result:    
            booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount = result[0]          
            guest = Guest(guest_id=guest_id, first_name=None, last_name=None, email=None, address=None, bookings=None)
            room = Room(room_id=room_id, room_number=None, price_per_night=None, room_type=None, hotel=None)
            updated_booking = Booking(booking_id=booking_id, guest=guest, room=room, check_in_date=check_in_date, check_out_date=check_out_date, is_cancelled=is_cancelled, total_amount=total_amount)
            return updated_booking
        
        else:
            raise BrokenPipeError #TODO möglicherweise nicht genau passender Error, selber ein Error dafür schreiben     