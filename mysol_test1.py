#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Reference Taken from https://medium.com/@GalarnykMichael/python-basics-8-fizzbuzz-441e97c6c767
x_1 = 1
x_100 = 100
def fizzbuzz(x_1,x_100):
    for num in range(x_1, x_100):
        if num % 3 == 0:
            print("Fizz")
            continue
        elif num % 5 == 0:
            print("Buzz")
            continue
        elif num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
            continue
        else:
            print(num)
    return()
fizzbuzz(1,100)


# In[ ]:




