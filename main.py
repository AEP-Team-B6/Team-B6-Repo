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
from model import Hotel
from model import Address
from model import Booking
from model import Guest
from model import Room
from model import Review

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
review_manager = business_logic.ReviewManager()


#TODO: Add more stuff


# Individuelles Testing ------------------------

if False:
    print("test")
    # Testbereich (auf True sezten zum Testen)




# Funktionierender Code------------------------

if True:
    print("all working user stories will now be runned trough")
    #Funktionierende Userstories (auf False sezten zum Testen)

        #--------------------------------------------------------------- 
    # US 1.1: Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.
    # US 1.2: Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.
    # US 1.3: Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).
    # US 1.4: Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.
    # US 1.5: Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.
    # US 2.1: Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.
    # US 2.2: Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von – bis) spezifiziert habe.
    # US   7: Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann.

    print("\nUser Story 1.1-1.5 und User Story 2.1, 2.2 und User Story 7")
    print("\nSie können nun nach Belieben nach Hotels und Zimmereigenschaften suchen")
    search_params = [None, None, None, None, None]
    print("(3 von 4 Suchparameter können bei Bedarf leer gelassen werden)\n")

    today = date.today()
    nights = 1

    while search_params[0] is None and search_params[1] is None and search_params[2] is None and search_params[3] is None:
        while search_params[0] is None:
            try:
                city = input_helper.input_valid_string("Gewünschte Stadt: ", allow_empty=True)  
                if city:
                    search_params[0] = city.title() # Stellt sicher, dass der User Input ins Format der Datenbank formatiert wird
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
                    start_date = datetime.strptime(start_date_str, "%d.%m.%Y").date()
                    if start_date < today: #prüfen ob Startdatum nicht in der Vergangenheit liegt
                        print("Fehler: Startdatum darf nicht vor heute liegen.")
                        continue
                    search_params[3] = start_date
                break
            except ValueError:
                print("Ungültiges Format. Bitte TT.MM.JJJJ eingeben.")
            except Exception as e:
                print(e)

        if search_params[3] is not None:
            while search_params[4] is None:
                try:
                    end_date_str = input_helper.input_valid_string("Enddatum (TT.MM.JJJJ): ", allow_empty=False)
                    if end_date_str:
                        end_date = datetime.strptime(end_date_str, "%d.%m.%Y").date()
                        if end_date <= search_params[3]: #TODO möglicherweise könnte hier noch ein spezifischer error eingebaut werden, jedoch sollte das wahrscheinlich im UI sein
                            print("Fehler: Enddatum muss nach dem Startdatum liegen.")
                            continue
                        search_params[4] = end_date
                        nights = (end_date - search_params[3]).days
                    break
                except ValueError:
                    print("Ungültiges Format. Bitte TT.MM.JJJJ eingeben.")
                except Exception as e:
                    print(e)
                    
        if search_params[0] is None and search_params[1] is None and search_params[2] is None and search_params[3] is None and search_params[4] is None:
            print("\nBitte geben Sie mindestens einen gültigen Suchparameter ein\n")

        result = hotel_manager.find_hotel_by_search_params(search_params) #übergeben der Suchparameter an den Hotelmanager und abfüllen des Ergebniss in result

        if result is not None:
            matching_hotels, matching_rooms, matching_addresses, matching_roomtypes  = result #entpacken der Liste
            print("\n" + "-"*80)
            print("Folgende Hotels passen zu Ihrer Suche:\n")
            print("─"*100)

            for hotel in matching_hotels:
                print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Stern{'en' if hotel.stars>1 else ''}")
                print(f"{'':<4}" + "-" * 80)

                for room in matching_rooms:
                    if room.hotel.hotel_id == hotel.hotel_id:
                        if search_params[3]:
                            mon = search_params[3].month

                            if 5 <= mon <= 9:
                                season = "Hauptsaison ist"
                                price = room.price_per_night
                                other = room.price_per_night_ls
                                other_season = "Nebensaison wäre"

                            else:
                                season = "Nebensaison ist"
                                price = room.price_per_night_ls
                                other = room.price_per_night
                                other_season = "Hauptsaison wäre"

                        else:
                            season = "in der Hauptsaison ist"
                            price = room.price_per_night
                            other = room.price_per_night_ls
                            other_season = "Nebensaison ist"

                        total = nights * price

                        print(f"{'':<4}Raum {room.room_number} | Typ: {room.room_type.description} | max. {room.room_type.max_guests} Pers.")
                        print(f"{'':<10}• Preis pro Nacht in der {season}: {price:.2f} CHF") #einrücken der Zeile um 10 Stellen, damit es übersichtlicher ist.
                        print(f"{'':<10}• Preis pro Nacht in der {other_season}: {other:.2f} CHF")

                        if search_params[3]: # Anzeigen der Anzahl Nächte und des daraus resultierenden Gesamttotals, jedoch nur wenn ein Zeitraum eingegeben wurde
                            print(f"{'':<10}• Nächte: {nights}, Gesamttotal: {total:.2f} CHF")

                        if room.room_facility: # Wenn das Zimmer eine oder mehrere Ausstattungen hat, werden sie angezeigt
                            print(f"{'':<10}• Ausstattung:")

                            for facility in room.room_facility:
                                print(f"{'':<14}→ {facility}")

                        else:
                            print(f"{'':<10}Keine Zusatz-Ausstattung")

                        print(f"{'':<4}" + "-" * 80)
                        
                print("─"*100)
        else:
            print("Leider wurden keine passenden Hotels gefunden")
            try:
                retry = input_helper.input_y_n("Möchten Sie eine neue Suche starten? (y/n): ")
                if retry:
                    # Zurück zum Anfang der while-Schleife, indem die search_params zurückgesetzt werden
                    search_params = [None, None, None, None, None]
                    continue
                else:
                    print("Vorgang beendet.")
            except Exception as e:
                print(f"Ungültige Eingabe. Vorgang beendet. ({e})")

    #--------------------------------------------------------------- 

    # Userstory 1.6
    # Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.

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

    # User Story 3.1 (Als Admin) Ich möchte neue Hotels zum System hinzufügen

    while True:
        print("\nNeues Hotel hinzufügen. (Durch leere Eingabe Vorgang abbrechen)")
        
        try:
            # 1. Adresse erfassen
            print("1. Adresse erfassen:")
            street = None
            zip_code = None
            city = None

            while True:
                try:
                    street = input_helper.input_valid_string("Bitte gib die Strasse an: ", min_length=3)
                    break
                except input_helper.EmptyInputError:
                    print("Vorgang abgebrochen.")
                    break
                except input_helper.StringLengthError as e:
                    print(f"Fehler: {e}")
            if not street:
                break

            while True:
                try:
                    zip_code = input_helper.input_valid_int("Bitte gib die Postleitzahl an: ", min_value=1000, max_value=9999)
                    break
                except input_helper.EmptyInputError:
                    print("Vorgang abgebrochen.")
                    break
                except input_helper.OutOfRangeError as e:
                    print(f"Fehler: {e}")
                except ValueError as e:
                    print(f"Fehler: {e}")
            if zip_code is None:
                break

            while True:
                try:
                    city = input_helper.input_valid_string("Bitte gib die Stadt an: ", min_length=2)
                    break
                except input_helper.EmptyInputError:
                    print("Vorgang abgebrochen.")
                    break
                except input_helper.StringLengthError as e:
                    print(f"Fehler: {e}")
            if not city:
                break

            address = Address(address_id= None, street=street, zip_code=zip_code, city=city)
            address_id = address_manager.create_address(address)
            address.address_id = address_id

            print(f"Adresse wurde erfolgreich hinzugefügt (ID: {address_id})")

            print("2. Hotel erfassen")
            hotel_name = None
            stars = None
            
            while True:
                try:
                    hotel_name = input_helper.input_valid_string("Hotelname: ", min_length=2)
                    break
                except input_helper.EmptyInputError:
                    print("Vorgang abgebrochen.")
                    break
                except input_helper.StringLengthError as e:
                    print(f"Fehler: {e}")
            if not hotel_name:
                break

            while True:
                try:
                    stars = input_helper.input_valid_int("Anzahl Sterne: ", min_value=1, max_value=5)
                    break
                except input_helper.EmptyInputError:
                    print("Vorgang abgebrochen.")
                    break
                except input_helper.OutOfRangeError as e:
                    print(f"Fehler: {e}")
                except ValueError as e:
                    print(f"Fehler: {e}")
            if stars is None:
                break

            hotel = Hotel(hotel_id=None, name=hotel_name, stars=stars, address=address, rooms=None, reviews=None)
            hotel_id = hotel_manager.add_hotel(hotel)

            print(f"Hotel erfolgreich hinzugefügt (ID: {hotel_id})")

            # Break for the loop, if the admin chooses "y" he can change another attribute value
            again = input_helper.input_y_n("Weiteres Hotel hinzufügen? (y/n): ")
            if not again:
                print("Vorgang beendet.")
                break

        except input_helper.EmptyInputError:
            print("Vorgang abgebrochen.")
            break
        except ValueError as err:
            print(f"Fehler: {err}\n")
    #--------------------------------------------------------------- 

    # User Story 3.2 (Als Admin) Ich möchte Hotels aus dem System entfernen
        
    while True:
        try:
            print("Hotel entfernen. (Durch leere Eingabe Vorgang abbrechen)")

            # Eingabe der Hotel-ID und Adress-ID
            hotel_id = input_helper.input_valid_int("Bitte gib die Hotel-ID ein: ")
            address_id = input_helper.input_valid_int("Bitte gib die Adress-ID ein: ")

            # Hotel löschen
            success_hotel = hotel_manager.delete_hotel(hotel_id)
            if success_hotel:
                print(f"Hotel mit ID {hotel_id} wurde erfolgreich gelöscht.")
            else:
                print(f"Hotel mit ID {hotel_id} konnte nicht gefunden oder gelöscht werden.")

            # Adresse löschen
            success_address = address_manager.delete_address(address_id)
            if success_address:
                print(f"Adresse mit ID {address_id} wurde erfolgreich gelöscht.")
            else:
                print(f"Adresse mit ID {address_id} konnte nicht gefunden oder gelöscht werden.")
            # Break for the loop, if the admin chooses "y" he can change another attribute value
            again = input_helper.input_y_n("Weiteres Hotel löschen? (y/n): ")
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
            cancel = False # Geändert auf false, da du das datum umbedingt benötigst um eine Buchung zu erstellen
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
            cancel = False #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebroben wird.
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

    # User Story 8
    # Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.
    print("\nUser Story 8: Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.\n")
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
    print("\nUser Story 9: Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.\n")

    room_details = room_manager.read_room_details()

    for room in room_details:
        print(f"Room ID: {room.room_id}")
        print(f"Room Number: {room.room_number}")
        print(f"Preis/Nacht: {room.price_per_night}")
        print(f"Zimmertyp: {room.room_type.description} (max. {room.room_type.max_guests} Gäste)")
        print(f"Hotel ID: {room.hotel.hotel_id}")

        facilities = room.room_facility

        if facilities:
            print("Ausstattung:", ", ".join([f.facility_name for f in facilities]))
        else:
            print("Ausstattung: -")
        
        print("-" * 50)
    #---------------------------------------------------------------  

    # User Story 10 und 3.3
    # TODO: error handling einbauen wenn ID nicht vorhanden
    # User Stroy 10:
    # Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Hoteldaten, Zimmertypen, Einrichtungen, 
    # und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.
    # User Story 3.3
    # (Als Admin) Ich möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw. (hinzugefügt: Addresse)
    print("\nUser Story 10: Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.")
    print("und")
    print("User Story 3.3: (Als Admin) Ich möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.\n")
    supported_tables = {                               #Sets the changeable tables and attributes in a dict
        "room_type": ["description", "max_guests"],
        "facility": ["facility_name"],
        "room": ["room_number", "type_id", "price_per_night", "price_per_night_ls"],
        "guest": ["first_name", "last_name", "email"],
        "hotel": ["name", "stars"],
        "address": ["street", "city", "zip_code"]
        }
    print("Admin-Stammdatenänderung gestartet (Abbruch jederzeit durch leere Eingabe)\n")

    while True:
        try:
            # Choose correct table, this block will fetch an input for the table and will check if it is allowed to make changes
            table = input_helper.input_valid_string(f"Welche Tabelle möchtest du ändern? ({list(supported_tables.keys())}): ", min_length=3)
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
            if attribute in ["max_guests", "type_id", "stars"]:
                new_value = input_helper.input_valid_int(f"Neuer Wert für {attribute} (Ganzzahl): ", min_value=0)
            elif attribute == "price_per_night":
                new_value = input_helper.input_valid_float(f"Neuer Preis (z.B. 199.99): ", min_value=0.0)
            elif attribute == "price_per_night_ls":
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
                elif table == "hotel":
                    hotel_manager.update_hotel(id, attribute, new_value)
                elif table == "address":
                    address_manager.update_address(id, attribute, new_value)
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
    
    #User Story DB 2.1 
    # Als Gast möchte ich auf meine Buchungshistorie zuzugreifen ("lesen"), damit ich meine kommenden Reservierungen verwalten kann.
    # 2.1. Die Anwendungsfälle für meine Buchungen sind "neu/erstellen", "ändern/aktualisieren", "stornieren/löschen".

    print("\nAls Gast möchte ich auf meine Buchungshistorie zuzugreifen (lesen), damit ich meine kommenden Reservierungen verwalten kann.")
    print("US 2.1: Die Anwendungsfälle für meine Buchungen sind neu/erstellen, ändern/aktualisieren, stornieren/löschen\n")

    # Anzeigen aller Buchungen
    guest_id = None
    cancel = False
    while not guest_id and not cancel:
        try:
            guest_id = input_helper.input_valid_int("bitte geben Sie ihre Kundennummer ein: ", min_value=1)
        except input_helper.EmptyInputError:
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebrochen wird.
        except ValueError as err:
            print(err)

    result = booking_manager.get_booking_by_guest_id(guest_id)
    if result is not None:
        matching_bookings = result
            
        print()
        print("-" * 50)
        print("Folgende Buchungen sind zu ihrer Kundennummer erfasst:\n") #TODO Ausgaben könnten später durch UI gemacht werden
        for booking in matching_bookings:
            is_cancelled_str = booking.is_cancelled
            if is_cancelled_str == 0:
                is_cancelled_str = "Nein"
            else:
                is_cancelled_str = "Ja"
            print(f"Buchungsnummer: {booking.booking_id} | Gast_ID: {booking.guest.guest_id} | Raum_ID: {booking.room.room_id}")
            print(f"Aufenthalt von: {booking.check_in_date.strftime("%d.%m.%Y")} bis {booking.check_out_date.strftime("%d.%m.%Y")}")
            print(f"Buchung storniert? {is_cancelled_str} | Totaler Preis: {booking.total_amount}")
            print("-" * 50)          
    else:
        print("Leider wurden keine Buchungen gefunden")

    # Bearbeiten der Buchungen
    print("\nBuchungen bearbeiten")
    print("-" * 50)  
    booking_edit_mode = None
    cancel = False
    while not booking_edit_mode and not cancel:
        try:
            booking_edit_mode = input_helper.input_valid_int("bitte wählen sie den Bearbeitungsmodus:\n1: neu erstellen\n2: aktualisieren\n3: stornieren\n", min_value=1, max_value=3)
        except input_helper.EmptyInputError:
            cancel = True #TODO wir müssen bestimmen ob bei leerer Eingabe die Aufforderung wiederholt oder abgebrochen wird.
        except ValueError as err:
            print(err)
    
    match booking_edit_mode:
        case 1: 
            print("\nNeue Buchung eintragen")
            print("-" * 50)
            booking_id = None

        case 2: 
            print("\nBuchung aktualisieren (nur die zu ändernden Werte eingeben)")
            print("-" * 50)

        case 3:
            guest_id = None
            room_id = None
            start_date = None
            end_date = None
            is_cancelled = 1
            total_amount = 0

    #einlesen der Buchungsnummer für Ändern oder Stornieren
    if booking_edit_mode == 2 or booking_edit_mode == 3:
        booking_id = None
        while booking_id is None:
            try:
                booking_id = input_helper.input_valid_int("Buchungsnummer: ", min_value=1,)
            except Exception as e:
                print(e)

    #einlesen der Informationen für Erstellen oder Ändern
    if booking_edit_mode == 1 or booking_edit_mode == 2:
    #Kundennummer
        guest_id = None
        while guest_id is None:
            try:
                guest_id = input_helper.input_valid_int("Kundennummer: ", min_value=1, allow_empty=(booking_edit_mode == 2)) #darf nur leer sein beim Ändern, nicht beim Erstellen
                break
            except Exception as e:
                print(e)

    #Zimmer ID
        room_id = None
        while room_id is None:
            try:
                room_id = input_helper.input_valid_int("Zimmer ID: ", min_value=1, allow_empty=(booking_edit_mode == 2)) #TODO hier könnte noch geprüft werden, welche Zimmer IDs es gibt und es dann mit max_value begrenzen
                break
            except Exception as e:
                print(e)
                
    #Startdatum
        start_date = None
        while start_date is None:
            try:
                start_date_str = input_helper.input_valid_string("Startdatum (TT.MM.JJJJ): ", allow_empty=(booking_edit_mode == 2))
                if start_date_str:
                    start_date = datetime.strptime(start_date_str, "%d.%m.%Y").date()
                break
            except Exception as e:
                print(e)

    #Enddatum
        end_date = None
        if start_date is not None:
            while end_date is None:
                try:
                    end_date_str = input_helper.input_valid_string("Enddatum (TT.MM.JJJJ): ")
                    if end_date_str:
                        end_date = datetime.strptime(end_date_str, "%d.%m.%Y").date()
                        if end_date <= start_date: #TODO möglicherweise könnte hier noch ein spezifischer error eingebaut werden, jedoch sollte das wahrscheinlich im UI sein
                            print("Enddatum muss nach dem Startdatum liegen")
                            end_date = None
                    if end_date is not None:        
                        break
                except Exception as e:
                    print(e)

    #Storniert
        is_cancelled = 0

    #Gesamtbetrag
        total_amount = None
        while total_amount is None:
            try:
                total_amount = input_helper.input_valid_int("Gesamtbetrag: ", min_value=0, allow_empty=(booking_edit_mode == 2))
                break
            except Exception as e:
                print(e)

    # Erstellen der Objekte
    guest = Guest(guest_id=guest_id, first_name=None, last_name=None, email=None, address=None, bookings=None)
    room = Room(room_id=room_id, room_number=None, price_per_night=None, price_per_night_ls=None, room_type=None, hotel=None)
    booking = Booking(booking_id=booking_id, guest=guest, room=room, check_in_date=start_date, check_out_date=end_date, is_cancelled=is_cancelled, total_amount=total_amount)

    # Aufrufen der Manager und bestätigen
    match booking_edit_mode:
        case 1:
            new_booking_id = booking_manager.create_booking(booking)
            print(f"Neue Buchung erstellt mit der Buchungsnummer {new_booking_id}")
        case 2:
            updated_booking = booking_manager.update_booking(booking)
            print(f"Buchung mit der Buchungsnummer {booking_id} aktualisiert")
            print(f"Buchungsnummer: {updated_booking.booking_id} | Guest-ID: {updated_booking.guest.guest_id} | Room-ID: {updated_booking.room.room_id} | Startdatum: {updated_booking.check_in_date} | Enddatum: {updated_booking.check_out_date} | Storniert: {updated_booking.is_cancelled} | Gesamtbetrag: {updated_booking.total_amount}")
        case 3:
            print("\nBuchung stornieren")
            print("-" * 50)
            updated_booking = booking_manager.update_booking(booking)
            print(f"Buchung mit der Buchungsnummer {booking_id} storniert")
            print(f"Buchungsnummer: {updated_booking.booking_id} | Guest-ID: {updated_booking.guest.guest_id} | Room-ID: {updated_booking.room.room_id} | Startdatum: {updated_booking.check_in_date} | Enddatum: {updated_booking.check_out_date} | Storniert: {updated_booking.is_cancelled} | Gesamtbetrag: {updated_booking.total_amount}")
    #---------------------------------------------------------------  

    # User Story DB 3 
    # Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.
    print("-" * 50)
    print("Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.")
    print("Vielen Dank, dass Sie sich für eine Bewertung Zeit nehmen.")

    cancel = False
    while not cancel:
        try:
            guest_id = input_helper.input_valid_int("Bitte geben Sie Ihre Kundennummer ein: ", min_value=1)
            if guest_id is None:
                print("Vorgang abgebrochen.")
                break

            guest_bookings = booking_manager.get_booking_by_guest_id(guest_id)

            valid_bookings = []
            if not guest_bookings:
                print("Keine vergangenen Aufenthalte gefunden.")
                break

            for b in guest_bookings:
                if b.check_out_date < date.today():
                    print(f"Buchung ID: {b.booking_id}, Aufenthalt: {b.check_in_date} bis {b.check_out_date}, Hotel: {b.room.hotel.name}")
                    valid_bookings.append(b)

            if not valid_bookings:
                print("Es sind keine abgeschlossenen Buchungen vorhanden, die bewertet werden können.")
                break

            selected_booking = None

            while selected_booking is None:
                try:
                    booking_id = input_helper.input_valid_int("Welche Buchung möchten Sie bewerten? (Buchungs-ID): ", min_value=1, allow_empty=True)
                    
                    if booking_id is None:
                        print("Vorgang abgebrochen.")
                        break

                    for booking in valid_bookings:
                        if booking.booking_id == booking_id:
                            selected_booking = booking
                            break

                    if selected_booking is None:
                        print("Keine passende Buchung gefunden. Bitte geben Sie eine gültige Buchungsnummer ein.")

                except input_helper.EmptyInputError:
                    print("Vorgang abgebrochen.")
                    break
                except ValueError as e:
                    print(f"Ungültige Eingabe: {e}")

            rating = input_helper.input_valid_int("Wie gut war deine Erfahrung von 1-10?: ", min_value=1, max_value=10)
            if rating is None:
                print("Vorgang abgebrochen.")
                break

            comment = input_helper.input_valid_string("Kommentar zur Bewertung: ")
            if comment is None:
                print("Vorgang abgebrochen.")
                break

            review = Review(
                review_id=None,
                rating=rating,
                comment=comment,
                booking=selected_booking,
                hotel=selected_booking.room.hotel
            )

            review_manager.submit_review(review)
            print("Vielen Dank für deine Bewertung!")
            break  # Nach erfolgreicher Bewertung beenden

        except input_helper.EmptyInputError:
            print("Vorgang abgebrochen.")
            break
        except ValueError as e:
            print(f"Ungültige Eingabe: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
            break
    #---------------------------------------------------------------

    # User Story Vis 1
    # Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in meinem Hotel sehen, damit ich weiss, 
    # welche Zimmer am beliebtesten sind und ich meine Buchungsstrategien optimieren kann.
    print("\nUser Story Vis 1: Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in meinem Hotel sehen, damit ich weiss,") 
    print("welche Zimmer am beliebtesten sind und ich meine Buchungsstrategien optimieren kann.\n")

    df = room_type_manager.get_stays_per_room_type()
    df.set_index("type_id", inplace=True) # inplace aktiviert um nicht andauernd Kopien zu erstellen und speicher zu verschwenden
    df.sort_values(by="stays", ascending=False, inplace=True)

    print("Raumtypen absteigend sortiert nach Übernachtungen")
    print("-" * 50) 
    print(df)
    #---------------------------------------------------------------

      #---------------------------------------------------------------
    
        #User Story 5 
        # Als Gast möchte ich nach meinem Aufenthalt eine Rechnung
        #erhalten, damit ich einen Zahlungsnachweis habe.
        #Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.

        
    guest_id = input_helper.input_valid_int("Bitte geben Sie Ihre Kundennummer ein: ", min_value=1)

    guest_bookings = booking_manager.get_booking_by_guest_id(guest_id)

        ###Nur abgeschlossene Buchungen werden akzeptiert
    past_bookings = [booking for booking in guest_bookings if booking.check_out_date < date.today()]

    if not past_bookings:
        print("Keine vergangenen Aufenthalte gefunden.")
    else:
        print("Vergangene Buchungen:")
        for booking in past_bookings:
            hotel_name = booking.room.hotel.name if booking.room.hotel else "Unbekannt"
        print(f"Buchung ID: {booking.booking_id}, Aufenthalt: {booking.check_in_date} bis {booking.check_out_date}, Hotel: {hotel_name}")

        booking_id = input_helper.input_valid_int("Für welche Buchung möchten Sie eine Rechnung erstellen? (Buchungs-ID): ", min_value=1)
        selected_booking = next((booking for booking in past_bookings if booking.booking_id == booking_id), None)

        if not selected_booking:
                print("Ungültige Buchungsnummer.")
        else:
            ###prüefe gitts scho e rechnig für die Buechig
            existing_invoice = invoice_manager.get_invoice_by_booking_id(booking_id)
            if existing_invoice:
                print("Für diese Buchung existiert bereits eine Rechnung.")
            else:
                issue_date = date.today()
                total_amount = selected_booking.total_amount
                invoice_status = "Offen"

                invoice = Invoice(
                    invoice_id=None,
                    booking=selected_booking,
                    issue_date=issue_date,
                    total_amount=total_amount,
                    invoice_status=invoice_status
                    )

                invoice_id = invoice_manager.create_invoice(invoice)
                print(f"Rechnung erfolgreich erstellt (Rechnungsnummer: {invoice_id}) für Buchung {booking_id}")
                print(f"Betrag: {total_amount} CHF | Ausgestellt am: {issue_date.strftime('%d.%m.%Y')} | Status: {invoice_status}")
        
        # User Story 6
        #Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige.
        #Hint: Sorgt für die entsprechende Invoice.
    
    guest_id = input_helper.input_valid_int("Bitte geben Sie Ihre Kundennummer ein: ", min_value=1)

    bookings = booking_manager.get_booking_by_guest_id(guest_id)

    ###Nur zukünftige und nicht stornierte Buchungen anzeigen
    open_bookings = [
        booking for booking in bookings
        if booking.check_in_date > date.today() and not booking.is_cancelled
    ]

    if not open_bookings:
        print("Sie haben keine stornierbaren Buchungen.")
    else:
        print("Stornierbare Buchungen:")
        for booking in open_bookings:
            hotel_name = booking.room.hotel.name if booking.room.hotel else "Unbekannt"
            print(f"Buchung ID: {booking.booking_id}, Aufenthalt: {booking.check_in_date} bis {booking.check_out_date}, Hotel: {hotel_name}")

        booking_id = input_helper.input_valid_int("Welche Buchung möchten Sie stornieren? (Buchungs-ID): ", min_value=1)
        selected_booking = next((booking for booking in open_bookings if booking.booking_id == booking_id), None)

        if not selected_booking:
            print("Ungültige Buchungsnummer.")
        else:
            confirm = input_helper.input_y_n(f"Möchten Sie Buchung {booking_id} wirklich stornieren? (y/n): ")
            if confirm:
                booking_manager.cancel_booking(booking_id)
                print("Buchung wurde storniert.")

                ### Gibt es eine Rechnung? 
                existing_invoice = invoice_manager.get_invoice_by_booking_id(booking_id)

                if not existing_invoice:
                    from model.invoice import Invoice
                    invoice = Invoice(
                        invoice_id=None,
                        booking=selected_booking,
                        issue_date=date.today(),
                        total_amount=0.0,
                        invoice_status="Storniert"
                    )
                    invoice_id = invoice_manager.create_invoice(invoice)
                    print(f"Stornorechnung erstellt (ID: {invoice_id}), Betrag: 0.0 CHF, Status: Storniert")
                else:
                    # Optional: Rechnung nachträglich stornieren
                    invoice_manager.cancel_invoice(existing_invoice.invoice_id)
                    print("Bestehende Rechnung wurde storniert.")
            else:
                print("Stornierung abgebrochen.")

    