
# coding: utf-8

# ** Problem 2 **

# In[ ]:




# In[14]:

n = int(input("Enter the number of integers"))
print("Number of integers n is:",n)

if(n in range(1,10**4)):
    list_of_integers = []
    for i in range(n):
        x = int(input("Enter the integer: "))
        list_of_integers.append(x)
    
    
    #list_of_integers = [int(i) for i in input("Enter the integers with a space: ").split()]
    print("List of integers:",list_of_integers)

    sorted_list = sorted(list_of_integers)
    #print(sorted_list)
    count = 0 
    for i in sorted_list:
        for j in sorted_list:
            if(i<j):
                z = i+j
                if(z in sorted_list):
                    count = count + 1
                    #print(z)
    print("----------------")
    print(count)
else:
    print("Range out of bounds")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



