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
close_skobki=[]
index=[]
close_index=[]
close_stack=[]
a=0
c=0
b=len(form)
d=len(form)
oshibka_open=None
oshibka_close=None
if '(' in skobki:
    close_skobki.append(')')
if '[' in skobki:
    close_skobki.append(']')
if '{' in skobki:
    close_skobki.append('}')
if '<' in skobki:
    close_skobki.append('>')
#Проверка на то, что введенные скобки это скобки
print(skobki)
print(list(skobki))
status=True
for x in skobki:
    if '(' in x or '[' in x or '{' in x or '<' in x:
        break
    else:
        quit()

print('XYU')
print(skobki)

#Проверка на наличие скобок в тексте
for i in s:
    #Если открывающаяся скобка в тексте
    if i in list(skobki):
        stack.append(i) #Добавление открывающейся скобки в stack
        index.append(form.index(i,a,b)) #Добавление скобки в index
        a=form.index(i,a,b)+1 #Добавление индекса скобки в a
        print(index)
        print(stack)
    elif i in close_skobki: #Если закрывающаяся скобка в тексте
        close_stack.append(i) #Добавление закрывающейся скобки в close_stack
        close_index.append(form.index(i, c, d)) #Добавление закрывающейся скобки в close_stack
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
if status and len(stack)==0 or status and skobki not in open_bracket:
    print(status, oshibka_open, oshibka_close)
else:
    oshibka_open=(open_bracket, open_index)
    oshibka_close=(close_index[0], close_stack[0])
    print(status, oshibka_open, oshibka_close)