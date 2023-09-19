s = "XXVII"

def foo(s):
    sym_val = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
    
    previous = None
    chng_val = {
        "I":False,
        "V":"I",
        "X":"I",
        "L":"X",
        "C":"X",
        "D":"C",
        "M":"C"
    }
    total = 0
    for i in s:
        if chng_val[i] == previous:
            num = sym_val[i]-(sym_val[previous])*2
            total = num+total
            previous = i
        else:
            num = sym_val[i]
            total = num+total
            previous = i

    return total

print(foo(s))