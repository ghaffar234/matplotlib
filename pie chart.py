import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[2,2,3,4]
c=["g","r","y","b"]
plt.pie(y, labels=x, colors=c, autopct='%1.1f%%')
#plt.bar(x,y,color=c)
plt.show()