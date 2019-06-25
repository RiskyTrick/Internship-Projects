#!/usr/bin/env python
# coding: utf-8

# In[10]:


n=int(input("enter no.of values"))
a = []
b = []
for i in range(n):           
    element=(int(input("enter The Unsorted Data:"))) 
    a.append(element)
for i in range(n-1):
    for j in range(n-i-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("The Sorted Output is :")
for i in range(n):
    print(a[i],end=" ")


# In[ ]:





# In[ ]:




