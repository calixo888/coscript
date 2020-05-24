import sys
import argparse

def create():
    print("create")

def run():
    print("run")

def update():
    print("update")

def delete():
    print("delete")

parser = argparse.ArgumentParser(description="Coscript")
subparsers = parser.add_subparsers()

parser_create = subparsers.add_parser("create", help="Create new coscript")
parser_create.set_defaults(func=create)
parser_run = subparsers.add_parser("run", help="Run a coscript")
parser_run.set_defaults(func=run)
parser_update = subparsers.add_parser("update", help="Update a coscript")
parser_update.set_defaults(func=update)
parser_delete = subparsers.add_parser("delete", help="Delete a coscript")
parser_delete.set_defaults(func=delete)

# parser.add_argument('coscript function', choices=["create", "run", "update", "delete"], metavar='create', type=str, nargs=1, help="COSCRIPT FUNCTION")

if len(sys.argv) <= 1:
    sys.argv.append('--help')

args = parser.parse_args()
args.func()
