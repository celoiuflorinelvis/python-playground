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


import math
math.pi
print(f"cos(60) = {math.cos(60)}")
print(f"cos(30) = {math.cos(30)}")
print(f"sin(PI/3) = {math.sin(math.pi / 3)}")
print(f"sin(PI/6) = {math.sin(math.pi / 6)}")


import random
print(f"Gauss = {random.gauss()}")
print(f"Random float = {random.random()}")
print(f'Choise = {random.choice(["one", "two", "three"])}')
print(f'Choises = {random.choices(["one", "two", "three"], k = 2)}')
print(f"Sample: {random.sample(range(100), 10)}")
print(f"RandomRange = {random.randrange(6, 10)}")


import statistics

#https://scipy.org>

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

print(f"mean = {statistics.mean(data)}")
print(f"variance = {statistics.variance(data)}")
print(f"median = {statistics.median(data)}")
print(f"correlation = {statistics.correlation(data, data)}")


from urllib.request import urlopen
with urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt") as response:
    for line in response:
        print(f"Line: {line.decode().rstrip()}")


from datetime import date

print(f"today = {date.today()}")
print(f'today_formatted = {date.today().strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")}')
print(f'diff = {( date.today() - date(2022, 12, 30) ).days}')


#zlib, gzip, bz2, lzma, zipfile and tarfile.
import zlib

s = b'witch which has which witches wrist watch'
s_compress = zlib.compress(s);

print(f"Compression: {len(s)} - {len(s_compress)}")
print(f"Compress text: {s_compress}")
print(f"Decompress text: {zlib.decompress(s_compress)}")
print(f"CRC Orig = {zlib.crc32(s)}")
print(f"CRC Decomp. = {zlib.crc32(zlib.decompress(s_compress))}")


from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())



