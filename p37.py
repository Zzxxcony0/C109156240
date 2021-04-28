n1 =int(input(""))
n2={}

for i in range(0,n1):
    n3 = int(input())
    n2[i]=n3
    
    
for i in range (0,n1):
    if(int(n2[i])%9==0 or int(n2[i])%11==0):
        print()
        print("第",i+1,"個點",n2[i])