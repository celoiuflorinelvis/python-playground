import os

print(f"Current dir. {os.getcwd()}")

os.mkdir("test")
os.chdir("test")
print(f"Current dir. {os.getcwd()}")
os.chdir("..")
os.rmdir("test")


import shutil
print( shutil.disk_usage(".") )


import glob
print(glob.glob("*.py"))


import argparse

parser = argparse.ArgumentParser(
    prog="top_lines", 
    description="Show top lines from a files"
)
parser.add_argument("-l", "--lines", type=int, default=5)
parser.add_argument("filenames", nargs='+')

args = parser.parse_args()
print(f"args = {args}")

f = open(args.filenames[0], 'r')
no_lines = 0
while no_lines <= args.lines:
    print(f.readline())
    no_lines += 1
f.close()


import sys
#sys.exit()
sys.stderr.write("Error from stderr.\n")
sys.audit("ERROR", 1)


import re
print( re.findall(r"\bX[a-z]*", "Aceasta este o variabila Xabc") )

email_pattern = r"[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9\.\-\_]+\.[a-zA-Z]+"
print( re.fullmatch(email_pattern, "email@email.com") )
print( re.fullmatch(email_pattern, "email.NaMe_ion12@email.com") )

print("Ion 2 years old".replace("2", "two"))








