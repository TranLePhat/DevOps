def print_report(server_name, cpu, ram, disk, status):
    print("\nSERVER HEALTH REPORT")
    print("Server Name :", server_name)
    print("CPU Usage   :", str(cpu) + "%")
    print("RAM Usage   :", str(ram) + "%")
    print("Disk Usage  :", str(disk) + "%")
    print("Status      :", status)
