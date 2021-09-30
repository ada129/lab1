# задание 1.1
a1=input("Индивидуальный гороскоп для пользователя:")
a1=input("Кем вы были в прошлой жизни:")
a1=input()
print("Ваш знак зодиака -", a1, ", поэтому вы -тонко чувствующая натура ", sep=" ")
# задание 1.2
print("1 бит-минимашльная единица информации","1 байт = 8 бит ",
      "1 Килобит= 1024 байта", "1 Килобайт =1024 байта",
      "1 Килобайт = 8192 бита", sep="\n")
# задание 1.3
first=input()
second=input()
thrid=input()
print(thrid, second, first, sep="\n")
# задание 2.1
print("вы проснулись в подвале. У вас есть 2 варианта действия 1-найти лестницу ,2- попытаться выломать дверь. Введите номер" )
choise=int(input())
if (choise==1):
    print("после долгих поисков вы нашли заветный предмет только она оказалась сломанной 1-попытаться вломать дверь 2-сделать оружие для защиты")
    choise=int(input())
    if(choise==1):
        print("вы не успели , похититель убил вас")
    else:
       if(choise==2):
        print("вы смогли обезвредить похитителя и выбраться на свободу")
       else:
        print("произошла ошибка")
else:
      if( choise==2):
          print("вы смогли взломать дверь 1-искать оружие для самообороны 2 -идти в слепую вперед")
          choise=int(input())
          if (choise==1):
              print("вы смогли выбраться благодаря эффекту неожиданности")
          else:
              if choise==2:
                  print("пока вы искали оружие потеряли драгоценое время")
              else:
                  print("произошла ошибка")
      else:
          print("произошла ошибка")
# задание 2.2
log=input("введите логин:")
if(log.find('@')==-1):
    log=input("введите резервнй адрес:")
    if (log.find('@')!=-1):
        print("OK")
    else:
        print("NO")
else:
    print("NO")
# задание 2.3
mood=input("какое у вас сегодня настроение:")
if (mood.find("хорошее")!=-1 or mood.find("прекрасно")!=-1):
    print("Отлично, у меня тоже все хорошо ")
else:
    if (mood.find("плохо")!=-1):
        print("Ничего , все наладится ")
    else:
        print("Извините я вас не понимаю")
# задание 2.4
chose=input()
if (chose=="да" or chose=="нет"):
    chose=input()
    if (chose == "да" or chose == "нет"):
        print("верно")
    else:
        print("неверно")
else:
    print("неверно")
# задание 2.5
chose=input("Какое время года ваше любимое:")
if chose=="зима":
    chose=input("какой месяц")
    if chose=="декабрь":
        print("Вы любите новогодние праздники")
    elif chose=="январь":
        print("вы любите учиться ")
    elif chose=="февраль":
        print("вам нравиться слякоть")
    else:
        print("некорректный ввод ответа")
elif chose=="весна":
    chose = input("какой месяц")
    if chose == "март":
        print("вы девушка")
    elif chose == "апрель":
        print("вы любите пасху")
    elif chose == "май":
        print("вам нравиться цветение")
    else:
        print("некорректынй ввод ответа")
elif chose=="лето":
    chose = input("какой месяц")
    if chose == "июнь":
        print("вы любите сдавать экзамены")
    elif chose == "июль":
        print("вам нравиться отдыхать")
    elif chose == "август":
        print("вы любите жить моментом")
    else:
        print("некореетный ввод ответа")
elif chose=="осень":
    chose = input("какой месяц")
    if chose == "сентябрь":
        print("вам нравиться учиться")
    elif chose == "октябрь":
        print("вы любите хеллуин")
    elif chose == "ноябрь":
        print("вы ждете зиму")
    else:
        print("неккоретный ввод ответа")
else:
    print("неккоретный ввод ответа")
# задание 3.1
number=float(input())
if (number>0):
    print("+")
elif number<0:
    print("-")
else:
    print("0")
# задание 3.2
number=float(input())
number2=float(input())
sign=input()
if (sign=='-'):
    print(number-number2)
elif sign=="+":
    print(number+number2)
elif sign=="*":
    print(number*number2)
elif (sign=="/" and number2!=0):
    print(number/number2)
else:
    print(888888)
