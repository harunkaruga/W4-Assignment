# manual_sort.py
def sort_dicts_by_key_manual(items, key, reverse=False):
    """
    Manual implementation to sort a list of dictionaries by a key.
    - We create a shallow copy to avoid changing original list.
    - We ensure missing keys are treated as None and place them last.
    """
    # Defensive copy
    items_copy = items[:]
    # Define helper that returns a tuple that sorts missing keys last
    def sort_key(d):
        val = d.get(key, None)
        # Put None values at the end: we use (is_none, val) so that False < True
        return (val is None, val)
    items_copy.sort(key=sort_key, reverse=reverse)
    return items_copy
