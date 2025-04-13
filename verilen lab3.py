n = int(input("Sətirlərin (n) sayını daxil et: "))
m = int(input("Sutunların (m) sayını daxil et: "))
X = []
print("Massivin elementlərini daxil et:")
for i in range(n):
    sətir = []
    for j in range(m):
        x = float(input(f"X[{i}][{j}] = "))
        sətir.append(x)
    X.append(sətir)

Y = []
for i in range(n):
    sətir = []
    for j in range(m):
        y = math.sin(X[i][j])
        sətir.append(y)
    Y.append(sətir)

print("\nY = sin(X) massivinin qiymətləri:")
for i in range(n):
    for j in range(m):
        print(f"Y[{i}][{j}] = {Y[i][j]:.4f}", end="  ")
    print()

