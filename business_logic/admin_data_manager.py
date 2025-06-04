#This ManagerClass is solely built for User Story 10, it handles the change and update of master data
import os

import model
import data_access

class AdminDataManager:
    def __init__(self) -> None:
        self.__admin_da = data_access.AdminDataAccess()         #Constructed with same Proxy Logic
        self.supported_tables = {                               #Sets the changeable tables and attributes in a dict
            "room_type": ["description", "max_guests"],
            "facility": ["facility_name"],
            "room": ["room_number", "type_id", "price_per_night"],
            "guest": ["first_name", "last_name", "email"]
        }
    
    def update(self, table, id, attribute, new_value):    #BLL method to link the correct DA method for given input
        table = table.lower()
        if table not in self.supported_tables:            #Error handling
            raise ValueError(f"Die Tabelle {table} wird nicht unterstützt.")
        
        if attribute not in self.supported_tables[table]: #Error handling
            raise ValueError(f"Das Attribut {attribute} in Tabelle {table} ist nicht änderbar.")
        
        #Now linking to the corresponding DA method from the admin input "table"
       
        if table == "room_type":
            self.__admin_da.update_room_type(id, attribute, new_value)

        if table == "facility":
            self.__admin_da.update_facility(id, new_value)

        if table == "room":
            self.__admin_da.update_room(id, attribute, new_value)
            
        if table == "guest":
            self.__admin_da.update_guest(id, attribute, new_value)