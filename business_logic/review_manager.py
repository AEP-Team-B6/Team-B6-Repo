from model.review import Review
from data_access.review_data_access import ReviewDataAccess
from data_access.booking_data_access import BookingDataAccess
from data_access.hotel_data_access import HotelDataAccess


class ReviewManager:
    def __init__(self):
        self.review_da = ReviewDataAccess()
        self.booking_da = BookingDataAccess()
        self.hotel_da = HotelDataAccess()


    # Used in User Story DB 3
    def submit_review(self, review: Review):
        """
        Uebermittelt eine neue Bewertung und prueft vorher,
        ob der Gast eine gueltige Buchung fuer das Hotel hat.
        """
        booking = review.booking

        if not self._has_booking(booking, review.hotel.hotel_id):
            raise Exception("Gast hat keine Buchung für dieses Hotel.")

        review.review_id = self.new_review_id()

        booking.add_review(review)
        review.hotel.add_review(review)

        self.review_da.write_review(review)

        return review

    # Used in User Story DB 3
    def _has_booking(self, booking, hotel_id: int) -> bool:
        """Prueft, ob das Booking zum gegebenen Hotel gehoert."""
        return booking.room.hotel.hotel_id == hotel_id

    # Used in User Story DB 3
    def new_review_id(self) -> int:
        """Generiert eine neue Review-ID."""
        return self.review_da.get_new_review_id()