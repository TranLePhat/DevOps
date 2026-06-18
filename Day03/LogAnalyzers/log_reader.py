def read_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            return lines

    except FileNotFoundError:
        print("Error: Log file not found.")
        return []