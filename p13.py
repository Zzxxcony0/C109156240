n = input("輸入一字元為:")
n0 = str(n)
n1 = n0[:]
n2 = n0[::-1]
if(n1 == n2):
    print("Yes")
else:
    print("No")
    