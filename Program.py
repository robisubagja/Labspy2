
print("MENCARI NILAI TERTINGGI")
print("=======================")

e = int(input("masukan bilangan pertama : "))
f = int(input("masukan bilangan kedua   : "))
g = int(input("masukan bilangan ketiga  : "))


if e > f and e > g:
    print(e,"adalah tertinggi")
elif f > e and f > g:
    print(f,"adalah tertinggi")
     
else: 
    print(g,"adalah tertinggi")



