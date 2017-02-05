n = int(input('Digite um número inteiro: '))
i,cont = 1,0
while i <= n:
	if(n % i == 0):
		cont += 1
	i += 1
if cont == 2:
	print('primo')
else:
	print('não primo')