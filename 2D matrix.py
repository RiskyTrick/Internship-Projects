#!/usr/bin/env python
# coding: utf-8

# In[8]:


R= int(input("Enter no of rows"))
C = int(input("Enter no of colls"))
matrix = []
print("Enter the values row wise")
for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input("Enter a value:")))
    matrix.append(a)
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = "  ") 
    print()             
                 
                 
                 
        
                     
                 


# In[ ]:





# In[ ]:




