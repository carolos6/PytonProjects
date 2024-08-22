notas={"Alex":12, "John Doe": 14, "John":15, "JohnMaria":16,}
mejor_estudiantes=max(notas, key=notas.get) #SE AGARRA LA MAYOR NOTA DEL DICCIONARIO
print("La nota mayor fue: ", mejor_estudiantes)