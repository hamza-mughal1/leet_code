import time
def foo(numbers, target):
    R = 0
    L = len(numbers)-1
    while True:
        condition = numbers[R] + numbers[L]
        if (condition) == target:
            return [R+1,L+1]
        if R == L:
            return None
        if (condition) > target:
            L -= 1
        if (condition) < target:
            R += 1


start = time.time()
result = foo([2,7,11,15],9)
print("time took : ",time.time()-start)
print(result)