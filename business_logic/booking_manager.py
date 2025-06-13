import model
import data_access
from model import Booking, Guest, Room, Invoice
from datetime import datetime

class BookingManager:
    def __init__(self) -> None:
        self.__booking_da = data_access.BookingDataAccess()


    # Used in User Story 4
    def generate_booking(self, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount):
        """Erstellt eine neue Buchung direkt über Parameter."""
        return self.__booking_da.create_new_booking(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
    
    # Used in User Story 8
    def read_all_bookings(self):
        """Liest alle Buchungen aus dem System (Admin-Übersicht)."""
        return self.__booking_da.get_all_bookings()
    
    # Used in User Story DB 2.1 and DB 3
    def get_booking_by_guest_id(self, guest_id:int) -> list[Booking]:
        """Gibt alle Buchungen eines bestimmten Gastes zurück."""
        return self.__booking_da.get_booking_by_guest_id(guest_id)
    
    # Used in User Story DB 2.1
    def create_booking(self, booking:Booking) -> int:
        """Erstellt eine Buchung basierend auf einem Booking-Objekt. Gibt neue booking_id zurück."""
        return self.__booking_da.create_booking(booking)
    
    # Used in User Story DB 2.1
    def update_booking(self, booking:Booking) -> Booking:
        """Aktualisiert eine bestehende Buchung. Gibt aktualisiertes Booking-Objekt zurück."""
        return self.__booking_da.update_booking(booking)
    
    # Used in User Story DB 2 and 5
    def cancel_booking(self, booking_id: int):
        """Storniert eine Buchung. Wenn keine Rechnung existiert, wird automatisch eine Stornierungsrechnung erstellt."""
        self.__booking_da.cancel_booking(booking_id)

        invoice_da = data_access.InvoiceDataAccess()
        invoice = invoice_da.get_invoice_by_booking_id(booking_id)

        if not invoice:
            booking = self.__booking_da.get_booking_by_id(booking_id)
            if booking:
                storno_invoice = Invoice(
                    invoice_id=None,  # Wird von Datenbank vergeben
                    booking=booking,
                    issue_date=datetime.now(),
                    total_amount=booking.total_amount,
                    invoice_status="Storniert"
                )
                invoice_da.create_invoice(storno_invoice)