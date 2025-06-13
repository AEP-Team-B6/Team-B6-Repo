from model.invoice import Invoice
import data_access


class InvoiceManager:
    def __init__(self) -> None:
        self.__invoice_da = data_access.InvoiceDataAccess()

    def create_invoice(self, invoice: Invoice) -> int:
        """Erstellt eine neue Rechnung und gibt die Rechnungs-ID zurueck."""
        return self.__invoice_da.create_invoice(invoice)

    def cancel_invoice(self, invoice_id: int):
        """Storniert eine Rechnung anhand der Rechnungs-ID."""
        self.__invoice_da.cancel_invoice(invoice_id)

    def get_invoice_by_booking_id(self, booking_id: int) -> Invoice | None:
        """Liefert die Rechnung zu einer bestimmten Buchung, falls vorhanden."""
        return self.__invoice_da.get_invoice_by_booking_id(booking_id)