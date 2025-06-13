Invoice Manager

import os

from model.invoice import Invoice
import data_access

class InvoiceManager:
    def __init__(self) -> None:
        self.__invoice_da = data_access.InvoiceDataAccess()

    def create_invoice(self, invoice: Invoice) -> int:
        return self.__invoice_da.create_invoice(invoice)

    def cancel_invoice(self, invoice_id: int):
        """Storniert eine Rechnung."""
        self.__invoice_da.cancel_invoice(invoice_id)

    def get_invoice_by_booking_id(self, booking_id: int) -> Invoice | None:
            return self.__invoice_da.get_invoice_by_booking_id(booking_id)
