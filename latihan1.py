import random
n = int(input("masukan nilai n :  "))
for b in range(n) :
    b += 1
    a = random.uniform(0.0,0.5)
    print('data ke : ',b,' => ',a )
print("end")