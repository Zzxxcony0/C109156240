money = int(input(""))
hun = money // 100
fifty = (money - 100*hun) // 50
ten = (money - 100*hun - 50*fifty) // 10
five = (money - 100*hun - 50*fifty - 10*ten) // 5
one = (money - 100*hun - 50*fifty - 10*ten - five*5) // 1
print(hun + fifty + ten + five + one)