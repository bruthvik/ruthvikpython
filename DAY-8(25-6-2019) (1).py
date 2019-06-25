#!/usr/bin/env python
# coding: utf-8

# # BINARY SEARCH     -- sorted  list
# ## THIS BINARY SEARCH -- UNIQUE LIST
# ### binary search algo
# #### can be applied only on sorted and duplicate list

# In[10]:


def binarySearch(a,lIndex,rIndex,taritem):
    while(lIndex<= rIndex):
        mIndex=lIndex+(rIndex-lIndex)//2
        if( a[mIndex]==taritem):
            return mIndex
        if(a[mIndex]>taritem):
            rIndex = mIndex - 1
        else:
            lIndex=mIndex+1
    return -1
list1 =[1,4,9,15,25,45,57,88,98]
res=binarySearch(list1,0,8,9)
if res != -1:
    print("item is found")
else:
    print("item is not found")


# # SORTING ALGORITHMS
# ### BUBBLE SORT
# ##### it compares the adjacent items if the first item is greater than second item then there would be a swap of the two numbers
# #### the complex n*n

# In[11]:


def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    for i in range(len(a)):
        print(a[i],end=" ")
lst1=[10,1,25,6,18,3]
bubbleSort(lst1)


# In[15]:


lst1=[1,3,24,36,81,72]
lst1.sort()
print(lst1)


# # strings in python
# ### a string is a sequence of charaters 
# ### The conversion of character to anumber is happens with ASCII Number
# ## ASCII NUMBERS
# ###
# ### A-Z -------65-90
# ### a-z --------97-122
# ### 0-9---------48-57

# In[17]:


str = "application"
print(str)

str1='application'
print(str1)
str2 = """application test
           working
           completed
           list 
           strings
           python"""
print(str2)


# In[18]:


str="application"
print(str)
print("str[0] = ",str[0])
print("str[1] = ",str[1])
print("str[-1]= ",str[-1])
print("str[-3]= ",str[-3])
print("str[1:5]=",str[1:5])
print("str[5:-2]=",str[5:-2])
print("str[::-1=]",str[::-1])


# # palindrome of a string

# In[4]:


def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
print(isPalindrome("python"))
print(isPalindrome("jalaj"))


# In[5]:


n = int(input("enter a number"))
cnt=0
while n!=0:
    cnt=cnt+1
    n=n//10
print(cnt)


# In[8]:


def countDigits(n):
    return len(str(n))
countDigits("application")


# In[41]:


def countUpper(str):
    c=0
    for i in str:
        if i.isupper():
            c=c+1
    return c
print(countUpper("Application"))
print(countUpper("TeST"))


# In[43]:


def count(str):
    c=0
    for i in str:
        if i.islower():
            c=c+1
    return(c)
print(count("Application"))
print(count("TeST"))


# In[40]:


def count(str):
    lst = list(str)
    return len(lst)
count("application")


# In[42]:


def countUppercase(str):
    cnt=0
    lst = list(str)
    for x in range(len(lst)):
        if ord((lst[x]))>=65 and ord(lst[x])<=90:
            cnt=cnt+1
    return cnt
print(countUppercase("appliCAtion"))
print(countUppercase("TeST"))


# In[44]:


def printDigits(str):
    s=''
    for x in str:
        if x.isdigit():
            s=s+x
    return s

print(printDigits("applic123"))    


# In[52]:


def countUppercase(str):
    lst = list(str)
    for x in range(len(lst)):
        if ord((lst[x]))>=48 and ord(lst[x])<=57:
            print(chr(ord(lst[x])),end="")
    

countUppercase("TeST12345")


# In[1]:


def sumOfdigits(str):
    sum=0
    lst = list(str)
    for x in range(len(lst)):
        if ord((lst[x]))>=48 and ord(lst[x])<=57:
            sum=sum+ord(lst[x])-48
    return sum
sumOfdigits("TeST123456789")


# In[3]:


def sumOfdigits(str):
    sum=0
    lst = list(str)
    for x in range(len(lst)):
        if ord((lst[x]))>=48 and ord(lst[x])<=57:
            print(ord(lst[x]),end=" ")
sumOfdigits("TeST123456789")


# # order function
# ## it returns the ASCII value of the given character

# In[7]:


def sumOfevendigits(str):
    sum=0
    lst = list(str)
    for x in range(len(lst)):
        if ord((lst[x]))>=48 and ord(lst[x])<=57:
            if(ord(lst[x])%2==0):
                sum=sum+ord(lst[x])-48
    return sum
sumOfevendigits("TeST123")


# In[10]:


def sumOfevendigits(str):
    sum=0
    lst = list(str)
    for x in range(len(lst)):
        if ord((lst[x]))>=48 and ord(lst[x])<=57:
            ac = ord(lst[x])-48
            if(ac%2==0):
                sum=sum+ac
    return sum
sumOfevendigits("T2eST123456987")


# In[ ]:




