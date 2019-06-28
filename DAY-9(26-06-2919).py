#!/usr/bin/env python
# coding: utf-8

# In[2]:


def caseConversion(str):
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x]) >=65 and ord(lst[x])<=90:
            lst[x]=ord(lst[x]) + 32
        elif ord(lst[x]) >=97 and ord(lst[x]) <= 122:
            lst[x] = ord(lst[x]) - 32
    return str
print(caseConversion("appLiZtO"))
        


# # islower()
# ### METHOD RETURNS THE OUTPUT EITHER TRUE OR FALSE IF IT IS TRUE THE GIVEN CHARACTER LOWER CASE THEN IT RETURNS FALSE

# In[5]:


s = 'python is Easy programming to learn and interesting'
print(s.islower())


# In[9]:


s = 'Application'
s1 = 'ANIL'
print(s.isupper())
print(s1.isupper())


# In[10]:


s='ANIL'
print(s.upper())


# # isnumeric()
# ## returns true or false

# In[13]:


s = "678"
s1 = "app2345"
print(s.isnumeric())
print(s1.isnumeric())


# # isalpha()
# ## returns true or false
# ### if it as alphabetic characters it returns true or vice-versa

# In[16]:


s = "Application"
s1 = "App1889"
print(s.isalpha())
print(s1.isalpha())


# # istitle()
# ## returns true or false
# ### if title given string is in title case it returns true or otherwise false
# 

# In[19]:


s = "python Programming"
s1 = "Python"
print(s.istitle())
print(s1.istitle())


# # isspace()
# ## returns true or false
# # ascii number space is 32

# In[27]:


s= " "
s1=" application programme "
print(s.isspace())
print(s1.isspace())


# ### string methods
# #### 1.join()        : join() method will concatenate two strings
# 
# 
# #### 2.spli()        :split() returns a list of strings that are seprated by whitespace into a seprate individual string
# 
# 
# #### 3.replace() :replace() it replaces the original with a substring

# In[32]:


print("    ".join(["python","programming","easy"]))


# In[36]:


s = "Python , Programming , is Easy"
print(s.split())
print(s.split("a"))
print(s.split(","))


# In[39]:


s= "python programming is easy to learn"
lst = s.split()
print(lst)
print(lst.index("is"))


# In[40]:


s= "python programming is easy to learn"
lst = list(s)
print(lst)


# In[44]:


s = "python programming"
print(s.replace("gra","application"))


# # PYTHON --- TUPLES
# ## A TUPLE is asequence of a set of objects is similar to the list
# ### the diffrences of the list and the tuples are these can not be changed unlike list
# ## list will use square brackets to hold the objects
# ### tuples will use paranthesis to hold objects
# ## TUPLES ARE USEFULL WHEN THE GIVEN INPUT IS ONLY FOR READ PURPOSE

# In[45]:


t1 =("Pyhton" "Programming","1989","2019","machine learning","AI")
t2 =(1,2,3,4,5)
print(t1)
print(t2)


# In[48]:


t1=("Python","Programming","1989","2019","machine learning","AI")
print("t1[0]= ",t1[0])
print("t1[2]= ",t1[2])
print("t1[-1]= ",t1[-1])
print("t1[1:4]= ",t1[1:4])
print("t1[2:-2]= ",t1[2:-2])


# In[54]:


t1=("Python","programming","1989","2019","machnine learning","AI")
print(t1)
## not supports
# t1[2]=2019
# del t1[2]


# In[55]:


t1=("Python","programming","1989","2019","machnine learning","AI")
print(t1)
del t1
print(t1)


# In[57]:


t1 = ("python","programming")
t2 = (1989,2019,"ML","AI")
t3 = t1+t2
print(t3)


# # TUPLE METHODS
# ## 1. len(tuple)**              --len of a tuple
# ## 2. max(tuple)**            --max value from a tuple
# ## 3.min(tuple)**              -- it returns the minimum value from the tuple
# ## 4.cmp(tuple1,tuple2)**--it returns the value as 1 or -1

# In[58]:


t1=("Python","programming","1989","2019","machnine learning","AI")
print(len(t1))


# In[59]:


t1=(12,34,56,7,89)
t2=("Python","programming",1989,"2019","machnine learning","AI")
print(max(t1))
print(max(t2))


# In[61]:


t1=(12,45,65,1,3)
print(min(t1))


# In[62]:


t1=(1,2,3,4,5)
t2=(1,2,3,4,5)
print(t1)
print(t2)
a = cmp(t1,t2)
print(a)


# In[67]:


list1=["Python","programming","1989","2019","machnine learning","AI"]
print(list1)
tuple1=tuple(list1)
print(tuple1)


# # PYTHON DICTIONARY
# ## in dictionary each key is seperated by : colon symbol
# 
# ## user data can be seperated by the coma , operator
# #### EXAMPLE 1
# ######   USER1={'NAME':'ANIL','AGE':29}
# # methods of dictionary objects
# ### len(dicobj)**;returns a number which is having length
# ### str(obj)** returns the eqo string to dic object
# ### copy()** copies the dtata from one to other dic
# ### items()** it lists out all the key words and items 
# ### values()**it gives all the values

# In[ ]:





# In[71]:


user1={'name':'anil','age':29,'emailid':'anil@gmail.com','mobile number':'3849837489137'}
print("user1[name] = ",user1['name'])
print("user1[emailid] = ",user1['emailid'])
print("user1[age] = ",user1['age'])
print("user1[mobile number] =", user1['mobile number'])


# In[78]:


