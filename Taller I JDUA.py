print('Bienvenido a la calculadora de conjuntos')
A=[]
A=set()
limA=int(input('Escriba cuantos elementos tendrá el conjunto A: '))
for i in range(0,limA):
    elemento=float(input('Elemento de A: '))
    A.add(elemento)
print(A)
B=[]
B=set()
limB=int(input('Escriba cuantos elementos tendrá el conjunto B: '))
for j in range(0,limB):
    elementosb=float(input('Elemento de B: '))
    B.add(elementosb)
print(B)
op=1
while op==1:
    operacion=int(input('Seleccione:\n 1. Unión de Conjuntos\n 2. Intersección de Conjuntos\n 3. Diferencia de Conjuntos\n 4. Diferencia Simétrica\n 5. Salir\n'))
    if operacion==1:
        C=[]
        C=set()
        C=A|B
        print(C)
        op=1
    elif operacion==2:
        D=[]
        D=set()
        D=A&B
        print(D)
        op=1
    elif operacion==3:
        diferencia=int(input('Digite 1 si desea restar A-B, o 2 si desea B-A: '))
        if diferencia==1:
             E=[]
             E=set()
             E=A-B
             print(E)
        elif diferencia==2:
             E=[]
             E=set()
             E=B-A
             print(E)
        else:
            print('Error')
        op=1
    elif operacion==4:
        F=[]   
        F=set()
        F=A^B
        print(F)
        op=1
    elif operacion==5:
        break
    else:
        print('Error')
        op=1