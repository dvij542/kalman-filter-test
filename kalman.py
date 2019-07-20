import matplotlib.pyplot as plt
import numpy as np

file1 = open("kalmann.txt","r")
lines = file1.readlines()
state1 = lines[0].split(",")
state = [float(state1[0]),float(state1[1])]
words = [i.split(",") for i in lines[1:]]
x = [[float(i[0]),0] for i in words]
y = [[float(i[1]),0] for i in words]
v = [float(i[2]) for i in words]
w = [float(i[3]) for i in words] 
file1.close()
t=1
e = [1.0,1.0]
maxdvx = 0
maxdvy = 0
errorx = 0
errory = 0
for i in range(359):
	state = [state[0] + v[i]*t,state[1] + w[i] * t]
	if i>1 :
		maxdvx = max(maxdvx,abs(v[i]-v[i-1]))
		maxdvy = max(maxdvy,abs(w[i]-w[i-1]))
	if i>2 :
		errorx = ((2*v[i-1]-v[i-2]-v[i])/maxdvx)**4
		errory = ((2*w[i-1]-w[i-2]-w[i])/maxdvy)**4 
	e = [e[0]+errorx ,e[1]+errory]
	kalmangain = [e[0]/(e[0] + 2.0),e[1]/(e[1] + 2.0)]
	print(kalmangain)
	e = [e[0] * (1.0-kalmangain[0]),e[1]*(1.0 - kalmangain[1])]
	[x[i][1],y[i][1]] = [state[0] + kalmangain[0] * (x[i][0]-state[0]),state[1] + kalmangain[1] * (y[i][0]-state[1])]
	state = [x[i][1],y[i][1]] 

#state = numpy[]
print("Final position : " , x[-1][1] , " , " , y[-1][1])
print("Initial position : " ,float(state1[0]) , " , " , float(state1[1]))
color = ("red", "green")
plt.scatter(x, y, alpha=0.8, marker = '.',c=color, edgecolors='none', s=30)
plt.show()