#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("Argv(0): ", sys.argv[0])
    print("Argv(1): ", sys.argv[1])

    n = int(sys.argv[1])
else:
    n = 10

a,b =  0,1
while a<n:
    print(a )
    a,b = b,a+b
print("\nFibo(10): ", a)
