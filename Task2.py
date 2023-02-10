
n = int(input("N = "))
a = []
for i in range(n):
    a.append(int(input(f"A[{i}] = ")))
x = int(input("X = "))

nearest = a[0]
for y in a:
    if abs(y - x) < abs(nearest - x):
        nearest = y

print(f"nearest to {x} in A = {nearest}")
