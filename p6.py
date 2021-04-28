num = input("輸入值為: ")
list1 = num.split(",")
for i in range(len(list1)):
    list1[i] = int(list1[i])
list1.sort()
Max = ""
Min = ""
for i in list1:
    Min += str(i)

Max = Min[::-1]

ans = int(Max) - int(Min)
print("最大值數列與最小值數列差值為 : " + str(ans))

