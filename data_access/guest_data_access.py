from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess
from data_access.address_data_access import AddressDataAccess


class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


    # Used in User Story 4
    def get_all_guests(self) -> list[model.Guest]:
        sql = """
        SELECT guest_id, first_name, last_name, email, address_id FROM Guest
        """
        rows = self.fetchall(sql)

        address_da = AddressDataAccess()

        guests = []
        for guest_id, first_name, last_name, email, address_id in rows: #TODO Listcomprahension
            address = address_da.read_address_by_id(address_id)
            guests.append(model.Guest(guest_id, first_name, last_name, email, address_id, address))
        return guests
    

    # Used in User Story 10
    def update_guest(self, id:int, attribute:str, new_value):
        sql = f"""
        UPDATE Guest SET {attribute} = ? WHERE guest_id = ?
        """
        self.execute(sql, (new_value, id))                          