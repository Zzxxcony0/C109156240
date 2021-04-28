a = list(input("輸入: "))
b = list(input("輸入: "))
c = len(a)
d = len(b)

a1 = 0
b1 = 0

for i in range(c):
    for j in range(d):
        if a[i] == b[j]:
            if i == j:
                a1 = a1 + 1
            else:
                b1 = b1 + 1

if a1 == 4 and b1 == 0:
    print(str(a1) + "A" + str(b1) + "B" + " 全對")
else:
    print(str(a1) + "A" + str(b1) + "B" + " 加油")