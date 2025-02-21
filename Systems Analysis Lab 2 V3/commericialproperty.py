from property import Property
import status  
import purpose  
import restype  

class CommericialProperty(Property):
    def __init__(self, property_id, address, location, asking_price, square_meters, status, description, unit_type, residential_type, no_bedrooms):
        super().__init__(property_id, address, location, asking_price, square_meters, status)
        self.__description = description
        self.__unit_type = unit_type
        self.__residential_type = residential_type  
        self.__no_bedrooms = no_bedrooms  

    def getDescription(self):
        return self.__description
    
    def setDescription(self, new_description):
        self.__description = new_description

    def getUnitType(self):
        return self.__unit_type
    
    def setUnitType(self, new_unit_type):
        self.__unit_type = new_unit_type

    def showDetails(self):
        statusStr = ""
        if self._status == status.Status.FORSALE:
            statusStr = "For Sale"
        elif self._status == status.Status.SALEAGREED:
            statusStr = "Sale Agreed"
        elif self._status == status.Status.SOLD:
            statusStr = "Sold"
        elif self._status == status.Status.UNDEROFFER:
            statusStr = "Under Offer"  
        elif self._status == status.Status.WITHDRAW:
            statusStr = "Withdrawn"  

        res_typeStr = ""  

       
        if self.__residential_type == restype.Res_type.APARTMENT:
            res_typeStr = "Apartment"
        elif self.__residential_type == restype.Res_type.DETACHED:
            res_typeStr = "Detached"
        elif self.__residential_type == restype.Res_type.DUPLEX:
            res_typeStr = "Duplex"
        elif self.__residential_type == restype.Res_type.SEMIDETACHED:
            res_typeStr = "Semi-Detached"
        elif self.__residential_type == restype.Res_type.TERRACED:
            res_typeStr = "Terraced"

        purposeStr = ""  

        # Check unit type
        if self.__unit_type == purpose.Purpose.BAR:
            purposeStr = "Bar"
        elif self.__unit_type == purpose.Purpose.FACTORY:
            purposeStr = "Factory"
        elif self.__unit_type == purpose.Purpose.HOTEL:
            purposeStr = "Hotel"
        elif self.__unit_type == purpose.Purpose.OFFICE:
            purposeStr = "Office"
        elif self.__unit_type == purpose.Purpose.RETAIL:
            purposeStr = "Retail"
        elif self.__unit_type == purpose.Purpose.WAREHOUSE:
            purposeStr = "Warehouse"

        
        print("Property ID: ", self._property_id)
        print("Address: ", self._address)
        print("Location: ", self._location)
        print("Asking Price: €", self._asking_price)
        print("Square Meters: ", self._square_meters)
        print("Status: ", statusStr)
        print("No. of Bedrooms: ", self.__no_bedrooms)
        print("Residential Type: ", res_typeStr)  
        print("Unit Type:", purposeStr)  
        print("Description: ", self.__description)
        print("-------------------------")
        print()
