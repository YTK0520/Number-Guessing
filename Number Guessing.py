#!/usr/bin/env python
# coding: utf-8

# In[49]:


import random

print("Guess the NUMBER from 1 to 100!")
rand_num=random.randint(1,100)
if rand_num%2==0:
    print("Hint:The answer is even.")
else:
    print("Hint:The answer is odd.")
for i in range(1,101):
    ans=int(input("Please input a number between 1 to 100 :"))
    if ans>rand_num:
        print("The inputed number is smaller than the answer.\nPlease try again.")
    elif ans<rand_num:
        print("The inputed number is greater than the answer.\nPlease try again.")
    else:
        print("Congratulations!\nThe inputed number is correct!")
        break

