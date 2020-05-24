import sys
import argparse

def create(coscript):
    print("create", coscript)

def run(coscript):
    print("run", coscript)

def update(coscript):
    print("update", coscript)

def delete(coscript):
    print("delete", coscript)

command_map = {
    "create": create,
    "run": run,
    "update": update,
    "delete": delete
}

def parse_function(args):
    coscript_function = command_map.get(args.function[0])

    if coscript_function:
        coscript_function(args.name[0])
    else:
        parser.print_help()

parser = argparse.ArgumentParser(description="Coscript")

parser.add_argument("function", help="CoScript function you want to run", choices=["create", "run", "update", "delete"], nargs='+', metavar="function", type=str)
parser.add_argument("name", help="Name of CoScript to run function on", nargs='+', metavar="name", type=str)

if len(sys.argv) <= 1:
    sys.argv.append('--help')

args = parser.parse_args()
parse_function(args)
