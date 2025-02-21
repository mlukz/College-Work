import status

class Property:
    def __init__(self, property_id, address, location, asking_price, square_meters, status):
        self._property_id = property_id
        self._address = address
        self._location = location
        self._asking_price = asking_price
        self._square_meters = square_meters
        self._status = status
    
    def getProperty_id(self):
        return self._property_id  
    
    def setProperty_id(self, new_property_id):
        self._property_id = new_property_id  
    
    def getAddress(self):
        return self._address  
    
    def setAddress(self, new_address):
        self._address = new_address  
    
    def getLocation(self):  
        return self._location  

    def setLocation(self, new_location):
        self._location = new_location     

    def getAsking_price(self):
        return self._asking_price  
    
    def setAsking_price(self, new_asking_price):
        self._asking_price = new_asking_price  

    def getSquare_meters(self):
        return self._square_meters  
    
    def setSquare_meters(self, new_square_meters):
        self._square_meters = new_square_meters  

    def getStatus(self):
        return self._status  
    
    def setStatus(self, new_status):
        self._status = new_status  

    def showDetails(self):
        print("Property ID: ", self._property_id)  # Fixed
        print("Address: ", self._address)  # Fixed
        print("Location: ", self._location)  # Fixed
        print("Asking Price : €", self._asking_price)  # Fixed
        print("Square Meters: ", self._square_meters)  # Fixed
        print("Status: ", self._status)  # Fixed
        print("-------------------------------------------------------")
        print()
