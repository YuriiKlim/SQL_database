import redis
from datetime import datetime


class Notebook:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db, decode_responses=True)
        self.username = None

    def create_user(self):
        username = input("Enter a new username: ")
        if self.r.hexists(f"user:{username}", "password"):
            print("Username already exists.")
            return
        password = input("Enter a new password: ")
        self.r.hset(f"user:{username}", "password", password)
        print(f"User {username} created successfully.")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        stored_password = self.r.hget(f"user:{username}", "password")
        if stored_password and stored_password == password:
            print("Login successful!")
            self.username = username
        else:
            print("Invalid username or password.")

    def add_note(self):
        if not self.username:
            print("You must login first.")
            return
        note_id = self.r.incr(f"note_id:{self.username}")
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        timestamp = datetime.now().isoformat()
        note_key = f"note:{self.username}:{note_id}"
        self.r.hset(note_key, mapping={
            "title": title,
            "content": content,
            "timestamp": timestamp
        })
        self.r.rpush(f"notes:{self.username}", note_key)
        print("Note added successfully.")

    def delete_note(self):
        if not self.username:
            print("You must login first.")
            return
        note_id = input("Enter note ID to delete: ")
        note_key = f"note:{self.username}:{note_id}"
        if self.r.exists(note_key):
            self.r.delete(note_key)
            self.r.lrem(f"notes:{self.username}", 0, note_key)
            print("Note deleted successfully.")
        else:
            print("Note not found.")

    def edit_note(self):
        if not self.username:
            print("You must login first.")
            return
        note_id = input("Enter note ID to edit: ")
        note_key = f"note:{self.username}:{note_id}"
        if self.r.exists(note_key):
            title = input("Enter new note title: ")
            content = input("Enter new note content: ")
            timestamp = datetime.now().isoformat()
            self.r.hset(note_key, mapping={
                "title": title,
                "content": content,
                "timestamp": timestamp
            })
            print("Note edited successfully.")
        else:
            print("Note not found.")

    def view_note(self):
        if not self.username:
            print("You must login first.")
            return
        note_id = input("Enter note ID to view: ")
        note_key = f"note:{self.username}:{note_id}"
        note = self.r.hgetall(note_key)
        if note:
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            print(f"Timestamp: {note['timestamp']}")
        else:
            print("Note not found.")

    def view_all_notes(self):
        if not self.username:
            print("You must login first.")
            return
        note_keys = self.r.lrange(f"notes:{self.username}", 0, -1)
        if note_keys:
            for note_key in note_keys:
                note = self.r.hgetall(note_key)
                print(f"ID: {note_key.split(':')[-1]}")
                print(f"Title: {note['title']}")
                print(f"Content: {note['content']}")
                print(f"Timestamp: {note['timestamp']}")
                print("-----")
        else:
            print("No notes found.")

    def view_notes_by_time(self):
        if not self.username:
            print("You must login first.")
            return
        start_time = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
        end_time = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")
        note_keys = self.r.lrange(f"notes:{self.username}", 0, -1)
        if note_keys:
            for note_key in note_keys:
                note = self.r.hgetall(note_key)
                timestamp = datetime.fromisoformat(note['timestamp'])
                if start_time <= timestamp.isoformat() <= end_time:
                    print(f"ID: {note_key.split(':')[-1]}")
                    print(f"Title: {note['title']}")
                    print(f"Content: {note['content']}")
                    print(f"Timestamp: {note['timestamp']}")
                    print("-----")
        else:
            print("No notes found in the specified time range.")

    def search_notes_by_keywords(self):
        if not self.username:
            print("You must login first.")
            return
        keywords = input("Enter keywords to search (comma separated): ").split(',')
        note_keys = self.r.lrange(f"notes:{self.username}", 0, -1)
        if note_keys:
            for note_key in note_keys:
                note = self.r.hgetall(note_key)
                content = note['content']
                if all(keyword.strip().lower() in content.lower() for keyword in keywords):
                    print(f"ID: {note_key.split(':')[-1]}")
                    print(f"Title: {note['title']}")
                    print(f"Content: {note['content']}")
                    print(f"Timestamp: {note['timestamp']}")
                    print("-----")
        else:
            print("No notes found containing the specified keywords.")

    def run(self):
        while True:
            print("\nNotebook Menu:")
            print("1. Create new user")
            print("2. Login")
            print("3. Add note")
            print("4. Delete note")
            print("5. Edit note")
            print("6. View note")
            print("7. View all notes")
            print("8. View notes by time range")
            print("9. Search notes by keywords")
            print("enter. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.add_note()
            elif choice == '4':
                self.delete_note()
            elif choice == '5':
                self.edit_note()
            elif choice == '6':
                self.view_note()
            elif choice == '7':
                self.view_all_notes()
            elif choice == '8':
                self.view_notes_by_time()
            elif choice == '9':
                self.search_notes_by_keywords()
            elif choice == '':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    notebook = Notebook()
    notebook.run()
