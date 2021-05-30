import os, sys
from typing import List
import threading
import jmpfile as com

def run_command():
	for i in range(len(com.command)):
		threading.Thread(target=os.system(f"{com.command[i]}"))

def main():
	run_command()


threading.Thread(target=main).start()
