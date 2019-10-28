e = int(input("masukan bilangan pertama : "))
f = int(input("masukan bilangan kedua : "))
g = int(input("masukan bilangan ketiga : "))

if e > f and e > g:
    print("maks = ", e)
elif f > e and f > g:
    print("maks = ", f)
     
else: 
    print("maks = ", g)

