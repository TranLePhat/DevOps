def count_log_levels(log_lines):
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in log_lines:
        if line.startswith("INFO"):
            log_counts["INFO"] += 1

        elif line.startswith("WARNING"):
            log_counts["WARNING"] += 1

        elif line.startswith("ERROR"):
            log_counts["ERROR"] += 1

    return log_counts


def get_system_status(log_counts):
    if log_counts["ERROR"] > 0:
        return "Critical"

    elif log_counts["WARNING"] > 0:
        return "Warning"

    else:
        return "Healthy"