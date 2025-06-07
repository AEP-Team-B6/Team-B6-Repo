class Review:
    def __init__(self, review_id:int, rating:int, comment: str, booking: Booking, hotel: Hotel):

        if not (1<= rating <=10):
            raise ValueError("Rating must be between 1-10!")

        self.__review_id = review_id
        self.__rating = rating
        self.__comment = comment
        self.__booking = booking
        self.__hotel = hotel

    @property
    def review_id(self):
        return self.__review_id
    
    @property
    def rating(self):
        return self.__rating
    
    @property
    def comment(self):
        return self.__comment
    
    @property
    def booking(self) -> Booking:
        return self.__booking
    
    @property
    def hotel(self) -> Hotel:
        return self.__hotel
    
    @rating.setter
    def rating(self, rating: int):
        if not (1<= rating <=10):
            raise ValueError("Rating must be between 1-10!")
        self.__rating = rating

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @booking.setter
    def booking(self, booking: Booking):
        self.__booking = booking

    @hotel.setter
    def hotel(self, hotel: Hotel):
        self.__hotel = hotel