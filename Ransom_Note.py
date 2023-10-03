def foo(ransomNote,magazine):
    if ransomNote == "":
        return False
    for pos,i in enumerate(ransomNote):
        if i not in magazine:
            return False
        if i in magazine:  
            index = magazine.find(i)
            magazine = magazine[:index] + magazine[index+1:]
            ransomNote = ransomNote[:pos] + ransomNote[pos+1:]
        
    return True


r = "aa"
m = "abaac"

print(foo(r,m))







