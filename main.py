# allgemeiner Teil

from datetime import date
import os

import pandas as pd # WICHTIG!!!! in VS-Terminal eingeben: py -m pip install pandas


import shutil

import model
import data_access
import business_logic
import ui
import ui.input_helper as input_helper

working_db = "./database/working_db.db"
current_db = "./database/current_db.db"

shutil.copyfile(working_db, current_db)

os.environ["DB_FILE"] = current_db


# Increase row and column display limits
pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.width", None)  # Auto-adjust display width
pd.set_option("display.max_colwidth", None)  # Show full column content


#Manager initialization (die die ihr nicht braucht auskommentieren)
address_manager = business_logic.AddressManager()
booking_manager = business_logic.BookingManager()
facility_manager = business_logic.FacilityManager()
guest_manager = business_logic.GuestManager()
hotel_manager = business_logic.HotelManager()
invoice_manager = business_logic.InvoiceManager()
room_facility_manager = business_logic.RoomFacilityManager()
room_manager = business_logic.RoomManager()
room_type_manager = business_logic.RoomTypeManager()


#TODO: Add more stuff


# Individuelle Testing -------------------

while False:
    print("test")
    # Testbereich (auf True sezten zum Testen)    









# Funktionierender Code------------------------
while True:
    print("test")
    #Funktionierende Userstories (auf False sezten zum Testen)
