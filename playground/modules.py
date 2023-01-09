"""
import fibolib

print(f"fibo(10) = {fibolib.fibo(10)}")
"""

"""
import fibolib as fib

print(f"fibo(10) = {fib.fibo(10)}")
"""

"""
from fibolib import fibo, fib

print(f"fibo(10) = {fibo(10)}")
print("\n First 10 fibo no:")
fib(10)
"""

"""
from fibolib import *

print(f"fibo(10) = {fibo(10)}")
print("\n First 10 fibo no:")
fib(10)
print(f"fib2 = {fib2(12)}")
"""

"""
import fibo

print(f"fibo(10) = {fibo.fibo(10)}")
"""

from tools import *

dif_1_3 = calculus.dif.dif(1, 3)
print(f"1 - 3 = {dif_1_3}")

dif_4_3 = calculus.dif.dif_and_print(4, 3)

sum_10 = calculus.sum.sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Sum(10) = {sum_10}")


from tools.printing.print import print_message

print_message("imported manually, whithout __all__")





