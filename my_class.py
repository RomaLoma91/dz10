class Field:
    def __init__(self, value=None):
        self.name = None
        self.value = value

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, index):
        del self.phones[index]

    def edit_phone(self, index, new_phone):
        self.phones[index].value = new_phone

class AddressBook:
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError('Only Record objects can be added to AddressBook')
        if not record.name.value:
            raise ValueError('Record name can not be empty')
        self.data[record.name.value] = record

    def delete_record(self, name):
        del self.data[name]

    def edit_record(self, name, new_record):
        if not isinstance(new_record, Record):
            raise ValueError
