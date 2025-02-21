import property
import client 

class Viewing:
    def __init__(self, viewing_id, date_time, property, client, offer_price, comments):
        self.__viewing_id = viewing_id
        self.__date_time = date_time
        self.__property = property
        self.__client = client
        self.__offer_price = offer_price
        self.__comments = comments


    def getViewing_id(self):
        return self.__viewing_id
    
    def setViewing_id(self, new_viewing_id):
        self.__viewing_id = new_viewing_id

    def getDate_time(self):
        return self.__date_time

    def setDate_time(self, new_date_time):
        self.__date_time = new_date_time

    def getProperty(self):
        return self.__property
    
    def setProperty(self, new_property):
        self.__property = new_property

    def getClient(self):
        return self.__client
    
    def setClient(self, new_client):
        self.__client = new_client
    
    def getOffer_prices(self):
        return self.__offer_price

    def setOffer_prices(self, new_offer_price):
        self.__offer_price = new_offer_price

    def getComments(self):
        return self.__comments
    
    def setComments(self, new_comments):
        self.__comments = new_comments

    def __str__(self):
        return f"""Viewing Details\n\tId: {self.__viewing_id}\n\tDate & Time: {self.__date_time}
        Property ID: {self.__property.getProperty_id()}\n\tAddress: {self.__property.getAddress()}
        Client ID: {self.__client.getClient_id()}\n\tClient Name: {self.__client.getClient_name()}
        Offer Price €: {self.__offer_price}\n\tComments: {self.__comments}
        -----------------------------------------------------------\n"""
