def final(a,b):
    def bin_to_des(num):
        i = 1
        total = 0
        for bit in num[::-1]:
            total += int(bit)*i
            i *= 2

        return total
    
    def des_to_bin(num):
        re = ""
        while True:
            if num%2 == 0:
                re += "0"
            else:
                re += "1"
            num = num//2

            if num <= 0:
                break

        return re[::-1]

    return des_to_bin(bin_to_des(a)+bin_to_des(b))

# print(bin_to_des("1011"))
# print(des_to_bin(10))
# print(final("1010","1011"))