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
form=list(s)
print(form)
stack=[]
skobki=input()
index=[]
close_index=[]
close_stack=[]
a=0
c=0
b=len(form)
d=len(form)

if skobki in '([{<':
    status=True
    for i in s:
        if i in '([{<':
            stack.append(i)
            index.append(form.index(i,a,b))
            a=form.index(i,a,b)+1
            print(index)
            print(stack)
        elif i in ')]}>':
            close_stack.append(i)
            close_index.append(form.index(i, c, d))
            c = form.index(i, c, d) + 1
            print(close_index)
            print(close_stack)
            if not stack:
                status=False
                break
            open_bracket=stack.pop()
            open_index = index.pop()
            print(open_bracket)
            print(open_index)
            if open_bracket in skobki and open_bracket=='(' and i==')':
                continue
            if open_bracket in skobki and open_bracket=='[' and i==']':
                continue
            if open_bracket in skobki and open_bracket=='{' and i=='}':
                continue
            if open_bracket in skobki and open_bracket=='<' and i=='>':
                continue
            status=False
            break
    if status and len(stack)==0:
        print(status)
    else:
        print(status, open_bracket, open_index)
else:
    print('XER')