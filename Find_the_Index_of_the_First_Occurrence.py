haystack = "sadbutsad"
needle = "sad"

def foo(haystack,needle):
    start = False
    p = -1
    if needle in haystack:
        for pos,i in enumerate(haystack):
            if i == needle[0]:
                start = True

            if start:
                for pos2,j in enumerate(needle):
                    if j != haystack[pos+pos2]:
                        break
                    if pos2 == len(needle)-1:
                        return pos
    
    return p
            
if __name__ == "__main__":
    print(foo(haystack,needle))
