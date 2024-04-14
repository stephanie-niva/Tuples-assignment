tuples =(1,2,3,4,5,6)

print(tuples)

print(tuples[2])

print(tuples[1:])
print(tuples[-3:-1])

x = list(tuples)
x[1] = 7
y = x + [30,40]
y.extend([50,80,25])
print(y)
y.pop()
print(y)
y.reverse()
print(y)
for a in y :print(a)
tuples = tuple(y)
print(tuples)



