import os


def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None

    except FileNotFoundError:
        return None, "Folder does not exist."

    except PermissionError:
        return None, "Permission denied."


def main():
    folders = input("Enter folder paths, separated by spaces: ").split()

    for folder in folders:
        print(f"\nFolder: {folder}")

        files, error = list_files_in_folder(folder)

        if error:
            print(f"Error: {error}")
        else:
            print("Files:")
            for file in files:
                print(f"- {file}")


if __name__ == "__main__":
    main()