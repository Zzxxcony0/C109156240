
a = int(input("組數為: "))
for i in range(a):
    gr0,gr1=map(int,input("第"+str(i+1)+"組: ").split()) 
    s = gr0*250 + gr1*175
    print("第"+str(i+1)+"組應收費用:"+ str(s))
     

   

