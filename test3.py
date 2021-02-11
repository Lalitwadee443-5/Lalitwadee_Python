'''
#3.1
print('เลือกเมนูเพื่อทำรายการ\n\nกด 1 เลือกจ่ายเพิ่ม\nกด 2 เลือกเหมาจ่าย\n')
num=input('')
print('กรุณากรอกระยะทาง')
km=input('')
if int(num)==1:
    if int(km)<=25:
        print('ค่าใช้จ่ายรวมทั้งหมด 25 บาท')
    else:
        print('ค่าใช้จ่ายรวมทั้งหมด 80 บาท')
elif int(num)==2:
    if int(km)<=25:
        print('ค่าใช้จ่ายรวมทั้งหมด 25 บาท')
    else:
        print('ค่าใช้จ่ายรวมทั้งหมด 55 บาท')
'''
'''
#3.2
print('กรุณากรอกจำนวนครั้งการรับค่า')
n=int(input(''))
z=0
i=1
while(i<=n):
    num=int(input('กรอกตัวเลข   '))
    z+=num
    i+=1
print('ผลรวมค่าที่รับมาทั้งหมด = %d'%z)
'''
'''
#3.3
foodlist=[]
i=0
print('ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม')
while(True):
    i+=1
    food=input('อาหารโปรดลำดับที่ {} คือ    '.format(i))
    foodlist.append(food)
    if food=='exit':
        break
print('อาหารโปรดของคุณมีดังนี้  ',end='')
for x in range (1,i):
    print(x,'.',foodlist[x-1],end=' ')
'''
'''
#3.4
a=[]
while True:
    b=input('----ร้านคุณหลินบิวตี้----\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n')
    b=b.lower()
    if b=='a':
        c=input('ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด) ')
        a.append(c)
        print('\n*******ข้อมูลได้เข้าสู่ระบบแล้ว*******\n')
    elif b=='s':
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a:
            e=d.split(":")
            print('{0[0]:<6} {0[1]:<10}({0[2]:<10})'.format(e))
            continue
    elif b=='x':
        break
print('ทำคำสั่งถัดไป')
'''
'''
#3.5
st=int(input('Please enter student: '))
n=[0,0,0,0,0,0]
sc=['90-100','80-89','70-79','60-69','50-59','0-49']
for a in range(0,st):
    s=int(input('Please enter student score: '))
    if s<=100 and s>=90:
        n[0]+=1
    elif s<=89 and s>=80:
        n[1]+=1
    elif s<=79 and s>=70:
        n[2]+=1
    elif s<=69 and s>=60:
        n[3]+=1
    elif s<=59 and s>=50:
        n[4]+=1
    else :
        n[5]+=1
for a in range(0,6):
    print(sc[a]+':'+n[a]*'*')
'''