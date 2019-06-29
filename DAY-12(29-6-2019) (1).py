#!/usr/bin/env python
# coding: utf-8

# In[1]:


# creating a series of numbers by passing list of values
import pandas as pd
mport pa=pd.Series([1,2,3,5,8,9])
print(a)


# In[11]:


import pandas as pd
import numpy as np
a1 = pd.Series([1,2,3,4,np.nan,6])
print(a1)


# In[12]:


# create a list of dates with in particular range
dates=pd.date_range('20190601',periods=20)
print(dates)


# In[16]:


import pandas as pd
lst=pd.date_range('20190601',periods=9)
print(lst)


# In[23]:


a3=pd.DataFrame({'A':1.,
                'B':pd.Timestamp('20190601'),
                'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                'D':np.array([3]*4,dtype='int32'),
                'E':pd.Categorical(["test","train","test","train"]),
                'F':'foo'})
print(a3)


# In[31]:


# turtle is a python feature like a drawing board
# lines,squares,star,rect and etc
# turtle()--- it creates and returns a new turtle projects
# step1: make all the turtle package is imported
import turtle as tt
#turtle method creates and returns the new object
a1 = tt.Turtle()
# forward() method moves 100 pixels
tt.forward(100)
# we are done
tt.done()


# In[32]:


# drawing a square
import turtle as tt
a1=tt.Turtle()
a1.forward(150)
a1.right(90)


a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)

a1.forward(150)
a1.right(90)

tt.done()


# In[ ]:


# draw a square
# backward and left
import turtle as tt
c1=tt.Turtle()
c1.color("blue")
for i in range(50):
    c1.forward(50)
    c1.left(123)

c1.pencolor("red")
for i in range(50):
    c1.forward(50)
    c1.left(123)
tt.done()


# In[ ]:


# a colourful hexagonal
import turtle as tt
colors=['red','blue','orange','green','yellow','purple']
a1=tt.Turtle()


for x in range(360):
    a1.pencolor(colors[x%6])
    a1.width(x/100+1)
    a1.forward(x)
    a1.left(60)
tt.done()


# In[ ]:


import turtle as tt
a1=tt.Turtle()
colors=['red','green','yellow','orange','blue','purple']
dot_distance=10
width=10
height=15


a1.penup()


for x in range(height):
    a1.pencolor(colors[x%6])
    for i in range(width):
        a1.dot()
        a1.forward(dot_distance)
    a1.forward(dot_distance*width)
    a1.right(90)
    a1.forward(dot_distance)
    a1.left(90)
tt.done()


# In[8]:


# generating flowers
from turtle import *
import random
for n in range(50):
    penup()
    goto(random.randint(-400,400),random.randint(-400,400))
    pendown()
    
    red_amount=random.randint(0,30)/100.0
    blue_amount=random.randint(50,100)/100.0
    green_amount=random.randint(0,30)/100.0
    pencolor((red_amount,blue_amount,green_amount))
    
    
    circle_size=random.randint(10,40)
    pensize(random.randint(4,6))
    
    
    for i in range(6):
        circle(circle_size)
        left(10)


# In[16]:


# symbol generation using python turtle
from turtle import *
def main():
    colors=("red","orange","yellow","blue","seagreen","royalblue")
    reset()
    screen()
    up()
    goto(-300,-195)
    width(70)
    for  color in colors:
        color(pcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66)
        right(90)
   
    width(25)
    color("white")
    goto(0,-170)
    down()
    
    circle(170)
    left(90)
    forward(340)
    up()
    left(180)
    forward(170)
    right(45)
    down()
    forward(170)
    up()
    backward(170)
    left(90)
    down()
    forward(170)
    up()
    goto(0,300)

if __name__ == "__main__":
    main()
    mainloop()
    
    


# In[ ]:




