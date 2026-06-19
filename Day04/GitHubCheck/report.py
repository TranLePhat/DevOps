def get_account_status(followers):

    if followers >= 10000:
        return "Popular Account"

    elif followers >= 1000:
        return "Growing Account"

    else:
        return "Normal Account"


def print_report(data):

    status = get_account_status(data["followers"])

    print("\nGITHUB USER REPORT\n")

    print("Username      :", data["login"])
    print("Account Type  :", data["type"])
    print("Followers     :", data["followers"])
    print("Following     :", data["following"])
    print("Public Repos  :", data["public_repos"])

    print("\nStatus        :", status)