# задание 3.3
year=int(input("введите год:"))
if ((year%4==0 and year%100!=0) or year%400==0):
    print("високостный")
else:
    print("невискостный")
# задание 3.4
number=int(input())
if (number%2==0):
    print("честное")
else:
    print("нечетное")
# задание 3.5
name=input("введите имя :")
print(len(name)*2+3)
# задание 3.6
key=int(input("введите пароль:"))
if (key%10==key//100):
    if (key%10==(key//10)%10):
        print("в числе все цифры одинаковые")
    else:
        print("В числе две цифры повторяются")
elif (key%10==(key//10)%10):
    print("в числе 2 цифры повторяются")
elif (key//100==(key//10)%10):
     print("в числе 2 цифры повторяются")
else:
    print("ок")
# задание 3.7
number=int(input("введите число:"))
if ((number%10+number//100)//2==(number//10)%10):
    print("вы ввели красивое число")
elif ((number%10+(number//10)%10)//2==number//100):
    print("вы ввели красивое число ")
elif ((number//100+(number//10)%10)//2==number//10):
    print("вы ввели красивое число")
else:
    print("Жаль , вы ввели обычное число")
# задание 3.8
number=int(input())
if ((number//100+(number//10)%10)>((number//10)%10+number%10)):
    print(str(number//100+(number//10)%10)+ str((number//10)%10+number%10) )
else:
    print(str((number//10)%10+number%10)+ str(number//100+(number//10)%10))
# задание 3.9
message=input()
cost= len(message)*40
print(cost//100, "рублей ", cost%100, "копеек")
# задание 4.1
line=input()
count=1
while line!="спасибо":
    line=input()
    count+=1
print(count)
# задание 4.2
temp=float(input())
ctemp=0.0
count=0
while temp>-300:
     ctemp+=temp
     temp=float(input())
     count+=1
if (ctemp!=0.0):
    print(ctemp/count)
# задание 4.3
number=int(input())
count=0
while number%2==0:
      count+=1
      number//=2
if (count!=0):
    print(count)
else:
    print("нет")
# задание 4.4
key1=input()
if len(key1)>=8:
    if (key1.find("123")==-1):
        if (input()==key1):
            print("ок")
        else:
            print("различаются")
    else:
        print("простой!")
else:
    print("простой!")
# задание 4.5
number=int(input())
count=1
if (number % 2 == 0):
    number //= 2
else:
    number = number * 3 + 1
while number!=1:
    if (number%2==0):
        number//=2
    else:
        number=number*3+1
    count+=1
print(count)
# задание 4.6
number=int(input())
while number%10==0:
    number=int(input())
# задание 4.7
x=int(input())
y=int(input())
xtec=0
ytec=0
count=0
n=-1
name=input()
while name!="стоп":
   if ytec!=y or xtec!=x:
       if name=="вперед":
           ytec+=int(input())
           if xtec==x and ytec==y:
               n=1
       elif name=="разворот":
           name=input()
           ytec-=int(input())
           count+=1
           if xtec==x and ytec==y:
               n=2
       elif name=="налево":
           name=input()
           xtec-=int(input())
           count+=1
           if xtec==x and ytec==y:
               n=3
       elif name=="направо":
           name=input()
           xtec+=int(input())
           count+=1
           if xtec==x and ytec==y:
               n=4
       count+=1
   name=input()
if n==1:print("север")
elif n==2:print("юг")
elif n==3:print("запад")
else:print("восток")
print(count)
# задание 4.8
count=0
x=0
y=1000
number=578
while count!=10 and (x!=number or y!=number):
    print((x+y)//2)
    if (number<(x+y)//2):
        print(">")
        y=(x+y)//2
    else:
        if number>(x+y)//2:
            print("<")
            x=(x+y)//2
        else:
            print("=")
            break
    count+=1
# задание 5.1
d=int(input())
m=int(input())+10
if (m>12):
    m-=12
x=int(input())
if (x%100==0):
    c=x//100
else:
    c=x//100+1
print((d+((13*m-1)//5)+x%100+((x%100)//4+c//4-2*c+777))%7)
# задание 5.2
count=int(input())
i=0
while count!=1:
    if count%2==0:
        count=count//2
    else:
        count-=1
    i+=1
print(i)
# задание 5.3
count1=int(input())
count2=int(input())
while count1!=0 or count2!=0:
      c=int(input())
      if c==1:
          count1-=int(input())
      else:
          count2-=int(input())
      print(count1,count2)
# задание 5.4
count=int(input())
i=0
while count!=0:
    i+=1
    if i%2==0:
        if count>3:
          print("введите количество камней , максимум 3")
        else:
            print("введите кол-во камней ,максимум ",count)
        count-=int(input())
    else:
        if count>3:
            count-=3
        else:
            count=0
if i%2==0:
    print("пользователь выйграл")
else:
    print("выйграл компьютер")
# задание 5.5
count=int(input())
i=1
while count!=0:
    if i%2==0:
        if count>3:
          print("введите количество камней , максимум 3")
        else:
            print("введите кол-во камней ,максимум ",count)
        count-=int(input())
    else:
        if count>3:
            count-=3
        else:
            count=0
    i+=1
if i%2==0:
    print("пользователь выйграл")
else:
    print("выйграл компьютер")
# задание 5.6
count1=int(input())
count2=int(input())
count3=int(input())
while count2!=0 or count3!=0 or count1!=0:
      n=int(input())
      if (n==1):
          count1-=int(input())
      elif (n==2):
          count2-=int(input())
      else:
          count3-=int(input())
      print(count1,count2,count3)
# задание 5.7
count1=int(input())
count2=int(input())
i=0
while count1!=0 or count2!=0:
    i+=1
    if i%2==0:
        print("введите номер кучи камней ")
        n=int(input())
        if (n==1):
          while True:
              print("введите кол-во камней ")
              n=int(input())
              if n<=count1:
                  break
          count1-=n
        else:
            while True:
                print("введите кол-во камней ")
                n = int(input())
                if n <= count2:
                    break
            count2 -= n
    else:
        if count1!=0:
            count1=0
        else:
            count2=0
if i%2==0:
    print("пользователь выйграл")
else:
    print("выйграл компьютер")
# задание 5.8
count1=int(input())
count2=int(input())
count3=int(input())
i=0
while count1!=0 or count2!=0 or count3!=0:
     i+=1
     if i%2==0:
         print("введите номер кучи ")
         n=int(input())
         if n==1:
             while True:
                 print("введите кол-во камней")
                 n=int(input())
                 if n<=count1:
                     break
             count1-=n
         elif n==2:
             while True:
                 print("введите кол-во камней")
                 n=int(input())
                 if n<=count2:
                     break
             count2-=n
         else:
             while True:
                 print("введите кол-во камней")
                 n = int(input())
                 if n <= count3:
                     break
             count3 -= n
     else:
         if count1!=0:
             count1=0
         elif count2!=0:
             count2=0
         else:count3=0
if i%2==0:
    print("выйграл пользователь")
else:print("выйграл компьютер")
# задание 6.1
n=int(input())
for i in range(n,-1,-1):
    print("Осталось секунд:",i)
print("Пуск")
# задание 6.2
n=int(input())
for i in range(n):
    print(" "*((2*(n-i)//2)),"*"*(2*i+1))
# задание 6.3
for i in range(17):
    g=int(input())
    if (i%g==0):
        print("да")
    else:
        print("нет")
# задание 6.4
n=int(input())
sred=int(input())
count=1
print("0")
tec=0
for i in range(n):
    tec=int(input())
    sred+=tec
    count+=1
    if (tec>sred//count):
        print(">")
    elif (tec<sred//count):
        print("<")
    else:
        print("=")
# задание 6.5
def euclid(zn,zn1):
    while zn!=zn1:
        if zn>zn1:
            zn-=zn1
        else:
            zn1-=zn
    return zn
count=int(input())
chl=int(input())
zn=int(input())
for i in range(count-1):
    chl1=int(input())
    zn1=int(input())
    chl=chl*zn1+chl1*zn
    zn*=zn1
if chl>zn:
    print(chl//zn, end=' ')
    t = euclid(chl%zn, zn)
    print((chl%zn)//t, "/", zn//t)
else:
    t=euclid(chl, zn)
    print(chl//t, "/", zn//t)
# задание 6.6
n=int(input())
k=0.0
pi=3.141592653589793**2
for i in range(1,n+1):
    k+=1/(i**2)
print(pi/k)
# задание 6.7
summ=0
n=int(input())
for i in range(n):
    if (i%2==0):
        summ+=int(input())
    else:
        summ-=int(input())
print(summ)
# задание 7.1
n=int(input())
k=False
for i in range(n):
    tex=input()
    if (tex.find("кот")!=-1 or tex.find("Кот")!=-1):
        k=True
if k:
    print("МЯУ")
else:
    print("НЕТ")
# задание 7.2
tex=input()
k=-1
count=1
while tex!="СТОП":
    if (tex.find("кот")!=-1 or tex.find("Кот")!=-1 and k==-1):
         k=count
    tex=input()
    count+=1
print(k)
# задание 7.3
n=int(input())
words=[]
k=True
for i in range(n):
    words.append(input())
for i in words:
    if (i.find("кот") != -1 or i.find("Кот") !=-1):
        k=True
        break
if k:
    print("МЯУ")
else:
    print("НЕТ")
# задание 7.4
tex=input()
k=-1
count=1
while tex!="СТОП":
    if (tex.find("кот")!=-1 or tex.find("Кот")!=-1 and k==-1):
         k=count
         break
    tex=input()
    count+=1
print(k)
# задание 7.5
tex=input()
count=1
count_cat=0
k=-1
while tex!="СТОП":
    if (tex.find("кот") != -1 or tex.find("Кот") != -1 ):
        if k==-1:
            k=count
        count_cat+=1
    count+=1
    tex=input()
print(count_cat,k)
# задание 7.6
x=int(input())
y=int(input())
count=0
tecx=0
tecy=0
tex=input()
while tex!="стоп":
    if tex=="север":
        tecy+=int(input())
    elif tex=="юг":
        tecy-=int(input())
    elif tex=="запад":
        tecx-=int(input())
    else:
        tecx+=int(input())
    if (tecx!=x or tecy!=y):
        count+=1
    tex=input()
print(count)
# задание 7.7
cat=False
dog=False
n=int(input())
for i in range(n):
    tex=input()
    if (tex.find("кот")!=-1 or tex.find("Koт")!=-1 and not dog):
        cat=True
    if (tex.find("пес")!=-1 or tex.find("Пес")!=-1):
            cat=False
            dog=True
if cat:
    print("Мяу")
else:
    print("Нет")
# задание 7.8
n=int(input())
count=0
one=False
two=False
three=False
while n!=0:
    tex=input()
    if (tex=="раз" and not one and not two and not three ):
        one=True
        count+=1
    elif( tex=="два" and one and not two and not three ):
        two=True
        count+=1
    elif (tex=="три"and one and  two and not three  ):
        three=True
        count+=1
    elif (tex=="четыре" and one and  two and  three  ):
        count+=1
        one=False
        two=False
        three=False
    else:
        n-=1
        print("Правильных отчетов было ", count, ", но теперь начинайте заного")
        count=0
        one=False
        two=False
        three=False
print("На сегодня хватит")
# задание 7.9
def fac(number):
    f=1
    for i in range(1,number+1):
        f*=i
    return f
while True:
    number=int(input())
    operation=input()
    if (operation=="+"):
        print(number+int(input()))
    elif (operation=="-"):
        print(number-int(input()))
    elif (operation=="*"):
        print(number*int(input()))
    elif (operation=="/"):
        print(number//int(input()))
    elif(operation=="%"):
        print(number%int(input()))
    elif(operation=="!"):
        print(fac(number))
    else:
        break
# задание 7.10
purchase=0
sale=0
pre=int(input())
n=pre
while n!=0:
    n=int(input())
    if (n>pre and purchase==0):
        purchase=n
    if (n<pre and sale==0 and purchase!=0):
        sale=n
    pre=n
print(purchase,sale,sale-purchase)
# задание 8.1
n=int(input())
m=int(input())
for i in range(m):
    for j in range(n):
        print((n+1)/(m+1))
# задание 8.2
n=int(input())
m=int(input())
sym=input()
for i in range(n):
    if (i==0 or i==n-1):
        print(sym*m)
    else:
        print(sym," "*(m-2),sym,sep="")
# задание 8.3
money=int(input())
count=int(input())
for i in range(1,money//20):
    for j in range(count-i):
        if (i*20+j*10+(count-i-j)*5<=money):
            print(i,j,count-i-j,i*20+j*10+(count-i-j)*5)
        else:
            break



