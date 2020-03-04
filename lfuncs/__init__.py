def find_startswith_in_list(prefix, list1):
    """Filters the given list so that only elements that
    start with the provided prefix will be returned.
    """
    return list(filter(lambda e: e.startswith(prefix), list1))

def find_endswith_in_list(suffix, list1):
    """Filters the given list so that only elements that
    end with the provided suffix will be returned.
    """
    return list(filter(lambda e: e.endswith(suffix), list1))

def split_lists(olist, prefix):
    """Splits a list into two lists and returns them as a tuple.
    The first list will contain all elements in the original list
    that start with the provided prefix. The second list will
    contain all other elements.

    Parameters:
    - olist: the list that should be separated into two lists
    - prefix: the prefix that should be used to separate the list
    """
    list1 = []
    list2 = []
    for e in olist:
        if e.startswith(prefix + " "):
            list1.append(e)
        else:
            list2.append(e)

    return list1, list2

def joke():
    """Prints a funny joke."""
    print('A foo walks into a bar, takes a look around and says "Hello World!"')
