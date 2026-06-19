from config_reader import read_config
from config_writer import write_config
from config_writer import backup_config

config = read_config("server.conf")

print("\nCurrent Configuration")

for key, value in config.items():
    print(f"{key} = {value}")

setting = input(
    "\nEnter setting to update: "
)

new_value = input(
    "Enter new value: "
)

config[setting] = new_value

backup_config(
    "server.conf"
)

write_config(
    "server.conf",
    config
)


## print(config)