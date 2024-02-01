# imports for file handling and git commands

import sys # for argument handling
import shutil # for copy paste
import subprocess # for running git commands
import os # for checking if file is empty
from datetime import datetime # for the auto commitmsg

# vars
argv = sys.argv[1:]
argc = len(argv)
saved_files = "./dotfiles/"
saved_files_directory = "./dotfiles"
file_list = "./files_dotsync"
verbose = 0 

# read file locations from file and write if opened in write mode
# TODO write a install script

def save_file_location(): # saves provided file location to a file
    argv_locations = argv[1:]
    with open(file_list, "a") as file:
        for location in argv_locations:
            file.write(location + "\n")
    return 0

def copy_files():
    if os.path.getsize(file_list) == 0:
        print(f"You must add at least one file before syncing.")
        return 1
    with open(file_list, "r") as file:
        for line in file:
            source_file_location = line.strip()
            shutil.copy(source_file_location, saved_files)
            print(f"File copied from {source_file_location} to {saved_files}")
    return 0

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, shell=True, capture_output=True)
        if verbose:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while running command: {e}")
        print(f"Error info: {e.stderr}")


def upload_files(): # handles git commands
    if argc > 0:
        commit_msg = argv[0]
    else:
        curr_dt = datetime.now()
        commit_msg = curr_dt.strftime("%H:%M:%S %d.%m.%Y")
    run_command("git add files_dotsync")
    run_command("git add "+ saved_files_directory) # git add ./dotfiles/
    run_command('git commit -m "' + str(commit_msg) + '"')
    run_command("git push origin main")
    return 0

def help():
    print(f"Use without any arguments to copy saved files into a local folder and upload them to github\n")
    print("Use with the argument '-add' or '--a' to add files for uploading")
    sys.exit()

def main():
    if argc > 0:
        if argv[0] in ("-a","-add", "--a", "--add"):
            save_file_location()
        # elif argv[0] in ("-h", "-help", "--h", "--help"):
        else:
            help()
    else:
        copy_files()
        upload_files()
    return 0

if __name__ == "__main__":
    main()
