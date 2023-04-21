#Taller XIX JDUA
import math
x=[1,2,3,4,5,6,7]
y=[0.2,0.5,1.8,3.4,5.7,9,13.8]
print("-----MODELO LINEAL-----")
xy=[]
sumx=0
sumy=0
xsquare=[]
sumsquare=0
sumxy=0

for i in range(len(x)):
    xy.append(x[i]*y[i])

for k in range(len(x)):
    sumx=sumx+x[k]

for j in range(len(y)):
    sumy=sumy+y[j]

for h in range(len(x)):
    xsquare.append(x[h]*x[h])

for t in range(len(x)):
    sumsquare=sumsquare+xsquare[t]
    
for u in range(len(x)):
    sumxy=sumxy+xy[u]
    
promx=sumx/len(x)
promy=sumy/len(y)
a1=(((len(x)*sumxy)-(sumx*sumy))/((len(x)*sumsquare)-(sumx*sumx)))
ao=promy-(a1*promx)
#Errores
st=[]
sr=[]
sum=0
for el in range (len(y)):
    st.append((y[el]-promy)**2)
    sum=st[el]+sum
stsumatoria=sum
sy=math.sqrt((stsumatoria)/(len(y)-1))
sum2=0
for eo in range(len(x)):
    sr.append(((y[eo]-ao-a1*x[eo])**2))
    sum2=sr[eo]+sum2
srsumatoria=sum2
syx=math.sqrt(srsumatoria/(len(x)-2))

r=math.sqrt((stsumatoria-srsumatoria)/stsumatoria)*100

print("y= ",ao," + (",a1,"x)")
print("Sy: ",sy,"\nSy/x: ",syx,"\nr: ",r)
