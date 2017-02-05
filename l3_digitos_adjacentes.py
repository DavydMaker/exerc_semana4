n = input('Digite um número inteiro: ')
i = 1
r = False
while i < len(n):
	if n[i] == n[i-1]:
		r = True
		break
	i+=1
if r == True:
	print('sim')
else:
	print('não')