a = int(input(""))
if(a<=120):
    print("Summer months:" + str(a*2.10))
    print("Non-Summer months:" + str(a*2.10))
elif(a>=121 and a<=330):
    print("Summer months:" + str(252+(a-120)*3.02))
    print("Non-Summer months:" + str(252+(a-120)*2.68))
elif (a>=331 and a<=500):
    print("Summer months:" + str(886.2+(a-330)*4.39))
    print("Non-Summer months:" + str(814.8+(a-330)*3.61))     
elif (a>=501 and a<=700):
    print("Summer months:" + str(1632.5+(a-500)*4.97))
    print("Non-Summer months:" + str(1428.5+(a-500)*4.01))  
elif (a>=701):
    print("Summer months:" + str(2626.5+(a-700)*5.63))
    print("Non-Summer months:" + str(2230.5+(a-700)*4.50))