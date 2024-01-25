#  [1,2,3,4]
# 3:26
# 97%

# 4:10
# 83%


def foo(digits):
    s = str(digits)
    n = ""
    for i in s:
        if i.isnumeric():
            n += i

    n = int(n) + 1

    rdigits = []
    for i in str(n):
        rdigits.append(int(i))
    
    return rdigits


print(foo([1,2,3,9]))