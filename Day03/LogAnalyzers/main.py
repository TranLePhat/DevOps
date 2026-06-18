from log_reader import read_log_file
from log_parser import count_log_levels
from log_parser import get_system_status
from report import print_report


def main():
    log_file_path = "logs/app.log"

    log_lines = read_log_file(log_file_path)

    log_counts = count_log_levels(log_lines)

    system_status = get_system_status(log_counts)

    print_report(log_counts, system_status)


if __name__ == "__main__":
    main()