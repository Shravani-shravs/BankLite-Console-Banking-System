import json
import os

def load_users(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as f:
        return json.load(f)

def save_users(filepath, users):
    with open(filepath, 'w') as f:
        json.dump(users, f, indent=4)
