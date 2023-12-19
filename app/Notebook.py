import json

class Notebook:
    def __init__(self):
        self.notes = {}
        self.load_notes()

    def add_note(self, note, tag):
        note_id = len(self.notes) + 1
        self.notes[note_id] = {"note": note, "tag": tag}
        self.save_notes()
        print(f"Note added with ID: {note_id}")

    def delete_note(self, note_id):
        if note_id in self.notes:
            del self.notes[note_id]
            self.save_notes()
            print(f"Note with ID {note_id} deleted.")
        else:
            print("Note not found.")

    def edit_note(self, note_id, new_note, new_tag):
        if note_id in self.notes:
            self.notes[note_id] = {"note": new_note, "tag": new_tag}
            self.save_notes()
            print(f"Note with ID {note_id} updated.")
        else:
            print("Note not found.")

    def find_notes(self, tag):
        return {id: note for id, note in self.notes.items() if note['tag'] == tag}

    def save_notes(self):
        with open('notes.json', 'w') as file:
            json.dump(self.notes, file)

    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                self.notes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.notes = {}
