from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess
from model import Booking

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 8
    def get_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking
        """

        rows = self.fetchall(sql)
        return [
            Booking(booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
            for booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount in rows
            ]