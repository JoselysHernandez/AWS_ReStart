#import re

#with open("preproinsulin-seq.txt", "r") as file:
#    sequence = file.read()
 
#sequence = re.sub(r"ORIGIN|//|\d+|\s+", "", sequence)
 
#with open("preproinsulin-seq.txt", "w") as file:
#    file.write(sequence)

with open("preproinsulin-seq.txt", "r") as file:
    sequence = file.read()

lsinsulin = sequence[:24]
binsulin = sequence[24:54]
cinsulin = sequence[54:89]
ainsulin = sequence[89:110]

with open("lsinsulin-seq-clean.txt", "w") as file:
    file.write(lsinsulin)
with open("binsulin-seq-clean.txt", "w") as file:
    file.write(binsulin)
with open("cinsulin-seq-clean.txt", "w") as file:
    file.write(cinsulin)
with open("ainsulin-seq-clean.txt", "w") as file:
    file.write(ainsulin)


print(len(lsinsulin))
print(len(binsulin))
print(len(cinsulin))
print(len(ainsulin))