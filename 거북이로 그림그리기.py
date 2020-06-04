#!/usr/bin/env python
# coding: utf-8

# ## 거북이로 그림그리기

# In[ ]:


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# In[ ]:


import turtle as t
t.color('red', 'yellow')
t.shape('turtle')
t.fd(200)
t.left(90)
t.fd(200)
t.left(90)
t.fd(200)
t.left(90)
t.fd(200)
t.left(90)
t.exitonclick()


# In[ ]:


import turtle as t
t.color('red', 'yellow')
t.begin_fill()
t.shape('turtle')
for i in range(3):
    t.fd(200)
    t.left(120)
t.end_fill()
t.exitonclick()


# In[2]:


import turtle as t
t.color('red', 'yellow')
t.begin_fill()
t.shape('turtle')
angle = int(input('몇각형? '))
for i in range(angle):
    t.fd(200)
    t.left(360/angle)
t.end_fill()
t.exitonclick()


# In[1]:


import turtle as t
t.shape('turtle')
n=100
t.bgcolor("black")
t.color("red")
t.speed(0)
for x in range(n):
    t.circle(40)
    t.left(360/n)
    t.fd(5)

