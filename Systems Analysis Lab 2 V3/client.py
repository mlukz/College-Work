class Client:
    def __init__(self, client_id, client_name, phone_no, email):
        self.__client_id = client_id
        self.__client_name = client_name
        self.__phone_no = phone_no
        self.__email = email 

    def getClient_id(self):
        return self.__client_id
    
    def setClient_id(self, new_client_id):
        self.__client_id = new_client_id

    def getClient_name(self):
        return self.__client_name
        
    def setClient_name(self, new_client_name):
        self.__client_name = new_client_name

    def getClient_phone_no(self):
        return self.__phone_no
    
    def setClient_phone_no(self, new_phone_no):
        self.__phone_no = new_phone_no

    def getClient_email(self):
        return self.__email
    
    def setClient_email(self, new_client_email):
        self.__email = new_client_email

    def __str__(self):
        return f"""Client Details\n\tId: {self.__client_id}\n\tName: {self.__client_name}
        Phone No: {self.__phone_no}\n\tEmail: {self.__email}
        --------------------------------------------------------------------------------------\n"""