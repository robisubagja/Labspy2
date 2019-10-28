a = int(input("masukan bilangan pertama : "))
b = int(input("masukan bilangan kedua : "))
c = int(input("masukan bilangan ketiga : "))

if a > b and a > c:
    print("maks = ", a)
elif b > a and b > c:
    print("maks = ", b)
     
else: 
    print("maks = ", c)

