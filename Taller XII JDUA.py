import math
error=0
val_anterior=0
x=0.45
euler=(math.e)**(-x)
h=0.005
print('-----Iteración 0--------')
print('Euler es igual a: ',euler)
formula=(math.e**(-x))
val_anterior=euler
for i in range(1,16):
    if i%2==0:
        euler=val_anterior+ ((formula*(h**i))/math.factorial(i))
    else:
        euler=val_anterior+ (((formula*(h**i))/math.factorial(i))*-1)
    print('--------Iteración ',i,'--------')
    print('Euler es igual a: ',euler)
   
    error=math.fabs((euler-val_anterior)/val_anterior)*100
    print('El error es: ',error,' %')
    val_anterior=euler