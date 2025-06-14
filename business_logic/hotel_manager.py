import model
import data_access
from model import Hotel, Room, Room_Type, Address


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()
   
    # Used in User Story 1.5
    def find_hotel_by_search_params(self, search_params: list) -> list[list[Hotel], list[Room], list[Address], list[Room_Type]]:
        """Findet Hotels basierend auf verschiedenen Suchparametern (Filter-Suche)."""
        return self.__hotel_da.find_hotel_by_search_params(search_params)
    
    # Used in User Story 1.6
    def read_all_hotels(self):
        """Liest alle Hotels aus der Datenbank."""
        return self.__hotel_da.get_all_hotels()
    
    # Used in User Story 3.1
    def add_hotel(self, hotel: Hotel) -> int:
        """Fuegt ein neues Hotel hinzu und gibt dessen ID zurueck."""
        return self.__hotel_da.add_hotel(
            name=hotel.name,
            address_id=hotel.address.address_id,
            stars=hotel.stars)
    
    # Used in User Story 3.2
    def delete_hotel(self, hotel_id: int) -> bool:
         """Loescht ein Hotel anhand der ID."""
         return self.__hotel_da.delete_hotel(hotel_id)
    
    # Used in User Story 4
    def find_hotel_by_name_and_time(self, name_and_time: list) -> list[list[Hotel], list[Room_Type], list[Room]]:
        """Findet Hotels basierend auf Name und Zeitraum (fuer Buchung)."""
        return self.__hotel_da.find_hotel_by_name_and_time(name_and_time)
        
    #Used in User Story 9
    def read_hotel_by_id(self, hotel_id:int):
        """Liest ein Hotel basierend auf der Hotel-ID."""
        return self.__hotel_da.get_hotel_by_id(hotel_id)
    
    # Used in User Story 10 und 3.3
    def update_hotel(self, id, attribute, new_value):
        """Aktualisiert ein bestimmtes Attribut eines Hotels."""
        return self.__hotel_da.update_hotel(id, attribute, new_value)
    
    #Used in User Story DB 3
    def read_hotel_by_room_id(self, room_id:int):
        """Findet das zugehoerige Hotel anhand einer Zimmer-ID."""
        return self.__hotel_da.get_hotel_by_room_id(room_id)  