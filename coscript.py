from termcolor import colored
import sys
import os
import subprocess
import platform
import argparse

# VARIABLES
coscript_dir = f"{os.getenv('HOME')}/coscripts/"

def create(coscript):
    if not coscript_exists(coscript):
        coscript_path = coscript_dir + coscript + ".txt"
        open(coscript_path, "a").close()

        if platform.system() == 'Darwin':
            subprocess.call(('open', coscript_path))
        elif platform.system() == 'Windows':
            os.startfile(coscript_path)
        else:
            subprocess.call(('xdg-open', coscript_path))

    else:
        print(colored("[-] That CoScript already exists!", "red"))

def run(coscript):
    if coscript_exists(coscript):
        coscript_path = coscript_dir + coscript + ".txt"

        file = open(coscript_path, "r")

        for (index, line) in enumerate(file.readlines()):
            print(f"[+] Running command #{index + 1}: {line}")

            if os.system(line) != 0:
                print(colored(f"[-] Command '{line.strip()}' failed to execute", "red"))
                print(colored("[-] Quitting out of CoScript execution", "red"))
                sys.exit(0)

            print("\n")

        file.close()

        print("[+] CoScript ran successfully!")

    else:
        print(colored("[-] That CoScript doesn't exist!", "red"))

def update(coscript):
    if coscript_exists(coscript):
        coscript_path = coscript_dir + coscript + ".txt"

        if platform.system() == 'Darwin':
            subprocess.Popen(('open', coscript_path))

        elif platform.system() == 'Windows':
            os.startfile(coscript_path)
        else:
            subprocess.Popen(('xdg-open', coscript_path)).wait()

    else:
        print(colored("[-] That CoScript doesn't exist!", "red"))

def delete(coscript):
    if coscript_exists(coscript):
        os.remove(coscript_dir + coscript + ".txt")
        print(colored(f"[+] Successfully deleted CoScript '{coscript}'", "green"))

    else:
        print(colored("[-] That CoScript doesn't exist!", "red"))

def read(coscript):
    if coscript_exists(coscript):
        coscript_path = coscript_dir + coscript + ".txt"

        file = open(coscript_path, "r")

        print(file.read())

        file.close()

    else:
        print(colored("[-] That CoScript doesn't exist!", "red"))

def list_coscripts():
    for coscript in os.listdir(coscript_dir):
        print(coscript.split(".")[0])

command_map = {
    "create": create,
    "run": run,
    "update": update,
    "delete": delete,
    "read": read,
    "list": list_coscripts
}

def verify_coscript_dir():
    return os.path.exists(coscript_dir)

def coscript_exists(coscript_name):
    return os.path.exists(coscript_dir + coscript_name + ".txt")

def parse_function(args):
    # IF IT'S 'LIST'
    if args.function[0] == "list":
        list_coscripts()
    else:
        coscript_function = command_map.get(args.function[0])

        coscript_dir_exists = verify_coscript_dir()
        if not coscript_dir_exists:
            os.makedirs(coscript_dir)

        if coscript_function:
            coscript_function(args.name[0])
        else:
            parser.print_help()

parser = argparse.ArgumentParser(description="Coscript")

parser.add_argument("function",
                    help="CoScript function you want to run",
                    choices=["create", "run", "update", "delete", "list", "read"],
                    nargs='+',
                    metavar="function",
                    type=str
                )
parser.add_argument("name",
                    help="Name of CoScript to run function on",
                    nargs='+' if ("list" not in sys.argv) else '?',
                    metavar="name",
                    type=str
                )

if len(sys.argv) <= 1:
    sys.argv.append('--help')

args = parser.parse_args()
parse_function(args)
