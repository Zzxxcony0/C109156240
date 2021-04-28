n = int(input("請輸入n : "))
k = int(input("請輸入k : "))
cal1 = n // k
cal2 = 0
if cal1 >= k:
    cal2 = cal1 // k
print(n + cal1 + cal2)  