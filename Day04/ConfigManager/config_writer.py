import shutil
import os

def backup_config(file_path):

    backup_number = 1

    while True:

        backup_file = (
            f"{file_path}.bak{backup_number}"
        )

        if not os.path.exists(
            backup_file
        ):
            break

        backup_number += 1

    shutil.copy(
        file_path,
        backup_file
    )

    print(
        f"Backup created: "
        f"{backup_file}"
    )

def write_config(
    file_path,
    config
):

    with open(
        file_path,
        "w"
    ) as file:

        for key, value in config.items():

            file.write(
                f"{key}={value}\n"
            )