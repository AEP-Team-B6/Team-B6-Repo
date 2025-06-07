from __future__ import annotations
from datetime import date, datetime
from model import review
from data_access.base_data_access import BaseDataAccess
import sqlite3 

#bim str fehlt es None, ha de fehler nonig entdeckt
class ReviewDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = ""):
        super().__init__(db_path)
    
    
    def write_review(self, review_id: int, rating: int, booking_id: int, hotel_id: int, comment: str, date: date):
        sql= """
            INSERT INTO reviews (review_id, rating, booking_id, hotel_id, comment, date)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        params=(
           review_id,
            rating,
            booking_id,
            hotel_id,
            comment,
            date
        )
        self.execute(sql, params)