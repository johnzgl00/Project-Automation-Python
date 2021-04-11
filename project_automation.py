import os
from time import sleep
path = os.getcwd()
dirname = str(input("Project Name: "))
os.mkdir(dirname)
os.chdir(dirname)
open("ReadMe.md","w")
open("ReadMe.md","w").close()
print("Directory Created")
print("ReadMe Created")
answer = str(input("Do you want to add a file (yes/no): "))
if (answer == "yes"):
	filename = str(input("File's name with extension: "))
	open(filename, "w")
	open(filename, "w").close()
	print("File added")
	print("Exiting")
	sleep(1)
else :
	print("Exiting")
	sleep(1)