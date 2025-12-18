def convert_unit_to_vnd(value, unit):
    if value is None:
        return None

    if unit == 'VND':
        return value * 10 ** 6
    return value
