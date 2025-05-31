# allgemeiner Teil

from datetime import datetime, date
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

    #User Story 1.4
    #Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) 
    # Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.
    print("\nIch möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes (von (check_in_date) und bis (check_out_date)).")
    print("Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.\n")
    city_and_time = [None, None, None]
    cancel = False
    while not city_and_time[0] and not cancel: #TODO für diese Inputbnlöcke könnte eine Funktion mit Übergabeparametern definiert werden (weniger redunanter code)
        try:
            city_and_time[0] = input_helper.input_valid_string("Gewünschte Stadt: ")
        except input_helper.EmptyInputError:
            cancel = True
        except ValueError as err:
            print(err)
    
    cancel = False
    while not city_and_time[1] and not cancel:
        try:
            input_str = input_helper.input_valid_string("Startdatum (TT.MM.JJJJ): ")
            city_and_time[1] = datetime.strptime(input_str, "%d.%m.%Y").date()
        except input_helper.EmptyInputError:
            cancel = True
        except ValueError:
            print("Ungültiges Format. Bitte TT.MM.JJJJ eingeben.")

    cancel = False
    while not city_and_time[2] and not cancel:
        try:
            input_str = input_helper.input_valid_string("Enddatum (TT.MM.JJJJ): ")
            city_and_time[2] = datetime.strptime(input_str, "%d.%m.%Y").date()
        except input_helper.EmptyInputError:
            cancel = True
        except ValueError:
            print("Ungültiges Format. Bitte TT.MM.JJJJ eingeben.")

    prev_hotel_id = None
    if city_and_time[0] and city_and_time[1] and city_and_time[2] is not None:
        result = hotel_manager.find_hotel_by_city_and_time(city_and_time)
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
    #Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.

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

        # User Story 8
    # Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.
    print("\n Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.\n")
    all_bookings = booking_manager.read_all_bookings()
    
    for booking in all_bookings:
        is_cancelled_str = booking.is_cancelled
        if is_cancelled_str == 0:
            is_cancelled_str = "Nein"
        else:
            is_cancelled_str = "Ja"
        print(f"Buchungsnummer: {booking.booking_id}, Gast_ID: {booking.guest}, Raum_ID: {booking.room}")
        print(f"Aufenthalt von: {booking.check_in_date.strftime("%d.%m.%Y")} bis {booking.check_out_date.strftime("%d.%m.%Y")}")
        print(f"Buchung storniert? {is_cancelled_str}, Totaler Preis: {booking.total_amount}")
        print("-" * 50)
    #---------------------------------------------------------------  