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
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
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
    city_and_min_stars = [None, None]
    cancel = False

    while not city_and_min_stars[0] and not cancel:
        try:
            city_and_min_stars[0] = input_helper.input_valid_string("Gewünschte Stadt: ")
        except input_helper.EmptyInputError:
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
        except ValueError as err:
            print(err)

    while not city_and_min_stars[1] and not cancel:
        try:
            city_and_min_stars[1] = input_helper.input_valid_int("Mindestanzahl Sterne: ", min_value=1, max_value=5)
        except input_helper.EmptyInputError:
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
        except ValueError as err:
            print(err)
    
    if city_and_min_stars[0] is not None and city_and_min_stars[1] is not None:
        matching_hotels = hotel_manager.find_hotel_by_city_and_min_stars(city_and_min_stars)
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
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
        except ValueError as err:
            print(err)
    
    cancel = False
    while not city_and_guests[1] and not cancel:
        try:
            city_and_guests[1] = input_helper.input_valid_int("Gewünschte Anzahl Personen: ")
        except input_helper.EmptyInputError:
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
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
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
        except ValueError as err:
            print(err)
    
    cancel = False
    while not city_and_time[1] and not cancel:
        try:
            input_str = input_helper.input_valid_string("Startdatum (TT.MM.JJJJ): ")
            city_and_time[1] = datetime.strptime(input_str, "%d.%m.%Y").date()
        except input_helper.EmptyInputError:
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
        except ValueError:
            print("Ungültiges Format. Bitte TT.MM.JJJJ eingeben.")

    cancel = False
    while not city_and_time[2] and not cancel:
        try:
            input_str = input_helper.input_valid_string("Enddatum (TT.MM.JJJJ): ")
            city_and_time[2] = datetime.strptime(input_str, "%d.%m.%Y").date()
        except input_helper.EmptyInputError:
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
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

    #User Story 1.5
    #Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.
    print("\nIch möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.\n")
    search_params = [None, None, None, None, None]
    print("3 von 4 Suchparameter können bei Bedarf leer gelassen werden")

    while search_params[0] is None and search_params[1] is None and search_params[2] is None and search_params[3] is None:

        while search_params[0] is None:
            try:
                city = input_helper.input_valid_string("Gewünschte Stadt: ", allow_empty=True)
                if city:
                    search_params[0] = city
                break
            except Exception as e:
                print(e)

        while search_params[1] is None:
            try:
                search_params[1] = input_helper.input_valid_int("Mindestanzahl Sterne: ", min_value=1, max_value=5, allow_empty=True)
                break
            except Exception as e:
                print(e)

        while search_params[2] is None:
            try:
                search_params[2] = input_helper.input_valid_int("Gewünschte Anzahl Personen: ", allow_empty=True)
                break
            except Exception as e:
                print(e)

        while search_params[3] is None:
            try:
                start_date_str = input_helper.input_valid_string("Startdatum (TT.MM.JJJJ): ", allow_empty=True)
                if start_date_str:
                    search_params[3] = datetime.strptime(start_date_str, "%d.%m.%Y").date()
                break
            except Exception as e:
                print(e)

        if search_params[3] is not None:
            while search_params[4] is None:
                try:
                    end_date_str = input_helper.input_valid_string("Enddatum (TT.MM.JJJJ): ", allow_empty=False)
                    if end_date_str:
                        search_params[4] = datetime.strptime(end_date_str, "%d.%m.%Y").date()
                        if search_params[4] <= search_params[3]: #TODO möglicherweise könnte hier noch ein spezifischer error eingebaut werden, jedoch sollte das wahrscheinlich im UI sein
                            print("Enddatum muss nach dem Startdatum liegen")
                            search_params[4] = None
                    if search_params[4] is not None:        
                        break
                except Exception as e:
                    print(e)

        if search_params[0] is None and search_params[1] is None and search_params[2] is None and search_params[3] is None and search_params[4] is None:
            print("\nBitte geben Sie mindestens einen gültigen Suchparameter ein\n")


    prev_hotel_id = None
    result = hotel_manager.find_hotel_by_search_params(search_params)
    if result is not None:
        matching_hotels, matching_rooms, matching_addresses, matching_roomtypes = result
        print()
        print("-" * 50)
        print("Folgende Hotels passen zu Ihrer Suche:\n") #TODO Ausgaben könnten später durch UI gemacht werden
        for hotel in matching_hotels:
            if hotel.hotel_id != prev_hotel_id:
                prev_hotel_id = hotel.hotel_id
                if hotel.stars == 1:
                    print(f"Hotel {hotel.name} in {hotel.address.city} mit {hotel.stars} Stern")
                else:
                    print(f"Hotel {hotel.name} in {hotel.address.city} mit {hotel.stars} Sternen")

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
        print(f"Buchung storniert? {is_cancelled_str} / Totaler Preis: {booking.total_amount}")
        print("-" * 50)
    #---------------------------------------------------------------  

    # User Story 9
    # Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.
    print("\nAls Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.\n")

    room_details = room_manager.read_room_details()

    for room in room_details:
        print(f"Room ID: {room.room_id}")
        print(f"Room Number: {room.room_number}")
        print(f"Preis/Nacht: {room.price_per_night}")
        print(f"Zimmertyp: {room.room_type.description} (max. {room.room_type.max_guests} Gäste)")
        print(f"Hotel ID: {room.hotel.hotel_id}")

        facilities = room.get_facility_names() if hasattr(room, "get_facility_names") else [f.facility_name for f in room._Room__room_facility]

        if facilities:
            print(f"Ausstattung: {', '.join(facilities)}")
        else:
            print("Ausstattung: Keine zusätzlich Ausstattung verfügbar")

        print("-" * 50)
    #---------------------------------------------------------------  

    # User Story 10    
    # Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, 
    # und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.
    print("\nUser Story 10: Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.")
    supported_tables = {                               #Sets the changeable tables and attributes in a dict
        "room_type": ["description", "max_guests"],
        "facility": ["facility_name"],
        "room": ["room_number", "type_id", "price_per_night"],
        "guest": ["first_name", "last_name", "email"]
        }
    print("Admin-Stammdatenänderung gestartet (Abbruch jederzeit durch leere Eingabe)\n")

    while True:
        try:
            # Choose correct table, this block will fetch an input for the table and will check if it is allowed to make changes
            table = input_helper.input_valid_string("Welche Tabelle möchtest du ändern? (room, facility, guest, room_type): ", min_length=3)
            table = table.lower()
            if table not in supported_tables:
                raise ValueError(f"Ungültige Tabelle '{table}'. Erlaubt: {list(supported_tables.keys())}")

            # Now the corresponding ID will be requested from the admin
            id = input_helper.input_valid_int("Gib die ID des zu ändernden Eintrags ein: ", min_value=1)

            # Here is the same logic used as in the table fetch, but only for the attribute
            attribute = input_helper.input_valid_string(f"Welches Attribut von '{table}' möchtest du ändern? {supported_tables[table]}: ")
            attribute = attribute.lower()
            if attribute not in supported_tables[table]:
                raise ValueError(f"Ungültiges Attribut '{attribute}' für Tabelle '{table}'.")

            # The new value that should be set is asked from the admin. With conditions it is guaranteed, that there won't be any wrong types or negatives
            if attribute in ["max_guests", "type_id"]:
                new_value = input_helper.input_valid_int(f"Neuer Wert für {attribute} (Ganzzahl): ", min_value=0)
            elif attribute == "price_per_night":
                new_value = input_helper.input_valid_float(f"Neuer Preis (z.B. 199.99): ", min_value=0.0)
            else:
                new_value = input_helper.input_valid_string(f"Neuer Textwert für {attribute}: ", min_length=1, max_length=255)

            # Validation to make sure that the admin wants to confirm the expected change
            confirm = input_helper.input_y_n(f"Wirklich '{attribute}' von ID {id} in '{table}' auf '{new_value}' setzen? (y/n): ")
            # Now we need to ensure that the for the change the corresponding method from the correct manager will be called
            if confirm:
                if table == "room_type":
                    room_type_manager.update_room_type(id, attribute, new_value)
                elif table == "facility":
                    facility_manager.update_facility(id, new_value)
                elif table == "room":
                    room_manager.update_room(id, attribute, new_value)
                elif table == "guest":
                    guest_manager.update_guest(id, attribute, new_value)
                print("Update erfolgreich.\n")
            else:
                print("Änderung abgebrochen.\n")

            # Break for the loop, if the admin chooses "y" he can change another attribute value
            again = input_helper.input_y_n("Weitere Änderung durchführen? (y/n): ")
            if not again:
                print("Vorgang beendet.")
                break

        except input_helper.EmptyInputError:
            print("Vorgang abgebrochen.")
            break
        except ValueError as err:
            print(f"Fehler: {err}\n")
    #---------------------------------------------------------------  

        # User Story 4
    # Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.
    print("\n Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.\n")

    #Als erstes werden die Hotels angezeigt und der Input des gewünschten Hotels vom User abgefragt und auf dessen Richtigkeit geprüft
    hotels = hotel_manager.read_all_hotels()
    valid_hotel_ids = [hotel.hotel_id for hotel in hotels] #Liste von den hotel_id Werten der Datenbank wird erstellt.
    hotel_name_by_id = None    

    for hotel in hotels: #Print Output für User damit er die Hotels als Liste sieht
        print(f"Hotelnummer: {hotel.hotel_id}")
        print(f"Hotelname: {hotel.name}")
        print(f"Stadt: {hotel.address.city}")
        print("-" * 50)

    while hotel_name_by_id is None:
        try:
            hotel_choice = input_helper.input_valid_int("Bitte geben Sie die gewünschte Hotelnummer an: ")  #Abfrage welche Hotel der User wählen möchte  
    
            if hotel_choice in valid_hotel_ids: #Vergleich User Input mit Datenbank
                hotel_name_by_id = hotel_manager.read_hotel_by_id(hotel_choice)
                if hotel_name_by_id:
                    print(f"\nIhr gewähltes Hotel ist {hotel_name_by_id.name}")
                else:
                    print("\nFehler beim Abrufen der Hoteldaten. Bitte erneut versuchen.")
            else:
                print("\nDie eingegebene Hotelnummer ist nicht in der Liste. Bitte erneut versuchen.")
        
        except input_helper.EmptyInputError:
            print("\nDie Eingabe darf nicht leer sein. Bitte geben Sie eine Hotelnummer ein.")
        except ValueError as err:
            print(err)

    #Nun wird die Kundennummer vom User abgefragt und auf dessen Richtigkeit geprüft
    guests = guest_manager.read_all_guests()
    valid_guest_ids = [guest.guest_id for guest in guests] #Liste von den guest_id Werten der Datenbank wird erstellt.
    client_number = None
    
    while client_number is None:
        try:
            client_number_input = input_helper.input_valid_int("\nBitte geben Sie Ihre Kundennummer an: ", min_value=1)

            if client_number_input in valid_guest_ids: #Vergleich ob Kundennummer in Datenbank ist
                try:
                    confirm_client_number = input_helper.input_y_n(f"Bitte bestätigen Sie Ihre Kundennummer: {client_number_input} // (y oder n): ")
                    if confirm_client_number:
                        guest_id = client_number_input
                        client_number = client_number_input
                        print("\nKundennummer bestätigt.")
                    else:
                        print("\nBitte geben Sie Ihre Kundennummer erneut ein.")
                except ValueError as err:
                    print(err)
            else:
                print("Kundennummer existiert nicht, bitte geben Sie Ihre Kundennummer ein.\nBei wiederholtem auftreten, wenden Sie sich bitte an den System-Administrator")

        except input_helper.EmptyInputError:
            print("Die Eingabe darf nicht leer sein. Bitte geben Sie Ihre Kundennummer ein.")
        except ValueError as err:
            print(err)

    # Mit folgenden while Loops wird sichergestellt, dass nur valide Datumseingabgen stattfinden. #TODO sicherstellen, dass nur Daten in der Zukunft eingegeben werden können
    check_in_date = None
    check_out_date = None

    cancel = False
    while not check_in_date and not cancel:
        try:
            inp_check_in = input_helper.input_valid_string("Bitte geben Sie das gewünschte Startdatum ein (TT.MM.JJJJ): ")
            parsed_date = datetime.strptime(inp_check_in, "%d.%m.%Y").date()

            if parsed_date < date.today():  # Error Handling Prüfung, ob das gewählte Startdatum in der Vergangenheit liegt.
                print("Das Startdatum darf nicht in der Vergangenheit liegen.")
            else:
                check_in_date = parsed_date

        except input_helper.EmptyInputError:
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
        except ValueError:
            print("Ungültiges Format. Bitte TT.MM.JJJJ eingeben.")

    cancel = False
    while not check_out_date and not cancel:
        try:
            inp_check_out = input_helper.input_valid_string("Bitte geben Sie das gewünschte Enddatum ein (TT.MM.JJJJ): ")
            parsed_date = datetime.strptime(inp_check_out, "%d.%m.%Y").date()

            if parsed_date <= check_in_date: # Error Handling Prüfung, ob das gewählte Enddatum nach dem Startdatum liegt.
                print("Das Enddatum muss nach dem Startdatum liegen.")
            else:
                check_out_date = parsed_date

        except input_helper.EmptyInputError:
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
        except ValueError:
            print("Ungültiges Format. Bitte TT.MM.JJJJ eingeben.")

    name_and_time = [hotel_name_by_id.name, check_in_date, check_out_date]
    prev_hotel_id = None

    if name_and_time:
        result = hotel_manager.find_hotel_by_name_and_time(name_and_time)
        if result is not None:
            matching_hotels, matching_roomtypes, matching_rooms = result
            print(f"\nFolgende verfügbare Zimmer passen zu Ihrer Suche im Hotel {hotel_name_by_id.name}:") #TODO Ausgaben könnten später durch UI gemacht werden
            
            for hotel in matching_hotels:
                if hotel.hotel_id != prev_hotel_id:
                    prev_hotel_id = hotel.hotel_id
            
            for room in matching_rooms:
                if room.hotel.hotel_id == hotel.hotel_id:
                    
                    print(f"Zimmer Nr.: {room.room_number}  |  Raumtyp: {room.room_type.description}  |  max. Personen: {room.room_type.max_guests}")
            print("-" * 50)  
            cancel_booking = False

            valid_room_numbers = [int(room.room_number) for room in matching_rooms] #Liste aus Matching Rooms erstellt um zu Prüfen, dass der nächste Input ein Wert aus dieser Liste ist

            room_id = None

            while room_id is None:
                try:
                    room_number = input_helper.input_valid_int("\nBitte wählen Sie eine Zimmernummer aus dieser Liste: ") #User Input, welche Raumnummer er möchte
                    if room_number in valid_room_numbers: #Prüfung ob gewählter Raum in obiger Liste vorhanden ist
                        room_id_by_number = room_manager.read_room_details_by_room_number(room_number) #Aufruf der Methode damit room_id gefetched werden kann
                        if room_id_by_number:
                            room_id = room_id_by_number.room_id
                            price_per_night = float(room_id_by_number.price_per_night)
                        else:
                            print("Fehler beim Abruf der Raum ID")

                    else:
                        print("Ungültige Zimmernummer ausgewählt.")
                
                except input_helper.EmptyInputError:
                    print("Die Eingabe darf nicht leer sein. Bitte geben Sie eine Hotelnummer ein.")
                except ValueError as err:
                    print(err)
     
        else:
            print(f"Leider wurden keine verfügbaren Räume zum angegebenen Zeitraum im Hotel {hotel_name_by_id.name} gefunden")
            cancel_booking = True

    is_cancelled = 0

    duration = check_out_date - check_in_date
    booked_nights = duration.days
   
    total_amount = booked_nights * price_per_night

    confirm_booking = False

    while not cancel_booking:
        confirmation = input(f"\nWollen Sie die Buchung im {hotel_name_by_id.name} von {check_in_date} bis {check_out_date} bestätigen? (y/n): ")
        confirmation = confirmation.lower()
        if confirmation == "y":
            confirm_booking = True
            break
        elif confirmation == "n":
            print("Buchungsvorgang wurde abgebrochen")
            break
        else:
            print("Ungültige Eingabe. Bitte geben Sie 'y' (ja) oder 'n' (nein) ein.")

    if confirm_booking == True:
        final_booking = booking_manager.generate_booking(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        print(f"\nBuchung erfolgreich! Ihre Buchungsnummer lautet: {final_booking}")
    else:
        print("Buchungsvorgang fehlgeschlagen")

    #---------------------------------------------------------------