from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess


class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = ""):
        super().__init__(db_path)

    def create_invoice(self, invoice: Invoice) -> int:
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

    def get_invoice_by_booking_id(self, booking_id: int) -> Invoice:
        sql = "SELECT * FROM invoice WHERE booking_id = ?"
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (booking_id,))
        row = cursor.fetchone()
        connection.close()
        if row:
            from data_access.booking_data_access import BookingDataAccess
            booking = BookingDataAccess().get_booking_by_id(booking_id)
            return Invoice(
                invoice_id=row["invoice_id"],
                booking=booking,
                issue_date=row["issue_date"],
                total_amount=row["total_amount"],
                invoice_status=row["invoice_status"]
            )
        else:
            return None

    def update_invoice_status(self, invoice_id: int, new_status: str):
        sql = "UPDATE invoice SET invoice_status = ? WHERE invoice_id = ?"
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (new_status, invoice_id))
        connection.commit()
        connection.close()

    def cancel_invoice(self, invoice_id: int):
        self.update_invoice_status(invoice_id, "Storniert")