#!/usr/bin/env python
# coding: utf-8

# In[1]:


modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr',
'StELLa']


# In[2]:


l1=enumerate(modern_family)
l1=list(l1)
print(l1)
len(l1)


# In[3]:


indices=[]
characters=[]
for k,v in enumerate(modern_family):
    indices.append(k)
    characters.append(v)
print(indices)
print(characters)    


# In[4]:


print(characters)
for i in range(len(characters)):
    characters[i] = characters[i].lower()
    characters[i] = characters[i].replace('_','-')
print(characters)


# In[5]:


print(characters)
l=lambda y:len(y)
print(l(characters))


# In[6]:


temp=[]
m=map(lambda y:len(y),characters)
temp=list(m)
print(m)
print(temp)


# In[7]:


n=zip(indices,temp)
x=list(n)
print(x)


# In[8]:


x[1][1]


# In[9]:


indices=[sum(i) for i in x]
print(indices)


# In[10]:


indices.sort(reverse=True)
print(indices)


# In[11]:


print(indices)
print(characters)
p=zip(indices,characters)
z=list(p)
Phew_finally=dict(z)
print(Phew_finally)


# In[12]:


'''Observe the given list carefully and using only list slicing, create a list named 'next_game'
which contains all 'green_light' elements from the given list. Make sure you don’t accidentally
include the others!'''

creepy_doll = ['red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light', 'you_got_shot',
'you_got_shot', 'green_light', 'you_ got_shot', 'red_light', 'green_light', 'red_light', 'you_got_shot',
'green_light','red_light', 'red_light', 'green_light', 'you_got_shot','red_light', 'you_got_shot']


# In[13]:


creepy_doll.sort()
print(creepy_doll)
len(creepy_doll)


# In[14]:


index = creepy_doll.index('green_light')
index


# In[15]:


creepy_doll.sort(reverse=True)
print(creepy_doll)


# In[16]:


index = creepy_doll.index('green_light')
index


# In[17]:


next_game=creepy_doll[0:6]
print(next_game)
len(next_game)


# ###  task 1.3 
# 

# In[25]:


class Titandex:
    #ws=0
    def __init__(s):
        s.n1=input("enter name of the titan")
        s.h=input("enter height of the titan")
        s.st=input("enter strength of the titan")
        s.ws=0
    def __TitanvsScout__(s):
        s.n=input("enter name of the scout")
        s.ss=input("enter strength of the scout")
        if(s.st>s.ss):
            print(" wins",s.n1)
            s.ws+=1
        elif(s.st<s.ss):
            print(" wins",s.n)
            s.ws=0
        else:
            print("match draw")
            s.ws=0
    def __Titanvstitan__(s):
        s.n2=input("enter name of the titan2")
        if(s.n1==s.n2):
            s.n2=input("enter another titan")
        else:
            s.st2=input("enter strength of the titan2")
            if(s.st>s.st2):
                print(" wins",s.n1)
                s.ws+=1
            elif(s.st<s.st2):
                print(" wins",s.n2)
                s.ws=0
                
            else:
                print("match draw")
                s.ws=0
                    
                   
                    
                    
    def __display__(s):
        print("wninning streak of titan1 is ",s.ws)
        return(s.ws)

obj=Titandex()
#obj.__init__()
obj. __TitanvsScout__()
obj.__Titanvstitan__()
obj.__display__()
                   
               
           
        


# In[24]:


s='sam'
print(' name ',s)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




