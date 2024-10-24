import json
import os
import hashlib

class Database:
    def __init__(self, filename='users.json'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({}, f)

    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def insert(self, name, email, password):
        hashed_password = self.hash_password(password)

        try:
            with open(self.filename, 'r') as rf:
                users = json.load(rf)

            if email in users:
                return 0

            users[email] = {"name": name, "password": hashed_password}
            with open(self.filename, 'w') as wf:
                json.dump(users, wf)

            return 1

        except Exception as e:
            print(f"Error while inserting user: {e}")
            return -1

    def search(self, email, password):
        try:
            with open(self.filename, 'r') as rf:
                users = json.load(rf)

            if email in users:
                if users[email]["password"] == self.hash_password(password):
                    return 1
            return 0

        except Exception as e:
            print(f"Error while searching for user: {e}")
            return -1
