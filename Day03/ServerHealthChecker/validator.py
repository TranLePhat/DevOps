def validate_percentage(value):
    try:
        number = int(value)

        if number < 0 or number > 100:
            return None

        return number

    except ValueError:
        return None