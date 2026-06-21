from GitHubCheck.github_api import get_user_data
from GitHubCheck.report import print_report


def main():

    username = input("Enter GitHub username: ")

    user_data = get_user_data(username)

    if user_data is None:
        print("User not found.")
        return

    print_report(user_data)


if __name__ == "__main__":
    main()