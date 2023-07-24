n=int(input("donner un nombre positif: "))
while n<=0:
	n=int(input("donner un nombre positif: "))
s=0
for i in range(1,n+1):
	for j in range(1,i+1):
		if i%j==0:
			s=s+1
	if s==2:
		print("le nombre",i,"est premier")	