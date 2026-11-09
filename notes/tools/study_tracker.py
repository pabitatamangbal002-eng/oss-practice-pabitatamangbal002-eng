import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True)
args = parser.parse_args()

subjects = [
    ["Python", "Learning"],
    ["GitHub", "Practicing"],
    ["Open Source", "Exploring"]
]

print(f"\nWelcome to {args.name}'s Study Tracker!")
print(tabulate(subjects, headers=["Subject", "Status"], tablefmt="grid"))
print("\nKeep learning and keep growing!")