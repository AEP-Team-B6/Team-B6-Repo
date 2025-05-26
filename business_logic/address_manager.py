import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.address import Address

class AddressManager:
    def __init__(self):
        self.addresses = []
        self._next_id = 1

    def add_address(self, street:str, zip_code:int, city:str) -> Address:
        #if not all([street, zip_code, city]):
        #    raise ValueError("All address fields must be provided")

        for addr in self.addresses:
            if (addr.street == street and
                addr.zip_code == zip_code and
                addr.city == city):
                print("Address already exists – returning existing one.")
                return addr
        
        new_address = Address(self._next_id, street, zip_code, city)

        if new_address in self.addresses:
            print("Address already exists")
            return

        self.addresses.append(new_address)
        self._next_id += 1
        print("Address has been added")

#Testing
manager_test = AddressManager()
manager_test.add_address("Am Bach 3", 5502, "Hunzenschwil")
manager_test.add_address("Am Bach 3", 5502, "Hunzenschwil")

'''
    def del_address():
        pass

    
    def read_all_address():
        pass

    def update_address():
        pass


    def validate_address():
        pass


    def assign_address_to_guest():
        pass
'''