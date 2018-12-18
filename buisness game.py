print("this is a buisness game\n")
money = 10000
import random
print("you have",money,) 
store = input("you have 3 options, you can buy a big store for $5000\n a medeum store for $3000 or a small store for $1500 choose 1,2, or 3\n")
store1 = 5000
store2 = 3000
store3 = 1500
if store == "1":
    print("you have succesfully bought the biggest store for $5000\n")
    money = money - store1
    print ("you now have$",money,)
    chance = random.randint(1,20)
    if chance == 1:
        print("it seems that there is some work to do on the pluming and the electrical\n")
        money = money - 1500
        print ("you now have$",money,)
        
if store == "2":
    print("you have succesfully bought the regular store for $3000")
    money = money - store2
    print ("you now have$",money,)
    chance = random.randint(1,10)
    if chance == 1:
        print("it seems that there is some work to do on the pluming and the electrical\n")
        money = money - 1000
        print ("you now have$",money,)


if store == "3":
    print("you have succesfully bought the smallest store for $1500\n")
    money = money - store3
    print ("you now have$",money,)
    chance = random.randint(1,5)
    if chance == 1:
        print("it seems that there is some work to do on the pluming and the electrical\n")
        money = money - 700
        print ("you now have$",money,)
sign = input("would you like to buy a big sign for $1000, a meduem sign for $500 or a small sign for $100(please enter 1,2 or 3\n")
sign1 = 1000
sign2 = 500
sign3 = 100
if sign == "1":
    print ("you have bought the biggest sign, it better attrace some coustmars")
    money = money - sign1
    sign = sign1

if sign == "2":
    print ("you have bought the meduem sign, its the same size as everyone elses\n")
    money = money - sign2
    sign = sign2

if sign == "3":
    print ("you have bought the smallest sign, i can barely see it!\n")
    money = money - sign3
    sign = sign3
print ("you now have$",money,)
cameras = 2000
safe = input("yould you like to buy a secrety system? it will cost $2000\n")
if safe == "yes":
    print ("ok we have bought the secrety system\n")
    money = money - cameras
else:
    print("no need we are safe\n")

print ("you now have$",money,)


#im so freaking bored ahhhhhaufgialqkrfip;fgipqwafrvipaqdebveoqr

print("now for the good stuff")



if sign == sign3:
    coustmers = random.randint(15,30)
    print(coustmers," coustmers came today")
    print("you earned",coustmers * 15)
    money = money + coustmers * 15
    print ("you now have$",money,)
    steal = random.randint(1,2)
    if steal == 1:
        print("but one person stole 2000")
        money = money - 2000
    else:
        print("no one stole today")

if sign == sign2:
    coustmers = random.randint(30,50)
    print(coustmers," coustmers came today")
    print("you earned",coustmers * 15)
    money = money + coustmers * 15
    print ("you now have$",money,)
    steal = random.randint(1,2)
    if steal == 1:
        print("but one person stole 3000")
        money = money - 3000
    else:
        print("no one stole today")
if sign == sign1:
    coustmers = random.randint(50,100)
    print(coustmers," coustmers came today")
    print("you earned",coustmers * 15)
    money = money + coustmers * 15
    print ("you now have$",money,)
    steal = random.randint(1,2)
    if steal == 1:
        print("but one person stole 5000")
        money = money - 5000
    else:
        print("no one stole today")

print("at the end of day one you have",money,)

while True:
    continue

while money >= "0":
    print("YOU WENT BANKRUPT!!!")
    break

















 
