
def union(x,y):
    return x|y
def inter(x,y):
    return x&y
def difer(x,y):
    return x-y
def difersim(x,y):
    return x^y

A={6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
print('A: ',A)
B={2,4,6,8,10,12,14,16,18,20,22,24}
print('B: ',B)
C={1,4,8,10,12,15,18,20}
print('C: ',C)
D={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43}
print('D: ',D)

menu=1
while menu==1:
    opciones=int(input('Seleccione su opción:\n 1. Para realizar B∩(CΔD)\n 2. Para realizar (A∩C)UB\n 3. Para realizar (BUD)-C\n 4.(A-B)Δ(A∩D)\n 5. Para salir\n'))
    if opciones==1:
        r=inter(B,difersim(C,D))
        print(r)
        menu=1
    elif opciones==2:
        r=union(inter(A,C),B)
        print(r)
        menu=1
    elif opciones==3:
        r=difer(union(B,D),C)
        print(r)
        menu=1
    elif opciones==4:
        r=difersim(difer(A,B),inter(A,D))
        print(r)
        menu=1
    elif opciones==5:
        break
    else:
        print('Error')
        menu=1