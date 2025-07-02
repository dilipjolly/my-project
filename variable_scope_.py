from builtins import function

Buit in function

demo_tuple = (9,123,40,8,7,6,5,4,3,2)
x = max(demo_tuple)
print(x)
i = iter(demo_tuple)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

demo_tuple = (9,123,40,8,7,6,5,4,3,2,40,8,7,6,5,4,3,2,1)
p = min(demo_tuple)
i = iter(demo_tuple)
j = reversed(demo_tuple)
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(p)

demo_tuple = (9, 123, 40, 8, 7, 6, 5, 4, 3, 2, 40, 8, 7, 6, 5, 4, 3, 2, 1)
x = slice(2, 18, 2)
print(demo_tuple[x])
x = sorted(demo_tuple)
print(x)
y = sum(demo_tuple)
print(y)

x = input("Enter Your Name- ")
y = x.upper()
print("Welcome to the Dashboard " +y )

