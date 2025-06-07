import os

import model
import data_access
from model import Booking

class BookingManager:
    def __init__(self) -> None:
        self.__booking_da = data_access.BookingDataAccess()

    # User Story 8
    def read_all_bookings(self):
        return self.__booking_da.get_all_bookings()
    
    # User Story 4
    def generate_booking(self, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount):
        return self.__booking_da.create_new_booking(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)