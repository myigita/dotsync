import sys
import subprocess

argv = sys.argv[1:]
argc = len(argv)
saved_files_directory = "dotfiles"
file_list = "files_dotsync"
verbose = 0

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, shell=True, capture_output=True)
        if verbose:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while running command: {e}")
        print(f"Error info: {e.stderr}")

def install():
    repo = input("Please input the repo address\n(Example: 'git@github.com:<name>/<repo>.git' or 'https://github.com/<user>/<repo>.git'):")
    run_command("git init " + repo)
    run_command("git remote add origin " + repo)
    run_command("git pull origin main")

def create():
    repo = input("Please input the repo address\n(Example: 'git@github.com:<name>/<repo>.git' or 'https://github.com/<user>/<repo>.git'):")
    run_command("touch files_dotsync")
    run_command("touch README.md")
    run_command("echo Created by Dotsync > README.md")
    run_command("mkdir " + saved_files_directory)
    run_command("touch "+ saved_files_directory + "/.gitkeep")
    run_command("git init")
    run_command("git remote add origin " + repo)
    run_command("git add " + file_list)
    run_command("git add " + saved_files_directory)
    run_command('git commit -m "dotsync install commit"')
    run_command("git push -u origin main")


def clean():
    run_command("rm -rf .git")
    run_command("rm -r dotfiles")
    run_command("rm README.md")
    run_command("rm " + file_list)

def reinstall():
    clean()
    install()

def main():
    if argc == 1:
        if argv[0] == "install":
            install()
        elif argv[0] == "create":
            create()
        elif argv[0] == "clean":
            clean()
        elif argv[0] == "reinstall":
            reinstall()
        else:
            print(f"Unknown argument '{argv[0]}'")
    else:
        print(f"Invalid argument count. Use only 'install', 'clean' or 'reinstall' as arguments. Example usage of the program:\npython3 install_dotsync.py install")
    pass

if __name__ == "__main__":
    main()
