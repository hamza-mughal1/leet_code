s = "   fly me   to   the moon  "

def foo(s):
    pre = s[0]
    word = ""
    start = False
    if s[0] != " ":
        word+=s[0]
    for i in s[1:]:
        if pre == " " and i != " ":
            start = True
            word = ""
        elif pre != " " and i == " ":
            start = False
        elif pre != " " and i != " ":
            start = True
        
        if start:
            word+=i
        
        pre = i

    if word == "":
        return 1
    return len(word)





print(foo(s))

