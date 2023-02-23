# RankedSeedPractice
Generates a list of seeds rolled by a specific user in MCSR Ranked, macro creates a world with a seed from that list each time a hotkey (default `Ctrl-R`) is pressed.

## Setup
- Install [Python 3](https://www.python.org/downloads/) and [AutoHotkey](https://www.autohotkey.com/) if you don't have them.
- Download and extract [RankedSeeds.zip](https://github.com/Ataraxia1339/RankedSeedPractice/releases/download/v1.0/RankedSeeds.zip). If you want to move one or more of the files to your Desktop (or some other location) for easy access, either move all the files, or create a shortcut on your Desktop that points to the script you want to run.
- Double-click `retrieve_seeds.py`. The first time you run this file, you may see an installation message in the window. That is Python installing the module `requests`, which is required to fetch the API from MCSR Ranked.
- You should see the following message:

<img src="https://user-images.githubusercontent.com/110107468/220834576-572be293-c238-4a13-af27-c41cf3241bde.png" width="45%"/>

- Enter the user's Minecraft username and press `Enter`. A list of seeds rolled by that user will be written to `seeds.txt`. _This overwites anything currently in `seeds.txt`._
- Press `Enter` to exit the program.

<img src="https://user-images.githubusercontent.com/110107468/220834692-5d6b5d12-8761-4705-9175-8812007d69b6.png" width="45%"/>

- If you would like to change the hotkey for creating a world with a practice seed (default is `Ctrl-R`), right-click `practice_seeds.ahk` and click "Edit Script".
- Edit the following part of the script highlighted in blue (`^` denotes `Ctrl`).

<img src="https://user-images.githubusercontent.com/110107468/220838134-9b630389-8c7a-40f4-aeae-077b70110803.png" width="30%"/>

- Once you're done, save the file and close it.
- Run `practice_seeds.ahk` by double-clicking it. Nothing should happen yet.
- Open Minecraft and go to the title screen. Make sure you have at least one world in your saves folder.
- Press `Ctrl-R` (or the hotkey you have changed it to). This should create a world with the first seed in `seeds.txt` and remove that seed from `seeds.txt`.
  - If `seeds.txt` is empty, a message box will appear and the program will exit. You will now have to repopulate `seeds.txt` by running `retrieve_seeds.py` with a different username.

## Known Issues
- Some runners have rolled the same seed multiple times. If they did not change the seed, that seed will show up as a duplicate in `seeds.txt`. This may be fixed in the future if I rewrite a bit of the code structure.
- If running `retrieve_seeds.py` results in a Permission Error (the program does not have permissions to write to seeds.txt), it might be caused by running the program from the command line. Try double-clicking the `retrieve_seeds.py` file instead.
- If the macro does not input a seed properly, you likely:
  - do not have at least one world in your saves folder.
  - are not pressing the hotkey from the title screen.
  - have a button selected (possibly because you pressed `Tab`) on the title screen.
