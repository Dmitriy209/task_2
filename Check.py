import re
#Vseskobki=[]
#Formula=input('Введите формулу: ')
#Vseskobki=input('Введите скобки, которые хотите проверить: ')

#skobki=list(Vseskobki)
#print(skobki)
#skobkiinformula=re.search(r"[(){}[\]]+",Formula)
#print(skobkiinformula)

#s=Formula
#keep = {"(",")","[","]","{","}"}
#print("".join([ch for ch in s if ch in keep]))
#a="(){}[]<>"
#if Vseskobki in a and Vseskobki in Formula:

#else:
#    print('Таких скобок нет')

s=input()
stack=[]
skobki=input()
if skobki in '({[<':
    good=True
    for i in s:
        if i in '([{<':
            stack.append(i)
        elif i in ')]}>':
            if not stack:
                good=False
                break
            open_bracket=stack.pop()
            if open_bracket in skobki and open_bracket=='(' and i==')':
                continue
            if open_bracket in skobki and open_bracket=='[' and i==']':
                continue
            if open_bracket in skobki and open_bracket=='{' and i=='}':
                continue
            if open_bracket in skobki and open_bracket=='<' and i=='>':
                continue
            good=False
            break
    if good and len(stack)==0:
        print(good)
    else:
        print(good)
else:
    print('XER')