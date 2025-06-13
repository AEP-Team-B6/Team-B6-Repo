from __future__ import annotations

from data_access.base_data_access import BaseDataAccess
from data_access.booking_data_access import BookingDataAccess
from model import Invoice

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # Used in User Story 5 and 6
    def create_invoice(self, invoice: Invoice) -> int:
        """Erstellt eine neue Rechnung und gibt deren ID zurück."""
        sql = """
            INSERT INTO invoice (
                booking_id,
                issue_date,
                total_amount,
                invoice_status
            ) VALUES (?, ?, ?, ?)
        """
        params = (
            invoice.booking.booking_id,
            invoice.issue_date,
            invoice.total_amount,
            invoice.invoice_status
        )
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, params)
        connection.commit()
        invoice_id = cursor.lastrowid
        connection.close()
        return invoice_id

    # Used in User Story 5 and 6
    def get_invoice_by_booking_id(self, booking_id: int) -> Invoice:
        """Liefert die Rechnung zu einer Buchung, falls vorhanden."""
        sql = "SELECT * FROM invoice WHERE booking_id = ?"
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (booking_id,))
        row = cursor.fetchone()
        connection.close()

        if row:
            invoice_id, booking_id, issue_date, total_amount, invoice_status = row  # Tuple-Unpacking
            booking = BookingDataAccess().get_booking_by_id(booking_id)
            return Invoice(
                invoice_id=invoice_id,
                booking=booking,
                issue_date=issue_date,
                total_amount=total_amount,
                invoice_status=invoice_status
            )
        else:
            return None

    # Used in User Story 6
    def update_invoice_status(self, invoice_id: int, new_status: str):
        """Aktualisiert den Status einer Rechnung (z. B. 'Bezahlt', 'Storniert')."""
        sql = "UPDATE invoice SET invoice_status = ? WHERE invoice_id = ?"
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (new_status, invoice_id))
        connection.commit()
        connection.close()

    # Used in User Story 6
    def cancel_invoice(self, invoice_id: int):
        """Setzt den Rechnungsstatus auf 'Storniert'."""
        self.update_invoice_status(invoice_id, "Storniert")