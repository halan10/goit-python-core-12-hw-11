from collections import UserDict
from datetime import datetime, date

        
        
class Field:
    def __init__(self, value):
        if not isinstance(value,str):
            raise ValueError("Value must be a string")
        self.__value = None
        self.value = value

    def __str__ (self)->str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)
    
    #setter and getter logic for the value attributes of the Field inheritors
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,value):
        self.__value = value
    
class Name(Field):
    pass

class Phone(Field):

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value (self,value):
        if not value.isdigit() or len(value) != 12:
            raise ValueError ("Invalid phone number")
        self.__value = value

class Birthday(Field):

    def __init__(self, value):
        self.__value = None
        self.value = value

        @property
        def value(self):
            return self.__value
        
        @value.setter
        def value(self, value):
            try:
                self.__value = datetime.strftime(value, '%d.%m.%Y')
            except ValueError:
                raise ValueError('Birthday format is :"dd.mm.yyyy"')

class Record:
    def __init__(self,name, phone = None, birthday=None):
        self.name = name
        self.phones = [] 
        self.birthday = birthday
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, index, phone):
        self.phones[index]=phone

    def days_to_birthday(self):
        today = datetime.now().date()
        if not self.birthday:
            return None
        bd = datetime.strftime('%d.%m.%Y').date()
        bd = bd.replace(year = datetime.now().year)
        if today > bd:
            bd = bd.replace(year=datetime.now().year+1)
            difference = bd - today
            return difference.days


    def __repr__(self) -> str:
        return ','.join([p.value for p in self.phones])

class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value]= record

    def paginator(self, page = 1):
        start = 0
        while True:
            result = list(self.data.values())[start:start + page]
            if not result:
                break
            yield result
            start += page
        
    def show_all(self):
        result = []
        for records in self.paginator():
            for record in records:
                result.append(str(record))
        return '\n'.join(result)

