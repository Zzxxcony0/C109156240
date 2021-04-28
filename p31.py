a = int(input("國文:"))
b = int(input("英文:"))
c = int(input("微積分:"))
d = int(input("體育:"))
e = int(input("程式設計:"))

avg = (a+b+c+d+e) / 5
print("平均分數 : " + str(avg))
print("")

Max=max(a,b,c,d,e)
if (Max == a): 
    print("最高分科目 : 國文 " + str(a) + " 分")
elif (Max == b): 
    print("最高分科目 : 英文 " + str(b) + " 分")
elif (Max == c): 
    print("最高分科目 : 微積分 " + str(c) + " 分") 
elif (Max == d): 
    print("最高分科目 : 體育 " + str(d) + " 分") 
elif (Max == e): 
    print("最高分科目 : 程式設計 " + str(e) + " 分")     
print("")


Min=min(a,b,c,d,e)
if (Min == a): 
    print("最低分科目 : 國文 " + str(a) + " 分")
elif (Min == b): 
    print("最低分科目 : 英文 " + str(b) + " 分")
elif (Min == c): 
    print("最低分科目 : 微積分 " + str(c) + " 分") 
elif (Min == d): 
    print("最低分科目 : 體育 " + str(d) + " 分") 
elif (Min == e): 
    print("最低分科目 : 程式設計 " + str(e) + " 分") 


