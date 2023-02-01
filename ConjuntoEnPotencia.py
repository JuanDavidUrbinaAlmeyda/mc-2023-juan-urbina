def conjpotencia(conjunto):
    return conjpotencia_a([],sorted(conjunto))
def conjpotencia_a(current,datos):
    if datos:
        return conjpotencia_a(current,datos[1:])+conjpotencia_a(current+[datos[0]],datos[1:])
    return[current]

conjunto=[1,2,3,4]
res=conjpotencia(conjunto)
print(res)