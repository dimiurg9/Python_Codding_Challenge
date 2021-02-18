x = "abc"
y = "defij"
print("before swap: x = ", x, " y = ", y)

x = x + y
y = x[:len(x)-len(y)]
x = x[len(y):]

print("after swap: x = ", x, " y = ", y)