user1={'name':'anil','age':29,'emailid':'anil@gmail.com','mobile number':'3849837489137'}
print(user1['emailid'])
#update the dictionary object data
user1['emailid']='brytg@gmail.com'
print(user1['emailid'])
user1['address'] = 'hyderabad'
print(user1['address'])
print(user1)


# In[80]:


user1={'name':'anil','age':29,'emailid':'anil@gmail.com','mobile number':'3849837489137'}
print(user1['emailid'])
del user1['emailid']
print(user1['emailid'])


# In[86]:


user1={'name':'anil','age':29,'emailid':'anil@gmail.com','mobile number':'3849837489137'}
del user1['emailid']
user1.clear
del user1


# In[94]:


user1={'name':'anil','age':29,'emailid':'anil@gmail.com','mobile number':'3849837489137'}
print(len(user1))
user1['adress']='hyderabad'
print(user1)


# In[97]:


user1={'name':'anil','age':29,'emailid':'anil@gmail.com','mobile number':'3849837489137'}
user2=user1.copy()

print(user1)
print(user2)
user1['address'] = 'hyderabad'

print(user1)
print(user2)


# In[99]:


user1={'name':'anil','age':29,'emailid':'anil@gmail.com','mobile number':'3849837489137'}
print(user1.items())


# In[101]:


user1={'name':'anil','age':29,'emailid':'anil@gmail.com','mobile number':'3849837489137'}
user2 = user1.copy()
print(user1.values())
print(user2.values())


# # STRING FORMATTING
# ## %s %d

# In[109]:


lst = ['python','programming']
print("%s %s"%(lst[0],lst[1]))
print(lst[0],lst[1])
print("{} {}".format(lst[0],lst[1]))


# In[111]:


print('1.1'.isnumeric())


# In[13]:


print('abcdefcdghcd'.split('cd', 2))


# # 1. add new contact --- done
# # 2. search for contacts --- done
# # 3. list of all the contacts---done
#      ### 3.1 name1-- phone1
#      3.2 name2------phone2
#      3.3 imporyting new contacts--done
#      3.4 merge to existing contacts---done
#      

# In[6]:


contacts = {}
def addContact(name,phone):
    #verify that the contact does not exist
    if name not in contacts:
        contacts[name]=phone
        print("contact %s added "% name)
    else:
        print("contact %s is already exists" % name)
    return
addContact("anil",764836234)
addContact("harsha",36547316)
addContact("harsh",487343657)


# In[3]:


# search for a particular contact from the contact list
def searchContact(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
            print("%s does not exist" % name)
    return
searchContact("anil")
searchContact("adeeb")


# In[7]:


# new contacts given in the dictionary
# merge new contacts with the existing contacts list
def importContacts(newContacts):
    contacts.update(newContacts)
    print(len(newContacts.keys()),"contacts added successfully")
    return
newContacts = {'dinesh':89743652,'ajay':2348423456}
importContacts(newContacts)


# In[8]:


print(contacts)


# In[11]:


# delete a contact from the dictionary
def deleteContact(name):
    if name in contacts:
        del contacts[name]
        print(name,": is deleted from the list of contacts")
    else:
        print(name,"is not exists in the contacts")
    return
deleteContact("harsha")
deleteContact("anil")


# In[12]:


print(contacts)


# In[16]:


def updateContact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print(name,"updated with new phone number")
    else:
        print(name,"name is not exists in the contact")
    return
updateContact("dinesh",34512454)
        
    


# In[17]:


print(contacts)


# In[18]:


lst=[1,2,3,4]
print("%d %d %d %d"%(lst[0],lst[1],lst[2],lst[3]))


# In[23]:


lst=[1,2,3,4]
print("value at : {0} value at {1}".format(lst[0],lst[1]))
print("value at : {0} value at {1}".format(lst[2],lst[3]))


# # packages and modules
# ## packge ; collection of modules(pyhton file.py)
# ## sub package: its part of main package
# ## module: a single python file contain set of operations(functions)
# ### package->sub package->modules -> functions
# # standard lib ---- math

# In[24]:


from math import floor as f1
f1(123.453)
#the memory is allocated only for the floor function


# In[25]:


from math import factorial as fact
fact(5)


# In[26]:


import math
math.factorial(5)
# the memory is allocated for all the functions im math lib


# In[28]:


# generate the random numbers between two limits
import random
def generateRandomNumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end =" ")
    return
generateRandomNumbers(10,12,120)


# In[29]:


from math import ceil as c
c(2.5)


# In[30]:


from math import floor as f2
f2(4.5)


# In[32]:


from math import factorial as f
f(6)


# In[36]:


from math import fabs as a
a(-10)


# In[38]:


from math import  modf as m
m(6)


# In[39]:


from math import fmod as f
f(9,3)


# In[45]:


from math import log as sq
sq(4)


# In[46]:


from math import log10 as l
l(4)


# In[48]:


import random

print(random.choice([1,2,3,4]),end =" ")


# In[52]:


import random
print(random.randrange(20,40,2),end = " ")


# In[55]:


import random
print(random.seed(10),end = " ")


# In[56]:


import random
print(random.uniform(4,6),end = " ")


# In[57]:


import random
print(random.random())


# In[60]:



import random
li=[1,2,36,3]
for i in range(0,len(li)):
    print(li[i],end =" ")
    random.shuffle(li)


# In[61]:


import random
print(random.randint(1,5))


# In[65]:


import random
print(random.triangular(2,8,3))


# In[71]:


import random
print(random.getrandbits(4))


# In[ ]:




