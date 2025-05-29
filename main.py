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

hotel_reservation_sample = "./database/hotel_reservation_sample.db"
current_db = "./database/current_db.db"

shutil.copyfile(hotel_reservation_sample, current_db)

os.environ["DB_FILE"] = current_db


# Increase row and column display limits
pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.width", None)  # Auto-adjust display width
pd.set_option("display.max_colwidth", None)  # Show full column content


#Manager initialization (die die ihr nicht braucht auskommentieren)
address_manager = business_logic.AddressManager()
#booking_manager = business_logic.BookingManager()
#facility_manager = business_logic.FacilityManager()
#guest_manager = business_logic.GuestManager()
hotel_manager = business_logic.HotelManager()
#invoice_manager = business_logic.InvoiceManager()
#room_facility_manager = business_logic.RoomFacilityManager()
#room_manager = business_logic.RoomManager()
#room_type_manager = business_logic.RoomTypeManager()


#TODO: Add more stuff


# Individuelle Testing -------------------

if False:
    print("test")
    # Testbereich (auf True sezten zum Testen)    










# Funktionierender Code------------------------
if True:
#Funktionierende Userstories (auf False sezten zum Testen)

    print("\nUser Story 1.6: Alle Hotels anzeigen (Name, Adresse, Sterne)\n")

    hotels = hotel_manager.read_all_hotels()

    if not hotels:
        print("Keine Hotels gefunden.")
    else:
        for hotel in hotels:
            print(f"{hotel.name} ({hotel.stars} Sterne)")
            print(f"Adresse: {hotel.address.street}, {hotel.address.zip_code} {hotel.address.city}")
            print("-" * 50)