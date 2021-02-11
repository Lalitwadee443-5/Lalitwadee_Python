'''
import os
choice=0
filename=''

def menu():
    global choice
    print('Menu\n1.Open Write\n2.Open Notepad\n3.Exit')
    choice=input('Select Menu: ')

def opennotepad():
    filename='C:\\Windows\\notepad.exe'
    print('Memorandem writing %s'%filename)
    os.system(filename)

def openwrite():
    filename='C:\\Windows\\write.exe'
    print('Memorandem writing %s'%filename)
    os.system(filename)

while True:
    menu()
    if choice=='1':
        openwrite()
    elif choice=='2':
        opennotepad()
    else:
        break
'''
'''
#4.1
buy_list=[]
a=[0,0,0,0,0]
p=[15,10,20,30,25]

def one():
    print('\tรายการสินค้า\n1.ยาดม ราคา 15 บาท\n2.น้ำเปล่า ราคา 10 บาท\n3.มาม่า ราคา 20 บาท\n4.สบู่ ราคา 30 บาท\n5.แปรงสีฟัน ราคา 25 บาท')

def two():
    c=0
    while True:
        print('1.ยาดม\n2.น้ำเปล่า\n3.มาม่า\n4.สบู่\n5.แปรงสีฟัน\n6.ออกจากฟังก์ชัน')
        c=(input('เลือกหยิบสินค้าหมายเลข: '))
        try:
            if int(c)==1 or c=="1":
                buy_list.append("ยาดม")
            elif int(c)==2 or c=="2":
                buy_list.append("น้ำเปล่า")
            elif int(c)==3 or c=="3":
                buy_list.append("มาม่า")
            elif int(c)==4 or c=="4":
                buy_list.append("สบู่")
            elif int(c)==5 or c=="5":
                buy_list.append("แปรงสีฟัน")
            elif int(c)==6 or c=="6":
                break
            else:
                print('กรุณากรอกหมายเลขให้ถูกต้อง')
        except :
            print('กรุณากรอกหมายเลขให้ถูกต้อง')
            pass

def three():

    for i in buy_list:
        if i=="ยาดม":
            a[0]+=1
        elif i=="น้ำเปล่า":
            a[1]+=1
        elif i=="มาม่า":
            a[2]+=1
        elif i=="สบู่":
            a[3]+=1
        elif i=="แปรงสีฟัน":
            a[4]+=1
    att=a[0]+a[1]+a[2]+a[3]+a[4]
    ptt=a[0]*15+a[1]*10+a[2]*20+a[3]*30+a[4]*25
    print('')
    print('{0:_<10}{1}{0:_<10}'.format("",'สินค้าที่คุณได้หยิบไปมีดังนี้'))
    print('{0:.<6}{1}{0:.<6}{2}{0:.<6}{3}{0:.<7}'.format('','สินค้า','จำนวน','ราคา'))
    print('{0:_<38}'.format(""))
    if a[0]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','ยาดม',str(a[0]),str(a[0]*15)))
    if a[1]!=0:
        print('{0:.<4}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','น้ำเปล่า',str(a[1]),str(a[1]*10)))
    if a[2]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','มาม่า',str(a[2]),str(a[2]*20)))
    if a[3]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','สบู่',str(a[3]),str(a[3]*30)))
    if a[4]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','แปรงสีฟัน',str(a[4]),str(a[4]*25)))
    print('{0:_<38}'.format(''))
    print('{0:.<6}{1}{0:.<6}{2}{0:.<9}{3}{0:.<10}'.format('','รวม',str(att),str(ptt)))
    
def four():
    n=0
    while True:
        print('\tสินค้าในตะกร้ามีดังนี้')
        for i in buy_list:
            n+=1
            print('\t'+str(n)+'.'+i)
        n=0
        c=int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์-1เพื่อออก: '))
        try:
            if c<=len(buy_list) and c!=-1:
                buy_list.pop(c-1)
            elif c==0 and c<=len(buy_list) and c!=-1:
                buy_list.pop(c)
            elif c==-1:
                break
        except:
            print('กรุณากรอกลำดับสินค้าให้ถูกต้อง')

while True:
    print('\tโปรแกรมร้านค้าออนไลน์\n')
    print('1.แสดงรายการสินค้า\n2.หยิบสินค้าเข้าตะกร้า\n3.แสดงจำนวนและรายการสินค้าที่หยิบ\n4.หยิบสินค้าออกจากตะกร้า\n5.ปิดโปรแกรม\n\n')
    choice=input('กรุณาเลือกทำรายการ: ')
    if choice=='1':
        one()
    elif choice=='2':
        two()
    elif choice=='3':
        three()
    elif choice=='4':
        four()
    elif choice=='5':
        choice=input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ')
        if choice=='y':
            break
        elif choice=='n':
            continue
'''
'''
def Introduce(arg1,arg2='com',arg3='ed',arg4='kku'):
    print("Hello, I am "+arg1+","+arg2+" "+arg3+" "+arg4)

Introduce("Python")
Introduce(arg1="Python")
Introduce(arg1="Python",arg3="Sci")
Introduce("Python",arg4="CMU")
'''
'''
#4.2
dic={}
def one():
    volcap=input('เพิ่มคำศัพท์      ')
    ttype=input('ชนิดคำศัพท์ (n.,v.,adj.)   ')
    mean=input('ความหมาย      ')
    dic[volcap]=ttype,mean
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')

def two():
    print('{0:-<15}{1:-<15}{2:-<10}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for w in dic:
        print('{}{:<3}{}'.format(w,'',dic[w]))

def three():
    rword=input('พิมพ์คำศัพท์ที่ต้องการลบ:  ')
    sure=input('ต้องการลบ {} ใช่หรือไม่ (y/n): '.format(rword))
    if sure=='y':
        del dic[rword]
        print('ลบ'+rword+'เรียบร้อยแล้ว')

while True:
    print('พจนานุกรม\n1.เพิ่มคำศัพท์\n2.แสดงคำศัพท์\n3.ลบคำศัพท์\n4.ออกจากโปรแกรม\n\n')
    choice=input('Input Choice: ')    
    if choice=='1':
        one() 
    elif choice=='2':
        two()   
    elif choice=='3':
        three()
    elif choice=='4':
        choice=input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ')
        if choice=='y':
            print('ออกจากโปรแกรมเรียบร้อยแล้ว')
            break
        elif choice=='n':
            continue
'''
'''
#4.3
import time
name_list=[]
score_list=[]
time_list=[]
hit_list=[]
def timee():
    thistime=time.localtime()
    now=time.strftime('%d %B %Y, %H:%M:%S',thistime)
    print(now)
number=int(input('กรุณากรอกจำนวนผู้ซ้อมยิงปืน: '))
for i in range(number):
    print('กรอกข้อมูลผู้ซ้อมคนที่ ',1+i)
    name=input('ชื่่อผู้ซ้อม: ')
    score=float(input('คะแนน: '))
    ttime=float(input('ระยะเวลาที่ใช้: '))
    name_list.append(name)
    score_list.append(score)
    time_list.append(ttime)
    hit_list.append(score/ttime)
for i in range(number):
    j=i
    for j in range(number):
        if hit_list[i] > hit_list[j]:
            q,w,e,r=hit_list[i],name_list[i],score_list[i],time_list[i]
            hit_list[i],name_list[i],score_list[i],time_list[i]=hit_list[j],name_list[j],score_list[j],time_list[j]
            hit_list[j],name_list[j],score_list[j],time_list[j]=q,w,e,r
thistime=time.localtime()
a=time.strftime('%A',thistime)
b=time.strftime('%Y',thistime)
print('Shotgun '+a+' Training ',b,'\nCondition : 1')
timee()
print('-'*77)
print('{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}'.format('NO.','PTS','TIME','COMPETITOR#Name','HIT FACTOR','STATE POINTS','STATE PERCENT'))
print('-'*77)
for i in range(number):
    state_point=(hit_list[i]/hit_list[0])*50
    state_percent=(state_point/(hit_list[0]/hit_list[0]*50))*100
    print('{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}'.format(i+1,int(score_list[i]),time_list[i],name_list[i],'%.4f'%hit_list[i],'%.4f'%state_point,'%.2f'%state_percent))
'''
