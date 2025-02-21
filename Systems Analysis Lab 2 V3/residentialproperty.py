from property import *

class ResidentialProperty(Property):
    def __init__(self, property_id, address, location, asking_price, square_meters, status, no_bedrooms, residential_type):
        super().__init__(property_id, address, location, asking_price, square_meters, status)
        self.__no_bedrooms = no_bedrooms        # private attribute
        self.__residential_type = residential_type  # private

    def getNoBedrooms(self):
        return self.__no_bedrooms

    def setNoBedrooms(self, new_no_bedrooms):
        self.__no_bedrooms = new_no_bedrooms

    def getResidential_type(self):
        return self.__residential_type

    def setResidential_type(self, new_residential_type):
        self.__residential_type = new_residential_type

    def showDetails(self):
        print("Property ID: ", self._property_id)
        print("Address: ", self._address)
        print("Location: ", self._location)
        print("Asking Price: ", self._asking_price)
        print("Square Meters: ", self._square_meters)
        print("Status: ", self._status)
        print("No. of Bedrooms: ", self.__no_bedrooms)
        print("Residential Property Type: ", self.__residential_type)
        print("------------------------------------")
        print()

