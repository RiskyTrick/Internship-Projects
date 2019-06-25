#!/usr/bin/env python
# coding: utf-8

# In[1]:


R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  

M = [] 
print("Enter the entries row wise:") 
  
for i in range(R):         
    a =[] 
    for j in range(C):
        a.append(int(input("Enter the Data of Matrix1  :"))) 
    M.append(a)
    
M2 = []
print("The First Matrix is  :")
for i in range(R): 
    for j in range(C): 
        print(M[i][j], end = " ") 
    print() 
for i in range(R):
    b =[]
    for j in range(C):
        b.append(int(input("Enter the Data of Matrix 2  :"))) 
    M2.append(b)
        
M3 = []
print("The Second Matrix is  :")
for i in range(R):
    for j in range(C): 
        print(M2[i][j], end = " ") 
    print()
print("""
      """)    
for i in range(R): 
    for j in range(C):
        M3 =[[M[i][j]*M2[i][j] for j in range(len(M[0]))]for i in range(len(M2))]
print("The Output of Final Multiplied Matrix is  :")       
for i in range(R): 
    for j in range(C):
        print(M3[i][j], end = " ") 
    print()   

