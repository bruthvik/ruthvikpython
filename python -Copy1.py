#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=10
while(n>=1):
    print(n)
    n=n-1


# In[1]:


x=-22
while(x>=-45):
    print(x)
    x=x-1


# In[2]:


x=int(input("enter the number"))
r=0
while(x>0):
    r=x%10
    print(r)
    x=x//10
    
    


# In[6]:


x=int(input("enter the number"))
r=0
s=0
while(x>0):
    r=x%10
    x=x//10
    if(r%2==0):
        s=s+r
print(s)


# In[9]:


x=int(input("enter the digit"))
r=0
while(x!=0):
    r=x%10
    if(r==0):
        print("zero")
    elif(r==1):
        print("one")
    elif(r==2):
        print("two")
    elif(r==3):
        print("three")
    elif(r==4):
        print("four")
    elif(r==5):
        print("five")
    elif(r==6):
        print("six")
    elif(r==7):
        print("seven")
    elif(r==8):
        print("eight")
    elif(r==9):
        print("nine")
    x=x//10


# In[2]:


x=int(input("enter the number 1 " ))
y=int(input("enter the number 2 " ))
z=int(input("enter the number 3 " ))
count=0
while(y<z):
    t=y+1
    while(t>0):
        r=t%10
        if(r==x):
            count=count+1
        t=t//10
    y=y+1
print(count)

        
    


# In[9]:


def printNaturalnnumbers(n):
    cnt=1
    while(cnt<=n):
        print(cnt,end=" ")
        cnt=cnt+1;
    print()
    return
printNaturalnnumbers(10);
printNaturalnnumbers(15);


# In[22]:


def findFact(n):
    fact=1
    while(n!=0):
        fact=fact *n
        n=n-1
    return fact;

print(findFact(int(input("enter n  "))));


# In[5]:


def countOfpalindromes(n1,n2):
    cnt=0
    while(n1<n2):
        buffer=n1
        sum=0
        while(n1>0):
            r=n1%10
            sum=(sum * 10)+r
            n1=n1//10
        if(buffer==sum):
            cnt=cnt+1
        n1=buffer
        n1=n1+1
    return cnt
    
print(countOfpalindromes(1,10));
    
    


# In[ ]:





# In[ ]:




