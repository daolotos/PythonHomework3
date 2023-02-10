
n = int(input("N = "))
a = []
for i in range(n):
    a.append(int(input(f"A[{i}] = ")))
x = int(input("X = "))

count = 0
for y in a:
    if y == x:
        count += 1

print(f"X appears in A = {count}")
