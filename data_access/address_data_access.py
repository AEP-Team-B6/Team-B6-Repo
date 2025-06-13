from __future__ import annotations

from data_access.base_data_access import BaseDataAccess
from model import Address


class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

# Used in User Story 1.6
    def read_address_by_id(self, address_id) -> Address | None:
        """Liefert eine Adresse anhand der ID oder None, wenn nicht vorhanden."""
        sql = """
        SELECT address_id, street, zip_code, city FROM Address WHERE address_id = ?
        """

        params = tuple([address_id])
        result = self.fetchone(sql, params)

        if result:
            address_id, street, zip_code, city = result
            return Address(address_id=address_id, street=street, zip_code=zip_code, city=city)
        else:
            return None

# Used in User Story 3.1
    def add_address(self, address: Address) -> int:
        """Fuegt eine neue Adresse hinzu und gibt die zugewiesene ID zurueck."""
        sql = """
        INSERT INTO Address (street, zip_code, city)
        VALUES (?, ?, ?)
        """
        params = (address.street, address.zip_code, address.city,)
        self.execute(sql, params)

        # Adresse-ID aus DB ermitteln (SQLite-sicher)
        sql = "SELECT MAX(address_id) FROM Address"
        address_id = self.fetchone(sql)[0]
        return address_id

# Used in User Story 3.2
    def delete_address(self, address_id: int) -> bool:
        """Loescht eine Adresse anhand der ID. Gibt True zurueck, wenn erfolgreich."""
        sql = "DELETE FROM Address WHERE address_id = ?"
        params = (address_id,)
        _, result = self.execute(sql, params)
        return result > 0


# Used in User Story 10 und 3.3
    def update_address(self, id:int, attribute:str, new_value):
        """Aktualisiert ein bestimmtes Attribut einer Adresse."""
        # Hinweis: Attribut wurde im Input bereits validiert.
        sql = f"""
        UPDATE Address SET {attribute} = ? WHERE address_id = ?
        """
        self.execute(sql, (new_value, id))