from validator import validate_percentage


def get_server_name():
    return input("Enter server name: ")


def get_usage_value(metric_name):
    while True:
        value = input(f"Enter {metric_name} usage (%): ")

        validated_value = validate_percentage(value)

        if validated_value is not None:
            return validated_value

        print(f"Invalid {metric_name} usage. Please enter a number from 0 to 100.")