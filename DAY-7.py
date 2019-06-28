#!/usr/bin/env python
# coding: utf-8

# In[12]:


def printEven(n):
    cnt=0
    sum=0
    while(cnt!=n):
        if(cnt%2==0):
            sum=sum+cnt
        cnt=cnt+1
    return sum
print((printEven(20));
    


# In[19]:


def factorsList(n):
    i=1
    while(i!=n):
        if(n%i==0):
            print(i,end =" ")
        i=i+1
    return i
factorsList(int(input("enter n   ")))


# In[23]:


list1=[1,2,3,4,5]
#entire list
print(list1)
print(list1[1])


# In[36]:


list2=["akhil,arvind,anil,akash"]
for x in list2:
    print(x)


# ## for loop
# #syntax
#     for <variable> in <seq>:
#     <statements>
# 

# In[43]:


lst1=[1,2,3,4,5,6,7]
for x in lst1:
    print(x,end=" ")

print(lst1[4])
print(lst1[3:6])
print(lst1[0:3])
print(lst1[:3])
print(lst1[:7])
print(lst1[0:])


# In[68]:


lst1=[1,2,3,4,5,6,7,8,9,10]
for x in lst1:
    print(x,end = "  ")
print() 
print(lst1[1:-2])
print(lst1[::1])
print(lst1[::2])
print(lst[::3])
print(lst[::4])
print(lst1[-1])


# # list with range function
# ##range(number):
# 0 to number

# In[ ]:





# In[77]:


lst=["anil","adarsh","akhil",1]
print(lst)

lst[2]=15
print(lst)

del lst[3]
print(lst)
lst[1]="gitam"
print(lst)
lst1=[1,2,3]
print(lst+lst1)


# In[98]:


lst1=[1,2,3,4,5]
print(lst1)
del lst1[2]
print(lst1)
len(lst1)
lst1.append(15)
print(lst1)
lst1.append(150)
print(lst1)
lst1.append(1)
lst1.append(3)
lst1.append(1)
print(lst1)
print(lst1.count(1))
lst1.count(3)
lst1.append(lst[2])
print(lst1)


# # LIST METHODS
# ## APPEND(OBJ)
# the methods appends a passed objests into a exixsting list
# ####   lst.append()
# 
# ## COUNT METHOD
# this method returns the count of object how many times it's repeated.
# #### lst.count()
# ## insert method
# inserts
# #### lst.insert(index.obj)
# ## remove method
# the remove method removes the passed from the first obj from left direction
# #### lst.remove(obj)
# ## reverse method
# #### lst.reverse()

# In[114]:


lst1=["gitam","python","raptor",1,5,"python","python"]
print(lst1)
lst1.index(1)
print(len(lst1))
lst1.insert(1,2019)
print(lst1)
print(len(lst1))
lst1.insert(6,2020)
print(lst1)
print(len(lst1))


# In[118]:


lst1=["gitam","python","raptor",1,5,"python","python"]
print(lst1)
lst1.remove("python")
print(lst1)
lst1.remove("python")
print(lst1)
lst1.reverse()
print(lst1)


# # data structures
# ### 1 searching a data.
#      #### linear search
#      #### binary search
# ### 2 sort the data.
# ### 3 store the data.

# In[9]:


def linearSearch(a,tarItem):
    flag=0
    for i in range(len(a)):
        if(a[i]==tarItem):
            flag=1
            break
    if(flag!=0):
        print(" found")
    else:
        print("notfound")
a=[1,2,3,4,5]
linearSearch(a,1)


# In[8]:


def linearSearchduplicate(a,taritem):
    flag=0
    for i in range(len(a)):
        if a[i]==taritem:
            flag=flag+1
    print(flag)    
a=[9,1,6,1,5,9,15,16]
linearSearchduplicate(a,9)
            
            


# In[4]:


def linearExample(a,taritem):
    
    for i in range(len(a)):
        if(a[i]==taritem):
            print(i,end=" ")
            
a=[1,2,3,4,5,5]
linearExample(a,5)
            


# In[2]:


def linearExample(a,taritem):
    flag=0
    for i in range(len(a)):
        if(a[i]==taritem):
            j=0
            while j!=i+1:
                print("!",end = " ")
                j=j+1
            print(end = " ")
a=[1,2,3,4,5,5]
linearExample(a,5)
            


# In[4]:


def linearExample(a):
    sum=0
    for i in range(len(a)):
        if(a[i]%3==0 and a[i]%5==0):
            sum=sum+a[i]
    print(sum)
a=[15,12,2,9,18,36,45]
linearExample(a)

            
    


# In[14]:


def linearExample(a):
    l=[]
    for i in range(len(a)):
        if(i!=0 and  i!=(len(a)-1)):
            l.append(a[i-1]*a[i+1])
        else:
            l.append(a[i])
    print(l)
a=[1,2,3,4,5]
linearExample(a)


# In[16]:


def linearExample(a):
    for i in range(len(a)):
        if(i==0 or i==len(a)-1):
            print(a[i],end=" ")
        else:
            print(a[i-1]*a[i+1],end = " ")
a=[1,2,3,4,5]
linearExample(a)


# In[19]:


def linearExample(a):
    for i in range(len(a)):
        if(i==0 or i==len(a)-1):
            print(a[i],end=" ")
        elif(a[i-1]%2==0 and a[i+1]%2==0):
            print(a[i],end = " ")
a=[1,6,9,4,16,19,22]
linearExample(a)


# In[24]:


def numberTolistconversion(n):
    l = []
    while(n!=0):
        r=n % 10
        l.append(r)
        n=n//10
    l.reverse()
    print(l)
n=int(input("enter a number   "))
numberTolistconversion(n)


# In[25]:


def numberTolistconversion(n):
    l = []
    while(n!=0):
        l.append(n%10)
        n=n//10
    l.reverse()
    return l
n=int(input("enter a number   "))
numberTolistconversion(n)


# In[33]:


def listTonumberconversion(a):
    x=0
    for i in range(len(a)):
        x=x*10+a[i]
    return x    
a=[1,2,3,4,5]
listTonumberconversion(a)


# In[34]:


def linearExample(a):
    for i in range(len(a)):
        if(a[i]%2==0):
            print(a[i],end=" ")
a=[1,6,9,4,16,19,22]
linearExample(a)


# In[39]:


def listTonumberconversion(a):
    l=[]
    for i in a:
        if(i%2==0):
            l.append(i)
    return l
a=[1,2,3,4,5]
print(listTonumberconversion(a))


# In[ ]:




