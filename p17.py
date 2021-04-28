a=[]
for i in range(5):
  b=input("請輸入五筆資料: ")
  if b=='A':
    b=14
  if b=='J':
    b=11
  if b=='Q':
    b=12
  if b=='K':
    b=13
  a.append(int(b))  
print(sum(a))                