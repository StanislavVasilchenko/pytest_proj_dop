def get_val(collection, key, default='git'):
    try:
        return collection[key]
    except KeyError:
        return default
