def classify_status(cpu, ram, disk):
    if cpu >= 90 or ram >= 90 or disk >= 90:
        return "Critical"

    elif cpu >= 70 or ram >= 70 or disk >= 70:
        return "Warning"

    else:
        return "Healthy"