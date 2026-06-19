def read_config(file_path):

    config = {}

    with open(file_path, "r") as file:

        for line in file:

            line = line.strip()

            if "=" in line:

                key, value = line.split("=")

                config[key] = value

    return config