import json
from encryption import encrypt_data, decrypt_data

FILE = "storage.json"


def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_password(site, username, password):

    data = load_data()

    encrypted_password = encrypt_data(password)

    data[site] = {
        "username": username,
        "password": encrypted_password
    }

    save_data(data)


def view_password(site):

    data = load_data()

    if site in data:

        username = data[site]["username"]

        encrypted_password = data[site]["password"]

        password = decrypt_data(encrypted_password)

        return username, password

    else:
        return None


def delete_password(site):

    data = load_data()

    if site in data:

        del data[site]

        save_data(data)

        return True

    return False


def list_sites():

    data = load_data()

    return list(data.keys())
