# Create a dictionary with elements in the list as values and the indices as keys.
# Given a list of items, create a dictionary with the indices as keys and the items as items.

def create_indexed_dict(items: list) -> dict:

    return dict(enumerate(items))
    
