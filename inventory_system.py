"""
Inventory Management System Module.

This module provides functions for managing inventory stock data,
including adding, removing, and querying items.
"""

import json
from datetime import datetime


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item (str): The item name to add. Defaults to "default".
        qty (int): The quantity to add. Defaults to 0.
        logs (list): Optional list to append log messages. Defaults to None.
    """
    if logs is None:
        logs = []
    if not isinstance(item, str):
        print("Error: Item name must be a string.")
        return
    if not isinstance(qty, (int, float)):
        print("Error: Quantity must be a number.")
        return

    stock_data = load_data()
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    save_data(stock_data)


def remove_item(item, qty):
    """
    Remove a specified quantity of an item from inventory.

    Args:
        item (str): The item name to remove.
        qty (int): The quantity to remove.
    """
    stock_data = load_data()
    try:
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
        else:
            print(f"Item '{item}' not found.")
    except (KeyError, ValueError) as err:
        print(f"Error while removing item: {err}")
    save_data(stock_data)


def get_qty(item):
    """
    Get the quantity of an item in inventory.

    Args:
        item (str): The item name to query.

    Returns:
        int: The quantity of the item.
    """
    stock_data = load_data()
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file_name (str): The file path to load from.
            Defaults to "inventory.json".

    Returns:
        dict: Loaded inventory data.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except FileNotFoundError:
        print("Data file not found. Starting with empty inventory.")
        return {}
    except json.JSONDecodeError as err:
        print(f"Error loading data: {err}")
        return {}


def save_data(stock_data, file_name="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        stock_data (dict): The data to save.
        file_name (str): The file path to save to.
            Defaults to "inventory.json".
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
    except OSError as err:
        print(f"Error saving data: {err}")


def print_data():
    """
    Print a report of all items in inventory.
    """
    stock_data = load_data()
    print("\nItems Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """
    Check for items below a threshold quantity.

    Args:
        threshold (int): The threshold quantity. Defaults to 5.

    Returns:
        list: A list of items below the threshold.
    """
    stock_data = load_data()
    result = [item for item, qty in stock_data.items() if qty < threshold]
    return result


def main():
    """
    Main function to demonstrate inventory operations.
    """
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    print_data()
    print("Eval function removed for security.")


if __name__ == "__main__":
    main()
