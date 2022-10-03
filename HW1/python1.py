import matplotlib.pyplot as plt
import numpy as np

x=lambda n: 0 if n<-3 else [2,0,-1,6,-3,2,0][n+3] 
y=lambda n: 0 if n<-5 else [8,2,-7,-3,0,1,1][n+5]
w=lambda n: 0 if n<-2 else [3,6,-1,2,6,6,1][n+2]

def plot(func, range, title,save_name=""):
    y=[]
    x=[]
    xdot=[]
    ydot=[]
    for n in range:
        y.append(0)
        try:
            y.append(func(n))
            ydot.append(func(n))
        except:
            y.append(0)
            ydot.append(0)
        y.append(0)

        x+=[n,n,n]
        xdot.append(n)

    fig=plt.figure()
    plt.plot(x,y)
    plt.plot(xdot,ydot,"o")
    plt.title(title)
    plt.xlabel("n")
    plt.ylabel(f"{title[0]}[n]")
    plt.savefig(save_name)

c=lambda n: x(n+3)
plot(c,range(-10,5),"c[n]=x[n+3]","c.png")

d=lambda n: y(n-2)
plot(d,range(-10,5),"d[n]=y[n-2]","d.png")

e=lambda n: x(-n)
plot(e,range(-10,5),"e[n]=x[-n]","e.png")

u=lambda u: y(n+3)+x(n-3)
plot(u,range(-10,5),"u[n]=x[n-3]+y[n+3]","u.png")

v=lambda n: y(n-3)*w(n+2)
plot(v,range(-10,5),"v[n]=y[n-3]*w[n+2]","v.png")

s=lambda n: y(n+4)-w(n-3)
plot(s,range(-10,5),"s[n]=y[n+4]-w[n-3]","s.png")

r=lambda n: 3.9*w(n)
plot(r,range(-10,5),"r[n]=3.9w[n]","r.png")
