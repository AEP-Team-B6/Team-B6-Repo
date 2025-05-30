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

hotel_reservation_sample = "./database/hotel_reservation_sample.db"
current_db = "./database/current_db.db"

shutil.copyfile(hotel_reservation_sample, current_db)

os.environ["DB_FILE"] = current_db


# Increase row and column display limits
pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.width", None)  # Auto-adjust display width
pd.set_option("display.max_colwidth", None)  # Show full column content


#Manager initialization
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


# Individuelles Testing ------------------------

if False:
    print("test")
    # Testbereich (auf True sezten zum Testen)    
    


# Funktionierender Code------------------------

if True:
    print("all working user stories will now be runned trough")
    #Funktionierende Userstories (auf False sezten zum Testen)
    #Userstory 1.1 
    #Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.
    print("\nUser Story 1.1: Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.\n")
    city_name = None
    cancel = False
    while not city_name and not cancel:
        try:
            city_name = input_helper.input_valid_string("Gewünschte Stadt: ")
        except input_helper.EmptyInputError:
            cancel = True
        except ValueError as err:
            print(err)

    if city_name is not None:
        matching_hotels = hotel_manager.find_hotel_by_city(city_name)
        if matching_hotels:
            print("Folgende Hotels passen zu Ihrer Suche:") #TODO Ausgaben könnten später durch UI gemacht werden
            for hotel in matching_hotels:
                if hotel.stars == 1:
                    print(f"Hotel {hotel.name} mit {hotel.stars} Stern")
                else:
                    print(f"Hotel {hotel.name} mit {hotel.stars} Sternen")
                print("-" * 50)            
        else:
            print("Leider wurden keine passenden Hotels gefunden")
    #---------------------------------------------------------------

    #Userstory 1.2
    #Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen. 
    #TODO Hier könnte noch eine Auswahl umgesetzt werden, ob man =, > oder < der angegeben Anzahl sternen suchen will. Momentan zeigt es einfach alle >= an.
    print("\nUser Story 1.2: Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.\n")
    min_stars = None
    cancel = False
    while not min_stars and not cancel:
        try:
            min_stars = input_helper.input_valid_int("Mindestanzahl Sterne: ")
        except input_helper.EmptyInputError:
            cancel = True
        except ValueError as err:
            print(err)
    
    if min_stars is not None:
        matching_hotels = hotel_manager.find_hotel_by_min_stars(min_stars)
        if matching_hotels:
            print("Folgende Hotels passen zu Ihrer Suche:") #TODO Ausgaben könnten später durch UI gemacht werden
            for hotel in matching_hotels:
                if hotel.stars == 1:
                    print(f"Hotel {hotel.name} mit {hotel.stars} Stern")
                else:
                    print(f"Hotel {hotel.name} mit {hotel.stars} Sternen")
                print("-" * 50)           
        else:
            print("Leider wurden keine passenden Hotels gefunden")
    #---------------------------------------------------------------

    #Userstory 1.3 
    #Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).
    print("\nIch möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).\n")
    city_and_guests = [None, None]
    cancel = False
    while not city_and_guests[0] and not cancel:
        try:
            city_and_guests[0] = input_helper.input_valid_string("Gewünschte Stadt: ")
        except input_helper.EmptyInputError:
            cancel = True
        except ValueError as err:
            print(err)
    
    amount_guests = None
    cancel = False
    while not city_and_guests[1] and not cancel:
        try:
            city_and_guests[1] = input_helper.input_valid_int("Gewünschte Anzahl Personen: ")
        except input_helper.EmptyInputError:
            cancel = True
        except ValueError as err:
            print(err)

    prev_hotel_id = None
    if city_and_guests[0] and city_and_guests[1] is not None:
        result = hotel_manager.find_hotel_by_city_and_guests(city_and_guests)
        if result is not None:
            matching_hotels, matching_roomtypes, matching_rooms = result
            print("Folgende Hotels passen zu Ihrer Suche:") #TODO Ausgaben könnten später durch UI gemacht werden
            for hotel in matching_hotels:
                if hotel.hotel_id != prev_hotel_id:
                    prev_hotel_id = hotel.hotel_id
                    if hotel.stars == 1:
                        print(f"Hotel {hotel.name} mit {hotel.stars} Stern")
                    else:
                        print(f"Hotel {hotel.name} mit {hotel.stars} Sternen")

                    for room in matching_rooms:
                        if room.hotel.hotel_id == hotel.hotel_id:
                            
                            print(f"Raum Nr.: {room.room_number}  |  Raumtyp: {room.room_type.description}  |  max. Personen: {room.room_type.max_guests}")
                    print("-" * 50)          
        else:
            print("Leider wurden keine passenden Hotels gefunden")
    #---------------------------------------------------------------

    #Userstory 1.6
    print("\nUser Story 1.6: Alle Hotels anzeigen (Name, Adresse, Sterne)\n")

    hotels = hotel_manager.read_all_hotels()

    if not hotels:
        print("Keine Hotels gefunden.")
    else:
        for hotel in hotels:
            print(f"{hotel.name} ({hotel.stars} Sterne)")
            print(f"Adresse: {hotel.address.street}, {hotel.address.zip_code} {hotel.address.city}")
            print("-" * 50)
    #---------------------------------------------------------------

    #Userstory 3.1
    class HotelDataAccess:
        def __init__(self, db_connection):
            self.conn = db_connection

        def add_hotel(self, name: str, stars: int = None, address_id: int = None) -> int:
            query = """
            INSERT INTO Hotel (name, stars, address_id)
            VALUES (?, ?, ?);
            """
            cursor = self.conn.cursor()
            cursor.execute(query, (name, stars, address_id))
            self.conn.commit()
            return cursor.lastrowid
    #---------------------------------------------------------------

    #Userstory 3.2
    class HotelDataAccess:
        def __init__(self, db_connection):
            self.conn = db_connection

        def delete_hotel(self, hotel_id: int) -> bool:
            query = "DELETE FROM Hotel WHERE hotel_id = ?"
            cursor = self.conn.cursor()
            cursor.execute(query, (hotel_id,))
            self.conn.commit()

            # Prüfen, ob ein Datensatz gelöscht wurde
            return cursor.rowcount > 0
    #---------------------------------------------------------------