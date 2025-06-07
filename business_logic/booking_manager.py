import os

import model
import data_access
from model import Booking
from model import Guest
from model import Room

class BookingManager:
    def __init__(self) -> None:
        self.__booking_da = data_access.BookingDataAccess()

    # User Story 8
    def read_all_bookings(self):
        return self.__booking_da.get_all_bookings()
    

    # User Story DB 2.1
    def get_booking_by_guest_id(self, guest_id:int) -> list[Booking]:
        return self.__booking_da.get_booking_by_guest_id(guest_id)
    
    # User Story DB 2.1
    def create_booking(self, booking:Booking) -> int: #Erwartet Booking objekt, gibt neue booking_id zurück
        return self.__booking_da.create_booking(booking)
    
    # User Story DB 2.1
    def update_booking(self, booking:Booking) -> Booking: #Erwartet Booking objekt, gibt booking Objekt mit aktualisierten Werten zurück
        return self.__booking_da.update_booking(booking)
    
