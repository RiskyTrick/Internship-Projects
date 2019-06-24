#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###### i=0
listn =[]
n=int(input("Enter the max_size of the list"))
for i in range(0,n):
    element = int(input("Enter an Element to be Appended into he List:"))
    listn.append(element)
key=int(input("enter a key:"))
for i in range(n):
    if(key==listn[i]):
        print("Given Key is found at:",i)
        

