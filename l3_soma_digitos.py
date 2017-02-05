n = input('Digite um número inteiro: ')
i = 0
s = 0
while i < len(n):
	s = s + int(n[i])
	i+=1
print(s)