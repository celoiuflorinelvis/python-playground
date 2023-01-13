import reprlib
print( reprlib.repr(set('supercalifragilisticexpialidocious')) )


import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)


import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))


import locale
#locale.setlocale(locale.LC_ALL, 'English_United States.1252')
locale.setlocale(locale.LC_ALL)
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
#locale.format("%d", x, grouping=True)
print( locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
)


from string import Template
t = Template('${village}folk send $$10 to $cause.')
print( t.substitute(village='Nottingham', cause='the ditch fund') )

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
#print( t.substitute(d) )
print( t.safe_substitute(d) )


import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = "%"

fmt = "Florin_%n-%d%f"
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.safe_substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


import zipfile, threading

class BatchArchive(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    
    def run(self):
        f = zipfile.ZipFile(self.outfile, "w", zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print("\nFile was archived.\n")

backgroundJob = BatchArchive("data.json", "data.zip")
#backgroundJob.start()
print("Starting archiving ...")

#backgroundJob.join()
print("DONE")


from decimal import *

print( round(Decimal('0.70') * Decimal('1.05'), 2) )
print( Decimal('1.00') % Decimal('.10') )
print( 1.00 % 0.10 )
print( Decimal('1.0') == 1.0 )
print( sum([Decimal('0.1')]*10) == Decimal('1.0') )
print( sum([0.1]*10) == 1.0 )


from array import array

"""
Type code C Type Minimum size in bytes 
'b' signed integer 1 
'B' unsigned integer 1 
'u' Unicode character 2 (see note) 
'h' signed integer 2 
'H' unsigned integer 2 
'i' signed integer 2 
'I' unsigned integer 2 
'l' signed integer 4 
'L' unsigned integer 4 
'q' signed integer 8 (see note) 
'Q' unsigned integer 8 (see note) 
'f' floating point 4 
'd' floating point 8
"""
a_B = array('B',  [1, 2, 3, 4, 5])
print(f"size_B: {a_B.__sizeof__()}")

a_L = array('L',  [1, 2, 3, 4, 5])
print(f"size_L: {a_L.__sizeof__()}")


from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())


import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, "ruby"))
print(f"scores = {scores}")


from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heapify(data)                      # rearrange the list into heap order
print(data)

heappush(data, -5)                 # add a new entry
print(data)

[heappop(data) for i in range(3)]  # fetch the three smallest entries
print(data)


