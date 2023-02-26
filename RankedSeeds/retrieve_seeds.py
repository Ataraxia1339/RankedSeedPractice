try:
    import requests
except ModuleNotFoundError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests


def request_user(ign):
    with open("seeds.txt", "w") as f:
        f.write("")
    print(f"Retrieving seeds played by {ign}...")
    page, duplicates, seeds = 0, 0, []
    while 1:
        response = requests.get(f"https://mcsrranked.com/api/users/{ign}/matches?page={page}")
        if not response.json()["data"]:
            if not page:
                print("User has not played MCSR Ranked.")
            break
        for dic in response.json()["data"]:
            seed = dic["match_seed"]
            if seed in seeds:
                duplicates += 1
                continue
            seeds.append(seed)
        page += 1
    with open("seeds.txt", "a") as f:
        for i in seeds:
            f.write(i + "\n")
    print(f"Retrieved {len(seeds)} seeds played by {ign}, ignoring {duplicates} duplicate seeds.")


if __name__ == "__main__":
    request_user(input("Enter the user's IGN: "))
    input("Press Enter to exit. ")