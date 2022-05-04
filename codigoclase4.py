import statistics
import numpy as np

lista = [[40, 80, 19], [6,7,8,9,10,11,17,13], [50,6350,6443]]

b = [max(p) for p in lista] 

print(b)

lista1 = [2,3,6,8,9,11,13,13,17,20,23,29,30,32,35,37,40]

def primo(x):
	
	for i in range(2,x):
		if x % i == 0:
			return False
            
	else:
            return True

primos = list(filter(primo,lista1))

print(primos)
