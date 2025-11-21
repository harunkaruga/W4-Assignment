```python name=sort_by_key.py
def sort_by_key(list_of_dicts, key, reverse=False):
    """
    Sorts a list of dictionaries by a specific key.

    Parameters:
        list_of_dicts (list): List of dictionaries to sort.
        key (str): The key in the dictionary to sort by.
        reverse (bool): Whether to sort in descending order. Default is False.

    Returns:
        list: The sorted list of dictionaries.
    """
    return sorted(list_of_dicts, key=lambda x: x[key], reverse=reverse)

# Example usage:
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

sorted_people = sort_by_key(people, "age")
print(sorted_people)
```
