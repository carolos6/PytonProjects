numeros=[1,2,3,4,5,6,7,8]
resultado=[]
for i in numeros:
    if i%2==0:
        continue
    else:
        resultado.append(i*2)
print ("Lista rsultante: ", resultado)
        