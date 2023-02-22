#Aproximaciones JDUA
import math
erroresperado=(0.5*(10**-8))*100
print('El error esperado es de: ',erroresperado)
deg=float(input('Ángulo en Grados: '))
rad=deg*math.pi/180
erroraprox=100
coseno=1
print('El coseno es igual a 1')
i=2
k=1
while erroraprox>=erroresperado:
        valor_ant=coseno
        if k%2!=0:
         coseno=coseno-(((rad)**i)/(math.factorial(i)))
         erroraprox=math.fabs(((coseno-valor_ant)/valor_ant)*100)
         
        else:
         coseno=coseno+(((rad)**i)/(math.factorial(i)))
         erroraprox=math.fabs(((coseno-valor_ant)/valor_ant)*100)
           
        print ('El coseno es igual a: ',coseno)
        print('El error aproximado es: ',erroraprox,'%') 
        i=i+2 
        k=k+1
