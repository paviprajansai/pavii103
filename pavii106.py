p1,p2=map(str,input().split())
c1=[]
d1=[]
for i in p1:
	c1.append(p1.count(i))
for j in p2:
	d1.append(p2.count(j))
for i in c1:
	if i in d1:
		flag=1
	
	else:
		flag=0
if flag==1:
	print("yes")
else:
	print("no")
  #i
