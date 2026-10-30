"""
utils.py
---------
Handles reading from and writing to data.json.
Kept separate from model.py and budget_tracker.py so that "how saving
works" stays independent of "what the program does."
"""

import json
import os

FILENAME = "data.json"


def load_data():
    """
    Load saved data from data.json.

    Returns a default, empty structure if the file doesn't exist yet
    (first run) or if it exists but contains invalid/corrupted JSON.
    """
    default_data = {"transactions": [], "budget_limit": None}

    if not os.path.exists(FILENAME):
        return default_data

    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: data.json was unreadable. Starting fresh.\n")
        return default_data


def save_data(data):
    """
    Save transactions and budget_limit to data.json.

    'data' is expected to be a dictionary with "transactions" (a list
    of plain dictionaries) and "budget_limit" (a number or None).
    """
    data_to_save = {
        "transactions": data.get("transactions", []),
        "budget_limit": data.get("budget_limit"),
    }
    with open(FILENAME, "w") as file:
        json.dump(data_to_save, file, indent=4)