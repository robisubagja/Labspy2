a = int(input("masukan Bilangan pertama : "))
b = int(input("masukan bilangan kedua : "))
c = int(input("masukan bilangan ketiga : "))
d = int(input("masukan bilangan keempat : "))
e = int(input("masukan bialngan kelima : "))
if a > b and a > c and a > d and a > e:
    print("nilai terbesar adalah :",a)
elif b > a and b > c and b > d and b > e:
    print("nilai terbesar adalah :",b)
elif c > a and c > b and c > d and c > e:
    print("nilai terbesar adalah :",c)
elif d > a and d > b and d > c and d > e:
    print("nilai terbesar adalah :",d)
else:
    print("nilai terbesar adalah :",e)
