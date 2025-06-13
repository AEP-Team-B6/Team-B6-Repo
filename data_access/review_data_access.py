from __future__ import annotations
from datetime import date
from model import Review
from data_access.base_data_access import BaseDataAccess


class ReviewDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
    
    # Used in User Story DB 3
    def write_review(self, review: Review):
        """Schreibt eine neue Bewertung in die Datenbank."""
        sql = """

            INSERT INTO Review
            (review_id,
            rating,
            booking_id,
            hotel_id,
            comment,
            date)

            VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (

            review.review_id,
            review.rating,
            review.booking.booking_id,
            review.hotel.hotel_id,
            review.comment,
            date.today()

        )

        self.execute(sql, params)
    
    # Used in User Story DB 3
    def get_new_review_id(self) -> int:
        """Ermittelt die naechste freie Review-ID (auto-increment simuliert)."""
        sql = "SELECT MAX(review_id) FROM Review"
        result = self.fetchone(sql)
        return (result[0] + 1) if result and result[0] is not None else 1