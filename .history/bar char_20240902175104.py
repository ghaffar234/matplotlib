#this code make for bar chart
import matplotlib.pyplot as plt
x=["pyhton","java","c++","C#"]
y=[20,80,30,40]
c=["g","r","y","b"]
plt.xlabel("Progaramming lanuage",fontsize=20)
plt.ylabel("NO.",fontsize=20,color="r")
plt.title("Programming lanuage overview",fontsize=20,color="b")
c=["r","m","y","b"]
plt.bar(x,y,width=0.1,color=c)
plt.show()