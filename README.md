**Dotsync** is a project that aims to make syncing your dotfiles easier.

## Installation:
- Download the release and extract the folder inside and put the files inside it, in the folder where you want you dotfiles to be saved 
- Create an empty repo on GitHub (no README.md)
- Run "python3 install_dotsync.py create" if this is your first time using the program or "python3 install_dotsync install" if you want to download your dotfiles 
- Provide the remote URL for your repo when the program asks for it

## Usage:
- First you must add a dotfile to be synced using: "python3 dotsync.py -add ~/example_folder/example_file.file"
- Then you can run "python3 dotsync.py" to automatically copy the file and push it to your repo
- You can also use "python3 dotsync.py -help" for help

## TODO
- Ability to automatically install your dotfiles after downloading them
