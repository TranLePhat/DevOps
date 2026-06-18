import sys

from input_handler import get_server_name
from input_handler import get_usage_value

from health_checker import classify_status
from report import print_report


def show_help():
    print("""
usage: python3 main.py [-h|--help]

This script checks server health based on CPU, RAM, and Disk usage.

Usage:
  python3 main.py

Options:
  -h, --help    Show this help message and exit
""")


def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        show_help()
        return

    server_name = get_server_name()

    cpu = get_usage_value("CPU")
    ram = get_usage_value("RAM")
    disk = get_usage_value("Disk")

    status = classify_status(cpu, ram, disk)

    print_report(server_name, cpu, ram, disk, status)


if __name__ == "__main__":
    main()