import datetime
import json


def add_drop(data):
    with open("config.json", "r") as file:
        in_data = json.load(file)
    with open("config.json", "w") as file:
        in_data["drop"] = data
        json.dump(in_data, file)


def add_info(data):
    with open("config.json", "r") as file:
        in_data = json.load(file)
    with open("config.json", "w") as file:
        in_data["info"] = data
        json.dump(in_data, file)


def add_items(data):
    with open("config.json", "r") as file:
        in_data = json.load(file)
        in_data["items"] = data
    with open("config.json", "w") as file:
        json.dump(in_data, file)


def get_items():
    with open("config.json", "r") as file:
        in_data = json.load(file)
    if "items" in in_data:
        return in_data["items"]
    return False


def get_info():
    with open("config.json", "r") as file:
        in_data = json.load(file)
    if "info" in in_data:
        return in_data["info"]
    return False


def get_drop():
    with open("config.json", "r") as file:
        in_data = json.load(file)
    if "drop" in in_data:
        return in_data["drop"]
    return False


add_drop({'drop_date': (2020, 11, 12), 'timer': 1})