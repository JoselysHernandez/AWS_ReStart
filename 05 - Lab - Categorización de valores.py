# Crear una lista de varios tipos
MixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in MixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))