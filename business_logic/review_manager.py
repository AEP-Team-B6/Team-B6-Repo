from model.review import Review
from data_access.review_data_access import ReviewDataAccess
from data_access.booking_data_access import BookingDataAccess
from data_access.hotel_data_access import HotelDataAccess

class ReviewManager:
    def __init__(self):
        self.review_da = ReviewDataAccess()
        self.booking_da = BookingDataAccess()
        self.hotel_da = HotelDataAccess()

    def submit_review(self,review: Review):
        booking = self.booking_da.get_booking_by_id(booking_id)
        hotel = self.hotel_da.get_hotel_by_id(hotel_id)

        if not self._has_booking(booking, hotel_id: int):
            raise Exception("Gast hat kein Booking für dieses Hotel.")


        review_id = self.__generate_review_id()
        review = Review(review_id, rating, booking_id, hotel_id, comment)

        booking.add_review(review)
        hotel.add_review(review)

        self.review_da.save(review)
        self.booking_da.update(booking)
        self.hotel_da.update(hotel)

        return review

    def _has_booking(self, booking, hotel_id: int) -> bool:
        return booking.hotel_id == hotel_id
