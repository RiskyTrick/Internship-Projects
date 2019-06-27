#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def readfile(Risky):
    f=open(Risky,"r")
    if f.mode=="r":
        x=f.read()
        print(x)
    f.close()
    return
readfile("Risky.txt")

