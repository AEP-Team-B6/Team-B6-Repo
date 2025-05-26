#Creating class Invoice
from __future__ import annotations

class Invoice:
    def __init__(invoice_id:int, booking:Booking, issue_date:datetime, total_amount:float):
        self.__invoice_id = invoice_id
        self.__booking = booking
        self.__issue_date = issue_date
        self.__total_amount = total_amount

    @property
    def invoice_id(self):
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, new_invoice_id):
        self.__invoice_id = new_invoice_id

    @property
    def booking(self) -> Booking:
        return self.__booking

    @booking.setter
    def booking(self, new_booking:Booking):
        if not isinstance(new_booking, Booking):
            raise TypeError("booking must be an instance of Booking")
        self.__booking = new_booking

    @property
    def issue_date(self):
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, new_issue_date):
        self.__issue_date = new_issue_date

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, new_total_amount):
        self.__total_amount = new_total_amount
