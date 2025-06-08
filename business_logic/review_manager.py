from model.review import Review
from data_access.review_data_access import ReviewDataAccess
from data_access.booking_data_access import BookingDataAccess
from data_access.hotel_data_access import HotelDataAccess

class ReviewManager:
    def __init__(self):
        self.review_da = ReviewDataAccess()
        self.booking_da = BookingDataAccess()
        self.hotel_da = HotelDataAccess()

    def submit_review(self, review: Review):
        booking = review.booking
        hotel = review.hotel

        if not self._has_booking(booking, hotel.hotel_id):
            raise Exception("Gast hat kein Booking für dieses Hotel.")

        review.review_id = self.new_review_id()

        booking.add_review(review)
        hotel.add_review(review)

        self.review_da.write_review(review)
        self.booking_da.update(booking)
        self.hotel_da.update(hotel)

        return review

    def _has_booking(self, booking, hotel_id: int) -> bool:
        return booking.hotel.hotel_id == hotel_id

    def new_review_id(self) -> int:
        return self.review_da.get_new_review_id()
