
from socket import socket
import os
inventory={
    'Laptop':   (10,45000),
    'Mouse':    (85,350),
    'Keyboard': (40,750),
    'Monitor':  (6,12000)
}

total =0
for item,value in inventory.items():
    print(f"Items: {item}, Quantity: {value[0]}, Price: {value[1]}")
    a = value[0]*value[1]
    total +=a
    print("Stock Value: ",a,"\n")
  
a=input("Enter a name")
if a in inventory.keys():
    print("exist")
    price=input("enter a price")
    p=inventory[a][0]
    print(p)
    invent=(p,price)
    inventory[a]=invent
    print(inventory)

for i in inventory.items():
    a=i[1][0]
    print(a)
    if a<8:
        print("critical Stock")
    elif 8<a<12:
        print("low stock")
    elif 21<a<50:
        print("Adequate stock")
    elif a>50:
        print("High stock")

with open("inventory.txt","w") as f:
    for item, value in inventory.items():
        f.write(f"Items: {item}, Quantity: {value[0]}, Price: {value[1]},total :{total}\n")
