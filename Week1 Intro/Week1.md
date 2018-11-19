#Sum of three numbers

a = int(input())
b = int(input())
c= int(input())
print(a+ b+c)

#Area of right-angled triangle

b = int(input())
h=int(input())
result = 0.5*b*h
print(result)

#Hello Harry
name = input()
print("Hello,",str(name)+"!")

#Apple sharing
n = int(input())
k=int(input())
result = k//n
print(result)
print(k%n)

#Previous and next
a= int(input())
print("The next number for the number", str(a),"is", str(a+1))
print("The previous number for the number",str(a),"is",str(a-1))

#School desks
a = int(input())
b= int(input())
c= int(input())
result = 0
if a%2==0:
    result += a/2
else:
    result +=(a+1)/2
if b%2 == 0:
    result +=b/2
else:
    result+= (b+1)/2
if c%2==0:
    result +=c/2
else:
    result +=(c+1)/2
print(result)

#Minimum of two numbers
a=int(input())
b=int(input())
print(min(a,b))

#Sign function
a = int(input())
if a>0:
    print(1)
elif a<0:
    print(-1)
else:
    print(0)

#Minimum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(min(a,b,c))

#Equal numbers
a = int(input())
b = int(input())
c = int(input())
if a == b and b== c:
    print("3")
elif a==b or b==c or a==c:
    print("2")
else:
    print("0")

#Rook move
x1 =int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if (x1-x2)==0 or (y1-y2)==0:
    print("YES")
else:
    print("NO")

#Chess board - same color
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if abs(x1-x2)%2 == 0 and abs(y1-y2)%2==0:
    print("YES")
elif abs(x1-x2)%2 !=0 and abs(y1-y2)%2!=0:
    print("YES")
else:
    print("NO")

#King move
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if abs(x1-x2)==1 and abs(y1-y2)==1:
    print("YES")
elif abs(x1-x2)==1 and abs(y1-y2)==0:
    print("YES")
elif abs(x1-x2)==0 and abs(y1-y2)==1:
    print("YES")
else:
    print("NO")

#Bishop moves
first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
hor_change = abs(third - first)
ver_change = abs(fourth - second)

if hor_change == ver_change:
    result = 'YES'
else:
    result = 'NO'
print(result)

#Queen move
first = int(input())
second = int(input())
third = int(input())
fourth = int(input())

hor_change = abs(third - first)
ver_change = abs(fourth - second)

if hor_change ==0:
    result = "YES"
elif ver_change == 0:
    result = "YES"
elif hor_change == ver_change:
    result = "YES"
else:
    result = "NO"
    
print(result)


#Knight move
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
h_diff = abs(x1-x2)
v_diff = abs(y1-y2)
if h_diff ==1 and v_diff ==2:
    print ("YES")
elif h_diff==2 and v_diff==1:
    print("YES")
else:
    print("NO")

#Chocolate bar
n=int(input())
m=int(input())
k=int(input())
if n*m<k:
    print("NO")
elif k%n==0 or k%m ==0:
    print("YES")
else:
    print("NO")

#Leap year
x = int(input())
if x%400 == 0:
    print("LEAP")
elif x%4 == 0 and x % 100 != 0:
    print("LEAP")
else:
    print("COMMON")


#Fractional part
a = float(input())
print(a-int(a))

#First digit after decimal point
a= float(input())
print(int((a-int(a))*10))

#Car route
N = int(input())
M = int(input())
if M%N==0:
    print(M/N)
else:
    print(M//N+1)

#Digital clock
N= int(input())
hour = N//60
minute = N-hour*60
print(str(hour),str(minute))

#Total cost
x=int(input())
y=int(input())
n=int(input())
d = x*n
c = y*n
if c>100:
    d=d+c//100
    c=c-((c//100)*100)
    

print(d,c)


#Clock face - 1
a = int(input())
b = int(input())
c= int(input())
first = 30*a
second = b/2
third = 30/3600*c
result = first + second + third
print(result)

#Clock face - 2
a= float(input())
hour = a//30
minute = a-(hour*30)
result = minute*12
print(result)

#Sum of digits
a = int(input())
first = str(a)[-1]
second= str(a)[-2]
third = str(a)[-3]
result = int(first)+int(second)+int(third)
print(result)

#Tens digit
a = int(input())
left = a%10
result = (a-left)/10
print(str(int(result))[-1])

#Last digit of integer
a = int(input())
print(str(a)[-1])

