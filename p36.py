n1 = int(input("整數n:"))
n2 = str(n1)
n3 = int(1)
while(n1!=1):
    
    if(n1%2==1):
        n1 = n1*3+1
    
    else:
        n1 = n1/2
    n2 = n2+" "+str(int(n1))
    n3+=1
print("數列:",n2)

print("cycle length:",n3)
    
    



