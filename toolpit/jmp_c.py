import os, sys
from typing import List
import threading

f = open("commandlist.txt", "r").read()
print(f)
command = f.splitlines()

def run_command():
	for i in range(len(command)):
		threading.Thread(target=os.system(f"{command[i]}"))

def main():
	run_command()


threading.Thread(target=main).start()
