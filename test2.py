'''
#2.1
one=input('Input First Number\n')
two=input('Input Second Number\n')
print('%s ='%one,'%s'%two,':',one==two)
print('%s >'%one,'%s'%two,':',one>two)
print('%s <'%one,'%s'%two,':',one<two)
'''
'''
print(bool("Hello"))
print(bool(""))

print(bool(15))
print(bool(0))
'''
'''
a = 60
b = 13
c = 0

c = a & b
print(c)

c = a | b
print(c)

c = a ^ b 
print(c)

c = ~a 
print(c)

c = a << 2
print(c)

c = a >> 2
print(c)
'''
'''
#2.2
print('Day Converter Program')
day=input('Input number of Days : ')
print('%s'%day,'Days --> Hour',int(day)*24,'Hours')
print('%s'%day,'Days --> Minute',int(day)*24*60,'Minutes')
print('%s'%day,'Days --> Second',int(day)*24*60*60,'Seconds')
'''
'''
friend=["Jan","Cream","Phu","Bam","Aom","P","Bas","Kong","Da","James"]
friend.append("Dome")
friend.append("Poondang")
friend.insert(1,"Csa")
friend.insert(8,"Ped")
friend.remove("Aom")
friend.pop(3)
del friend[7]
friend.clear()
del friend
print(friend)
'''
'''
animal={"cat","dog","rat","pig","ant"}
animal.add("monkey")
animal.update(["python","capibara","spider","penguin","crocodile"])
print(animal)
'''
'''
#2.3
print('โปรแกรมหยิบสินค้าใส่ตะกร้า')
buy=[]
buy1=input('หยิบสินค้าชิ้นที่ 1 : ')
buy.append(buy1)
buy2=input('หยิบสินค้าชิ้นที่ 2 : ')
buy.append(buy2)
buy3=input('หยิบสินค้าชิ้นที่ 3 : ')
buy.append(buy3)
buy4=input('หยิบสินค้าชิ้นที่ 4 : ')
buy.append(buy4)
buy5=input('หยิบสินค้าชิ้นที่ 5 : ')
buy.append(buy5)
print('สินค้าที่หยิบใส่ตะกร้ามีดังนี้')
print('1. ',buy[0])
print('2. ',buy[1])
print('3. ',buy[2])
print('4. ',buy[3])
print('5. ',buy[4])
'''
'''
#2.4
print('โปรแกรมคำนวนค่าผ่านทางมอเตอร์เวย์\n')
print('รถยนต์ 4 ล้อ       กด 1\nรถยนต์ 6 ล้อ       กด 2\nรถยนต์มากกว่า 6 ล้อ กด 3\n\n')
car1=["ลาดกระบัง-->บางบ่อ = 25 บาท","ลาดกระบัง-->บางประกง = 30 บาท","ลาดกระบัง-->พนัสนิคม = 45 บาท","ลาดกระบัง-->บ้านบึง = 55 บาท","ลาดกระบัง-->บางพระ = 60 บาท"]
car2=["ลาดกระบัง-->บางบ่อ = 45 บาท","ลาดกระบัง-->บางประกง = 45 บาท","ลาดกระบัง-->พนัสนิคม = 75 บาท","ลาดกระบัง-->บ้านบึง = 90 บาท","ลาดกระบัง-->บางพระ = 100 บาท"]
car3=["ลาดกระบัง-->บางบ่อ = 60 บาท","ลาดกระบัง-->บางประกง = 70 บาท","ลาดกระบัง-->พนัสนิคม = 110 บาท","ลาดกระบัง-->บ้านบึง = 130 บาท","ลาดกระบัง-->บางพระ = 140 บาท"]
number=int(input('\tเลือกประเภทยานพาหนะ : '))
if number==1:
    print('\tค่าบริการรถยนต์ 4 ล้อ')
    for x in car1:
        print('\n',x)
elif number==2:
    print('\tค่าบริการรถยนต์ 6 ล้อ')
    for x in car2:
        print('\n',x)
elif number==3:
    print('\tค่าบริการรถยนต์มากกว่า 6 ล้อ')
    for x in car3:
        print('\n',x)
'''