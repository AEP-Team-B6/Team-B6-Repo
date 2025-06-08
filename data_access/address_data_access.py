from __future__ import annotations

from data_access.base_data_access import BaseDataAccess
from model import Address

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

#Used in User Story 1.6
    def read_address_by_id(self, address_id) -> Address | None:

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
        
#User Story 3.1
    def add_address(self, address: Address) -> int:
        sql = """
        INSERT INTO Address (street, zip_code, city)
        VALUES (?, ?, ?)
        """
        params = (
            address.street,
            address.zip_code,
            address.city,
        )

        address_id, _ = self.execute(sql, params)
        sql = """
        SELECT MAX(address_id) FROM Address
        """
        address_id = self.fetchone(sql)[0]
        return address_id


#User Story 3.2
    def delete_address(self, address_id: int) -> bool:
        sql = "DELETE FROM Address WHERE address_id = ?"
        params = (address_id,)
        result = self.execute(sql, params)
        return result[0] > 0