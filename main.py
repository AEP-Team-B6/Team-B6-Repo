# allgemeiner Teil

from datetime import date
import os

import pandas as pd

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


# Individuelle Testing ------------------------

if False:
    # Testbereich (auf True sezten zum Testen)    




# Funktionierender Code------------------------
if True:
    #Funktionierende Userstories (auf False sezten zum Testen)

    # USERSTORY 1.1 
    city_name = None
    cancel = False
    while not city_name and not cancel:
        try:
            city_name = input_helper.input_valid_string("City name:")
        except input_helper.EmptyInputError:
            cancel = True
        except ValueError as err:
            print(err)

    if city_name is not None:
        matching_hotels = hotel_manager.find_hotel_by_city(city_name)
        if matching_hotels:
            for hotel in matching_hotels:
                print("following hotels matched your search:")
                print(hotel)            
        else:
            print("No hotels found")
    #---------------------------------------------------------------