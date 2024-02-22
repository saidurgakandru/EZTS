#Day-1:

#second largest approach-1
'''a=int(input())
b=int(input())
c=int(input())
if (a<b and a>c) or (a>b and a<c):
    print(a)
elif (b>a and b<c) or (b<a and b>c):
    print(b)
else:
    print(c)'''
#second largest approach-2
'''a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    a=0
elif b>c and b>a:
    b=0
else:
    c=0
if a>b and b>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)'''

#print 1000 hello worlds
'''for i in range(1000):
    print("Hello World")'''
#relation between a and b
'''a,b=input().split()
a,b=int(a),int(b)
if a>b:
    print("a > b")
elif a==b:
    print("a == b")
else:
    print("b > a")'''
#traingle
'''a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
if a+b>c or b+c>a or c+a>b:
    print("Yes")
else:
    print("No")'''
#apples distribution for children
'''a=int(input())
b=int(input())
c=0
while b>a:
    c+=a
    if c<b:
        b-=c
print(b)'''
#reverse of number approach-1
'''a=int(input())
b=a
if a<0:
    b=a*(-1)
rev=0
while b>0:
    rev=rev*10+b%10
    b=b//10
if a<0:
    print(-1*(rev))
else:
    print(rev)'''

#candy
'''a=int(input())
d=0
for i in range(a):
    b,c=map(int,input().split())
    d=(b-c)
    if b>c:
        if d%4==0:
            print(d//4)
        else:
            print((d//4)+1)
    else:
        print(0)'''
#pizza
'''a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    ts=b*c
    tp=0
    c=0
    while ts>4:
        tp=tp+1
        ts=ts-4
    if tp==0:
        print(tp)
    else:
        print(tp+1)'''
'''ezts'''

#DAY-2
'''def myfun(x):
    x[0]
list_a=[10,11,12,13,14,15]
myfun(list_a)
print(list_a)'''

'''a=int(input())
def profit(b):
    c=int((b*50)-(0.7*b*50))
    return c
def testcase(x):
    if x>0:
        b=int(input())
        print(profit(b))
    else: 
        return
    testcase(x-1)
      
testcase(a)'''
#movie
'''x,y=map(int,input().split())
def movie(x,y):
    print(int((y/2)+(x-y)))
movie(x,y)'''
#lucky-four
'''a=int(input())
def luckyfour(b):
    c=0
    while b>0:
        if b%10==4:
            c+=1
        b=b//10
    return c
def testcase(x):
    if x>0:
        b=int(input())
        print(luckyfour(b))
    else: 
        return
    testcase(x-1)
testcase(a)'''
#factorial-1
'''a=int(input())
b=1
for i in range(a):
    b=b*i+b
print(b)'''
#factorial-2
'''a=int(input())
def factorial(a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)
    
print(factorial(a))'''

a=int(input())
b=(a*10)+3
rev=1
def reverse(b):
    rev=1
    while b>0:
        rev=rev*10+b%10
        b=b//10
    return rev

c=reverse(b)
c=c*10+3
print(reverse(c))











    
