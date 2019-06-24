#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input("enter n value"))
array = []  
for i in range(n):           
    element=(int(input("enter an element"))) 
    array.append(element)
for i in range(n):  
        print(array[i], end = " ") 
key=int(input("enter key value"))
low=0
high=n-1
mid=(low+high)//2
while(low<=high):
    if(key<array[mid]):
        high=mid-1
    elif(key==array[mid]):
        print("key is found at:",mid)
        break
    elif(key>array[mid]):
        low=mid+1
        mid=(low+high)//2
        

