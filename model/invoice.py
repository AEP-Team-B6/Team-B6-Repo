#Creating class Invoice
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: #WICHTIG: alle Imports in diesem IF schreiben, da so verhindert wird, dass wenn man in file A, file B importiert und in file B, file A importiert es eine Schlaufe gibt.
    from datetime import date, datetime
    from booking import Booking

# Definierte Statuswerte der Rechnung
Status = {"Offen", "Bezahlt", "Storniert"}


class Invoice:
    def __init__(self,invoice_id: int, booking:Booking, issue_date:datetime, total_amount:float, invoice_status: str):
        if invoice_status not in Status:
            raise ValueError("Ungueltiger Rechnungsstatus!")
        self.__invoice_id = invoice_id
        self.__booking = booking
        self.__issue_date = issue_date
        self.__total_amount = total_amount
        self.__invoice_status = invoice_status

    @property
    def invoice_id(self) -> int:
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, new_invoice_id: int):
        self.__invoice_id = new_invoice_id

    @property
    def booking(self) -> Booking:
        return self.__booking

    @booking.setter
    def booking(self, new_booking:Booking):
        if not isinstance(new_booking, Booking):
            raise TypeError("booking muss vom Typ Booking sein")
        self.__booking = new_booking

    @property
    def issue_date(self) -> date:
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, new_issue_date: date):
        self.__issue_date = new_issue_date

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, new_total_amount: float):
        self.__total_amount = new_total_amount

    @property
    def invoice_status(self) -> str:
        return self.__invoice_status

    @invoice_status.setter
    def invoice_status(self, new_status: str):
        if new_status not in Status:
            raise ValueError("Ungueltiger Rechnungsstatus!")
        self.__invoice_status = new_status