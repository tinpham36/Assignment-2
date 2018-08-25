
# coding: utf-8

# In[1]:


#Question 1: Write a program which accepts a sequence of comma-separated numbers from console and generate a list.
Input= input("Input a sequence of comma-separated numbers: ")
list = Input.split(",")
print("Generated List: ", list)


# In[16]:


#Question 2: Create the below pattern using nested for loop in Python.
n=5;
for i in range(0,n,1):
    for j in range(i):
        print ('*', end=' ')
    print(' ')

for i in range(n,0,-1):
    for j in range(i):
        print('*', end=' ')
    print(' ')


# In[4]:


#Question 3: Write a Python program to reverse a word after accepting the input from the user.
word = input('Input your words: ')
def reverse(word):
  plot = ""
  for i in word:
    plot = i + plot
  return plot
print('Reverse your word: ', reverse(word))


# In[17]:


#Question 4: 4. Write a Python Program to print the given string in the format specified in the sample output.
#WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN,
#SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens

a ='WE, THE PEOPLE OF INDIA,'
b ='having solemnly resolved to constitute India into a SOVEREIGN,'
c ='SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC'
d ='and to secure to all its citizens'

print(a,'\n', '\t',b, '!', '\n', c.center(60), '\n', d.center(62))
 


# In[ ]:




