almacenes={"Alamcen1":{"manzanas":30,"bananas":40,"naranjas":30},
            "Alamcen2":{"manzanas":20,"bananas":10,"naranjas":10},
            "Alamcen3":{"manzanas":40,"bananas":30,"naranjas":50}}
totales={}
for almacen, productos in almacenes.items():
    for producto, cantidad in productos.items():
        if producto in totales:
            totales[producto]+=cantidad
        else:
            totales[producto]=cantidad
    print("la suma total es : ", totales)