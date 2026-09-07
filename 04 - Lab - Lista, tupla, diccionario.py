# Definición de una lista
FruitList = ["apple", "banana", "cherry"]
print(FruitList)
print(type(FruitList))

## Acceso a una lista por posición
print(FruitList[0])
print(FruitList[1])
print(FruitList[2])

## Modificación de los valores de una lista
FruitList[2] = "Orange"
print(FruitList)

# Definición de una tupla

MyFruitListTupla = ("apple", "banana", "pineapple")
print(MyFruitListTupla)
print(type(MyFruitListTupla))

## Acceso a una tupla por posición
print(MyFruitListTupla[0])
print(MyFruitListTupla[1])
print(MyFruitListTupla[2])

# Definición de un diccionario
MyFruitListTuplaDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}
print(MyFruitListTuplaDictionary)
print(type(MyFruitListTuplaDictionary))

# Acceso al diccionario por nombre
print(MyFruitListTuplaDictionary["Akua"])
print(MyFruitListTuplaDictionary["Saanvi"])
print(MyFruitListTuplaDictionary["Paulo"])