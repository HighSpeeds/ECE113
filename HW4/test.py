x=lambda n: [1,1,1,1,0][n%5]

def circular_convolution(x, h,N):
    # Your code here
    y=[]
    for n in range(N):
        y.append(0)
        for k in range(N):
            y[n] += x(k) * h(n-k)
    return y

print(circular_convolution(x,x,5))

x=lambda n:[1, -1, 1, -1, 1, -1][n%6]
y=lambda n:[1, 1, -1, -1, 1, 1][n%6]

print(circular_convolution(x,y,6))