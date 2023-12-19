from app.Fields import Name, Phone, Email, Address, Birthday, Note

class Contact:
    def __init__(self, name, phone=None, birthday=None, email=None, address=None, note=None):
        self.name = Name(name)
        self.phone = Phone(phone) if phone else None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
        self.birthday = Birthday(birthday) if birthday else None
        self.note = Note(note) if note else None

    def add_note(self, note):
        self.notes = Note(note)

    def update_note(self, new_note):
        self.note = Note(new_note)