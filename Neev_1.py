
# coding: utf-8

# ** Problem 1 **

# In[ ]:




# In[128]:

n = int(input("Enter the number of integers "))
print("Number of integers n is:",n)

if(n in range(0,501)):
    list_of_integers = []
    for i in range(n):
        x = int(input("Enter the integer: "))
        list_of_integers.append(x)
    sum = 0
    prob1(list_of_integers,sum)
    
else:
    print("Range out of bounds")


# In[ ]:




# In[ ]:




# In[126]:

def prob1(list,sum):
    if(len(list)==0):
        print(sum)
        return(sum)
    if(len(list)>2):     
        list1=list[1:len(list)-1]
        minValue = min(list1)
        pos = list.index(minValue)
        x = list[pos]*list[pos-1]*list[pos+1]
        sum = sum + x
        list.remove(minValue)
        prob1(list,sum)
    else:
        product = 1
        maxValue = max(list)
        for x in list:
            product *= x
        sum = sum + product + maxValue
        print(sum)
        return sum


# In[ ]:



