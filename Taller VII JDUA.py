#Aproximaciones JDUA Euler
import math

erroresperado=(0.5*(10**-8))*100
print('El error esperado es de: ',erroresperado)
x=0.85
erroraprox=100
print('---------Aquí empieza el primer método-----------')
euler=1
print('Euler es igual a 1')
i=1
k=1
while erroraprox>=erroresperado:
        valor_ant=euler
        if k%2!=0:
         euler=euler-(((x)**i)/(math.factorial(i)))
         erroraprox=math.fabs(((euler-valor_ant)/valor_ant)*100)
         
        else:
         euler=euler+(((x)**i)/(math.factorial(i)))
         erroraprox=math.fabs(((euler-valor_ant)/valor_ant)*100)
           
        print ('Euler es igual a: ',euler)
        print('El error aproximado es: ',erroraprox,'%') 
        
        i=i+1
        k=k+1
        
print('Se realizaron ',k,' iteraciones')
print('----------Aquí empieza el segundo método----------')
euler=1
print('Euler es igual a 1')
i=1
k=1
erroraprox=100
suma=1
while erroraprox>=erroresperado:
    valor_ant=euler
    suma_ant=suma
    suma=suma_ant+((x)**i)/(math.factorial(i))
    euler=1/(suma)
    erroraprox=math.fabs(((euler-valor_ant)/valor_ant)*100)
    print ('Euler es igual a: ',euler)
    print('El error aproximado es: ',erroraprox,'%') 
    i=i+1
    k=k+1
print('Se realizaron ',k,' iteraciones')