def login(users, name):
    for user in users:
        if user['name'].lower() == name.lower():
            return user['id']
    return None

def register(users, name):
    new_id = max([u['id'] for u in users], default=1000) + 1
    users.append({'id': new_id, 'name': name})
    return new_id
