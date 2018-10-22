1. List of Squares 

n =int(input())
i=1
li=[]
while i**2<=n:
    li.append(i**2)
    i+=1
for x in li:
    print(x)

2. Least Divisor <https://snakify.org/en/lessons/while_loop/problems/least_divisor/> (Easy)

n = int(input())
divisor = 2
li = []
while n>=divisor:
    if n%divisor ==0:
        li.append(divisor)
    divisor +=1
print(min(li))

3. The Power of Two <https://snakify.org/en/lessons/while_loop/problems/powers_of_two/> (Medium)

n = int(input())
x = 0
li=[]
while pow(2,x)<=n:
    x +=1
    li.append(x)
biggest = max(li)-1
print(biggest)
print(pow(2,biggest))
4. Morning Jog <https://snakify.org/en/lessons/while_loop/problems/morning_jog/> (Medium)
x= int(input())
y=int(input())
count = 1
while x<y:
    count+=1
    x=x*1.1
print(count)

5. The Length of the Sequenc <https://snakify.org/en/lessons/while_loop/problems/seq_len/> (Easy)
x= int(input())
count = 0
while x !=0:
    count+=1
    x=int(input())
print(count)
6. The Sum of the Sequence <https://snakify.org/en/lessons/while_loop/problems/eq_sum/> (Easy)
x=int(input())
sum= 0
while x!=0:
    sum+=x
    x=int(input())
print(sum)
7. The Average of the Sequence <https://snakify.org/en/lessons/while_loop/problems/seq_avg/> (Easy)
count =0
summ=0
x = int(input())
while x!=0:
    count +=1
    summ+=x
    x=int(input())
print(summ/count)
8. The Maximum of the Sequence <https://snakify.org/en/lessons/while_loop/problems/seq_max/> (Easy)
x = int(input())
lar = 0
while x!=0:
    if x>lar:
        lar = x
    x=int(input())
print(lar)
9. The Index of a Maximum of a Sequence <https://snakify.org/en/lessons/while_loop/problems/seq_index_of_max/> (Medium)
x=int(input())
count = 0
li=[]
while x!=0:
    li.append(x)
    x=int(input())
print(li.index(max(li))+1)

10. The Number of Even Elements of a Sequence <https://snakify.org/en/lessons/while_loop/problems/seq_num_even/> (Easy)
x = int(input())
count = 0
while x!=0:
    if x%2==0:
        count+=1
    x=int(input())
print(count)
11. The Number of Elements that are Greater than the Previous One <https://snakify.org/en/lessons/while_loop/problems/seq_increasing_neighbours/> (Medium)
last_number=int(input())
last = 0
count = 0

while last_number!=0:
    next = int(input())
    if next> last_number and next !=0:
        count +=1
    last_number = next
print(count)
12. The Number of Elements equal to the Maximum <https://snakify.org/en/lessons/while_loop/problems/seq_num_maximal/> (Hard)

13. Fibonacci Numbers <https://snakify.org/en/lessons/while_loop/problems/kth_fibonacci/> (Medium)
n =int(input())
first = 0
second = 1
f_num=0
for i in range(0,n-1):
    f_num = first + second
    first = second
    second = f_num

if n ==1:
    f_num=1

print(f_num)
14. The Index of a Fibonacci Number <https://snakify.org/en/lessons/while_loop/problems/is_fibonacci/> (Hard)
15. The Maximum Number of Consecutive Equal Elements <https://snakify.org/en/lessons/while_loop/problems/seq_max_chunk_of_repetitions/> (Hard)


Use for loops for:
16. Series1 <https://snakify.org/en/lessons/for_loop_range/problems/series_1/> (Easy)
a = int(input())
b = int(input())
for x in range(a,b+1):
    print(x)

17. Series2 <https://snakify.org/en/lessons/for_loop_range/problems/series_2/> (Easy)
a = int(input())
b = int(input())
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in reversed(range(b,a+1)):
        print(i)

18. Sum of Ten Numbers <https://snakify.org/en/lessons/for_loop_range/problems/sum_of_ten_numbers/> (Easy)
su = 0
for i in range(0,10):
    x=int(input())
    su+=x
print(su)
19. Sum of N Numbers <https://snakify.org/en/lessons/for_loop_range/problems/suf_of_n_numbers/> (Easy)
n = int(input())
su=0
for x in range(n):
    new=int(input())
    su+=new
print(su)
20. Factorial <https://snakify.org/en/lessons/for_loop_range/problems/factorial/> (Easy)
x = int(input())
f=1
i=1
for i in range(1,x+1):
   f=f*i
print(f)
21. The Number of Zeros <https://snakify.org/en/lessons/for_loop_range/problems/how_many_zeroes/> (Medium)
n=int(input())
count=0
for i in range(0,n):
    i=int(input())
    if i == 0:
        count +=1
        
        
print(count)

22. Adding Factorials <https://snakify.org/en/lessons/for_loop_range/problems/sum_of_factorials/> (Hard)
n = int(input())
sum = 0

def fac(n):
    num = 1
    for n in range(n,0,-1):
        num = num * n
    return num

for i in range(0,n+1):
    sum+=fac(i)

print(sum-1)

23. Ladder <https://snakify.org/en/lessons/for_loop_range/problems/ladder/> (Hard)
n=int(input())
ls=list(range(0,n))
line_num=[i+1 for i in ls]

for i in line_num:
    line = list(range(1,i+1))
    print("".join(str(x) for x in line))


24. Lost Card <https://snakify.org/en/lessons/for_loop_range/problems/lost_card/> (Medium)
n=int(input())
ls=list(range(0,n))
ls=[i+1 for i in ls]

for i in range(0,len(ls)-1):
    j = int(input())
    ls.remove(j)
print(ls[0])
   
   





Use functions for:
25. The Length of the Segment <https://snakify.org/en/lessons/functions/problems/length_of_segment/> (Easy)

import math
x1 = float(input())
y1= float (input())
x2=float(input())
y2=float(input())

def distance(x1,y1,x2,y2):
    result = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(result)
distance(x1,y1,x2,y2)

26. Negative Exponent <https://snakify.org/en/lessons/functions/problems/negative_power/> (Medium)

a =float(input())
n= int(input())

def p(x,y):
    result = a**n
    return result
print(p(a,n))

27. Uppercase <https://snakify.org/en/lessons/functions/problems/capitalize/> (Easy)

x = input()
new_list = []
def capitalize(word):
    first_letter=chr(ord(word[0])-32)
    new_word = first_letter+word[1:]
    return new_word

li = x.split(" ")

for i in li:
    j = capitalize(i)
    new_list.append(j)
    
print(" ".join(new_list))

