import json
import string
import random
from pathlib import Path


class Bank:
    def __init__(self, db_file='data.json'):
        self.db_file = db_file
        self.data = self._load_data()

    def _load_data(self):
        if Path(self.db_file).exists():
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return []

    def _save_data(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def _generate_account_number(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=7))

    def create_account(self, name, pin):
        acc = self._generate_account_number()
        self.data.append({
            'account': acc,
            'name': name,
            'pin': pin,
            'balance': 0
        })
        self._save_data()
        return acc

    def login(self, acc, pin):
        for user in self.data:
            if user['account'] == acc and user['pin'] == pin:
                return user['name']
        return None

    def deposit(self, acc, amount):
        for user in self.data:
            if user['account'] == acc:
                user['balance'] += amount
                self._save_data()
                return True
        return False

    def withdraw(self, acc, amount):
        for user in self.data:
            if user['account'] == acc and user['balance'] >= amount:
                user['balance'] -= amount
                self._save_data()
                return True
        return False

    def update_account(self, acc, name=None, pin=None):
        for user in self.data:
            if user['account'] == acc:
                if name:
                    user['name'] = name
                if pin:
                    user['pin'] = pin
                self._save_data()
                return True
        return False

    def close_account(self, acc):
        for i, user in enumerate(self.data):
            if user['account'] == acc:
                self.data.pop(i)
                self._save_data()
                return True
        return False
