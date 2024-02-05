gas = [1,5,6,1,2]
cost = [3,6,4,1,1]

def foo(gas,cost):
    for pos,i in enumerate(gas):
        index = 1
        total_gas = i
        for _ in range(len(gas)):
            co = cost[(pos + index - 1)%len(gas)]
            if total_gas < co:
                break
            
            total_gas -= co
            total_gas += gas[(pos + index)%len(gas)]
            index += 1
        else:
            return pos
    else:
        return -1


print(foo(gas,cost))