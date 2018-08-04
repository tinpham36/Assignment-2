
# coding: utf-8

# In[1]:


print('Question 1: The program finds all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 ')
for n in range(2000, 3201):
    if (n%7)==0 and (n%5)!=0:
        print (n, ',')


# In[2]:


print('Question 2: Python program to accept the first and last name of users and then getting them printed in the the reverse order with a space between first name and last name')
n=input('Enter your first name: ')
m=input('Enter your last name: ')
print('Your name is: ',m, ' ', n)



# In[8]:


print('Question 3: Calculate the volumn of the Sphere')
import math
x=int(input('Enter the diameter of the Sphere: '))
V=4/3*math.pi*x**3
print("The volumn of the sphere with the diameter", x, 'cm is: ', round(V, 3), 'cm3')


# In[ ]:




