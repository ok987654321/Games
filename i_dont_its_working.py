from collections import defaultdict
color_code = {'C':"\U0001f7e9",'N':"\u2B1B",'W':"\U0001f7e8"}

with open('Coding/nerdle/equation.txt')as my_file:
    equation = my_file.readlines()

for i in range(17723):
    equation[i] = str(equation[i][:8])

with open('Coding/nerdle/input.txt') as we_need_it:
    t = we_need_it.readline()                           # t -> target
t = t[:8]

def compare(s,t):

    k = ['N','N','N','N','N','N','N','N']
    d = defaultdict(int)
    for i in range(8):
        d[t[i]] += 1

    for i in range(8):
        if t[i] == s[i]:
            k[i] = 'C'
            d[s[i]] -= 1
    for i in range(8):
        if k[i]!='C' and d[s[i]]>0:
            d[s[i]] -= 1
            k[i]='W'

    return "".join(k)

def filter(hehe , result, k):

    for i in range(8):
        if (result[i]=='C' and hehe[i]!=k[i]) or (result[i]!='C' and hehe[i]==k[i]):
            return False
    newk , newhehe = [],[]
    for i in range(8):
        if result[i]!="C":
            newk.append(k[i])
            newhehe.append(hehe[i])
        else:
            newk.append('_')
            newhehe.append('_')
    k , hehe = newk, newhehe

    for i in range(8):
        if result[i] == 'W':
            if hehe[i] in k:
                k[k.index(hehe[i])] = '_'
            else:
                return False
    for i in range(8):
        if result[i] == 'N' and hehe[i] in k:
            return False

    return True

def color(k):
    res=""
    for i in k:
        res+=color_code[i]
    return res

hehe , res , answer = "12+35=47" , compare("12+35=47",t) , [True]*17723

while res != "CCCCCCCC":
    print(hehe, *color(res))
    for i in range(17723):
        answer[i] = answer[i] and filter(hehe, res, equation[i])
    
    for i in range(17723):
        if answer[i]:
            hehe = equation[i]
            break
    res = compare(hehe,t)

print(hehe, *color(res))
