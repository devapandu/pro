d=int(input())
p=[]
for i in range (0,d):
	p.append(input())
l=len(p[0])
e=""
for i in range (0,l):
	c=p[0][i]
	f=0
	for j in range (0,d):
		if(c!=p[j][i]):
			f=1
	if(f==0):
		e=e+c
	else:
		break
print(e)
