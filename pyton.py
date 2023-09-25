n = int(input("Количество монет:"))
orel=0
resh=0

for i in range(n):
    x=int(input("Сторона монеты(1 или 0): "))
    if x ==1: 
      orel+=1
    else :
      resh +=1
if orel > resh :
   print(resh)
   
else :
    print (orel)

    
