#!/usr/bin/env python
# coding: utf-8

# In[7]:


def createfile(Risky):
    f=open(Risky,"w")
    for i in range(10):
        f.write("This is %d\n"%i)
    print("The File Has been Created Susccessfully")
    f.close()
    return
createfile("Risky.txt")


# In[4]:


open(Risky,"r")

