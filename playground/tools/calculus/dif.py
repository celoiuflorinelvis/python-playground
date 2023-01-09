from ..printing import print

def dif(a, b):
    return a - b

def dif_and_print(a, b):
    _dif = a - b
    print.print_message("{} - {} = {}".format(a, b, _dif))
    return _dif
