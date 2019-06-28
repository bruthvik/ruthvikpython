#!/usr/bin/env python
# coding: utf-8

# # FILE HANDILING IN PYTHON
# ## FILE  : DOCUMENT CONTAINING INFORMATION RESIDING ON THE THE PERMENENT      DEVICE STORAGES EX: PDF,TEXT,CSV FILES  ETC.
# ## FILE I/O:INPUT AND OUTPUT
#                    keyboard as input
#                    screen as output
#                    read/write
#                    open() -- open the file
#                    close() --- close the file
#                    
#                    
#                    
#                    open(filename,"mode of the file")
#                    
# ### "r"---it opens the file for reading
# ### "w"--- the mode open the file writing
#          ## if the file name is not present
#              it creates a new file and write some data in it
#              if the file already exsists virtual or local dir then the data will be over written

# In[ ]:





# In[62]:


#function to create the file and write some data
def createFile(filename):
    f = open(filename,"w")
    for i in range (10):
        f.write("Test /  %d line \n " % i)
    print("file is created successfully and Data is stored")
    f.close()
    return
createFile("file1.txt")


# In[63]:


#function for reding the file data
def readFile(filename):
    f=open(filename,"r")
    if f.mode == "r":
        x=f.read()
        print(x)
    f.close()
    return
readFile("file1.txt")


# In[77]:


ls


# In[99]:


def createFile(filename):
    f = open(filename,"w")
    for i in range (10):
        f.write("Test %d line \n" % i)
    print("file is created successfully and Data is stored")
    f.close()
    return
createFile("file1.txt")


# In[100]:


cat file1.txt


# In[114]:


names1=['amir','barry','chales','dao']
names2=names1
names3=names1[:]
print(names1,names2,names3)
names2[0]='alice'
names3[1]='bob'
print(id(names1),id(names2),id(names3))
sum=0
for l in (names1,names2,names3):
    if l[0]=='alice':
        sum=sum+1
    if l[1]=='bob':
        sum+=10
print(sum)


# In[19]:


def dataAnalysesWord(filename,word):  
    cnt=0
    f = open(filename,"w")
    if f.mode == "r":
        x=f.read()
        lst=x.split()
        cnt=lst.count(word)
    return cnt
print(dataAnalysesWord("file1.txt","read"))


# In[15]:


def countCharacters(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    return len(lst)
print(countCharacters("file1.txt"))


# In[85]:


cat file1.txt


# In[122]:


# function to count the upper case charaters from the given file
def countUpperCase(filename):
    cntUpper=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.isupper():
            cntUpper+=1
    cnt=lst.count(filename)
    return cntUpper
print(countUpperCase("file1.txt"))
    


# In[123]:


# function to count  the lines in the given file
def countLines(filename):
    cntLine=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split("\n")
    return lst
countLines("file1.txt")


# In[124]:


def countLines(filename):
    cntLine=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=x.split("\n")
    return len(lst)
countLines("file1.txt")


# # regular expressions
# ### pattern matching
# ### symbolic notation of a pattern
#  ### pattern represents the set of the values of a given pattern
#    # [0-9]---> Any digit
#    # [a-z]--->any lower case characters
#    # [A-Z]--->any upper case characters
#    # [2468]--->all multiples of 2 less than 9
#    # [0-9]{1} only single digit number
#    # cap : symbol is used for start of regular expression
#    # dollar: use to end the regular expression
#    # ^[0-9]{3}  regular expression will accept only three digits
#    # ^[a-z]{5}  it only accepts only 5 characters string that to lower case charcters
#    
#    # ^[a-zA-Z]{6}   a string can be upper or lower case characters and allows only 6 digits 
# # ^[a-zA-Z]{6,15} A STRING MIN OF 6 AND MAX OF 15 CHARACTERS
# # ^[6-9][0-9]{9}--- re for indian number

# # regular expressions for indian mobile number
# # validation for email.id username@gmail.com.extension
#  # 93484344757--first digit [6-9][0-9]
#  # 08748748455--first digit zero   second digit 0-9

# In[9]:


import re
def phoneNumberValidate(phone):
    pattern='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phoneNumberValidate("9443734743"))
print(phoneNumberValidate("09342323435"))
print(phoneNumberValidate("+919874374832"))


# In[10]:


import re
def validateRollNumber(number):
    number=str(number)
    pattern="^[1][5][2][U][1][A][0][1-9][0-6][0-9]$"
    if re.match(pattern,number):
        return True
    return False
print(validateRollNumber("152U1A0555"))


# In[22]:


import re
def validateEmailId(emailid):
    pattern='^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,emailid):
        return True
    return false
validateEmailId("bruthvik987@gmail.com")


# In[33]:


import re
def validPassword(password):
    pattern="^[a-zA-Z0-9@!#$]{6,15}$"
    if re.match(pattern,password):
        return True
    return False
validPassword("ruthvik@")


# ## ^[a].....[z]----> any string of lenght 5 start

# In[34]:


import re
def createFile(filename):
    f = open(filename,"w")
    for i in range (10):
        f.write("Test  %d line \n " % i)
    print("file is created successfully and Data is stored")
    f.close()
    return
createFile("file1.txt")


# In[36]:


def readFile(filename):
    f=open(filename,"r")
    if f.mode == "r":
        x=f.read()
        print(x)
    f.close()
    return
readFile("file1.txt")


# In[41]:


def countLowercase(filename):
    cntlower=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.islower():
            cntlower+=1
    cnt=lst.count(filename)
    return cntlower
print(countLowercase("file1.txt"))
        


# In[42]:


def countDigitcase(filename):
    cntdigit=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
        if i.isdigit():
            cntdigit+=1
    cnt=lst.count(filename)
    return cntlower
print(countdigitcase("file1.txt"))
        


# In[64]:


def countDigitcase(filename):
    c=0
    f=open(filename,"r")
    str=f.read()
    for i in str:
        if ord(i)>=33 and ord(i)<=47:
            c=c+1
    return c
print(countDigitcase("file1.txt"))


# In[60]:


file1.txt


# In[ ]:




