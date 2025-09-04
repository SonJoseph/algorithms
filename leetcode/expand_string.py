from typing import List

'''
[[a, b], [c, d], [e]]

s = [b, d]

O(number of options * max number within option)
'''
def createWord(i, options, word, res):
    if i >= len(options):
        res.append(''.join(word))
        return
    for opt in options[i]:
        word.append(opt)
        createWord(i+1, options, word, res)
        word.pop()


def expand(s: str) -> List[str]:
    res = []
    options = []

    i = 0
    while i < len(s):
        curr_option = []
        if s[i] == '{':
            i += 1
            while True:
                if s[i] == '}':
                    break
                if s[i] != ',':
                    curr_option.append(s[i])
                i += 1
        else:
            curr_option.append(s[i])
        options.append(sorted(curr_option))
        i+=1
    
    createWord(0, options, [], res)

    return res

    
                    


print(expand("{a,b}{c,d}e")) # ace bce ade bde. O(max # options * n)
             