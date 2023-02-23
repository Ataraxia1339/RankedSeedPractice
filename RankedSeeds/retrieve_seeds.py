try:
    import requests
except ModuleNotFoundError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests


def request_page(uuid, page):
    seeds = 0
    response = requests.get(f"https://mcsrranked.com/api/users/{uuid}/matches?page={page}")
    if not response.json()["data"]:
        if not page:
            print("User has not played MCSR Ranked.")
        return 0
    with open("seeds.txt", "a") as f:
        for dic in response.json()["data"]:
            f.write(dic["match_seed"] + "\n")
            seeds += 1
    return seeds


def request_uuid(uuid):
    page_number, seed_count = 0, 0
    while 1:
        response = request_page(uuid, page_number)
        if not response:
            break
        seed_count += response
        page_number += 1
    return page_number, seed_count


def get_uuid(ign):
    return requests.get(f"https://api.mojang.com/users/profiles/minecraft/{ign}").json()["id"]


def request_user(ign):
    with open("seeds.txt", "w") as f:
        f.write("")
    print(f"Retrieving seeds played by {ign}...")
    pages, seeds = request_uuid(get_uuid(ign))
    print(f"Retrieved all {seeds} seeds played by {ign}.")


if __name__ == "__main__":
    request_user(input("Enter the user's IGN: "))
    input("Press Enter to exit. ")