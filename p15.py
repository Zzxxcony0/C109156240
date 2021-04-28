a0 = list(input("輸入一組四位數字為 : "))
int0 = int(a0[0])
int1 = int(a0[1])
int2 = int(a0[2])
int3 = int(a0[3])

ans0 = (int0 + 7) % 10
ans1 = (int1 + 7) % 10
ans2 = (int2 + 7) % 10
ans3 = (int3 + 7) % 10

print (str(ans2) + str(ans3) + str(ans0) + str(ans1))



