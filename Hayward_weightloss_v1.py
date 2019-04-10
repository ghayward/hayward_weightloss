#!/usr/bin/env python
# coding: utf-8

# In[1]:


#let's use pandas
import pandas as pd


# In[2]:


#I used to be very over-weight, and after I lost about 90lbs,
#I started to very carefully monitor my weight on an iPhone app. 
#The app lets me export the weight as a CSV file.
weight = pd.read_csv("WeightDrop-Export-2019-04-10.csv")


# In[3]:


#Let's get a sense of the data.
print(weight.head())


# In[4]:


#What time perioid does the data span?
import datetime
format_str = '%m/%d/%y' #Setting up the format
#Key in this part is that the weight data is in chronological order. 
first_date = datetime.datetime.strptime(weight.date.iloc[0], format_str)
last_date = datetime.datetime.strptime(weight.date.iloc[-1], format_str)
#Let's make the formatting look nice.
print('{:%Y-%m-%d}'.format(first_date))
print('{:%Y-%m-%d}'.format(last_date))
#Let's subtract only on the dates (since the hours, mins, secs, microsecs, will all be 0)
print(str((last_date - first_date).days)+' days')


# In[5]:


#How much has my weight fluctuated?
print(str(round(weight.weight.max() - weight.weight.min()))+' lbs')


# In[6]:


#What's my longest period of consecutive weight gain?
#We'll use this to store values on during the for loop.
longest_set = 0
current_set = 0
longest_streak_end_date = 0

#Since we have a next-element iteration, we need to run the 'i's' for 1 less than the length\
#of the data frame or else we'll reach the end and look for a '+1' element where none will\
#exist because we are at the end of the list, and the script will blow up.
for i in range(len(weight)-1):
    
    #this asks, if the next element is more than the prior one (so a weight gain)\
    #if it is we add 1 to the current set...and we'll keep adding 1 to the current set\
    #until we see that the streak has ended.
    if weight.weight[i] < weight.weight[i + 1]:
        current_set += 1
   
    #next, we say that if the above is NOT the case, we sort of re-set our script. If we're\
    #here, we know the streak has ended. So we want to store the current_set value as the\
    #longest_set (which we do with the max function), and then we re-set the current set to 0.
    elif weight.weight[i] >= weight.weight[i + 1]:
        longest_set = max(longest_set, current_set)
        current_set = 0 
     
    #I think we can't use an else here because we don't want to do it in all times when a\
    #streak is broken. Basically, if the current streak is at any time greater than the\
    #longest streak, we then want to make sure we note that date, and this will do that.
    if current_set > longest_set:
        longest_streak_end_date = weight.date[i + 1]
        
    #I did not use an 'else:' here because I wanted the logic to be like a fork, more and\
    #then a return, then a regular tree. In other words. A or B then we do C. I did not want\
    #A then B then C, and I thought that an else would give us that later kind of thing. For\
    #me the way I looked at the else was if A did not happen, then else would always happen.\
    #But really what I wanted was that if A did not happen or did happen, else would sometimes\
    #happen. So, here I actually wanted another if. 
    
print(str(max(longest_set, current_set))+' days consecutive weight gain ending on '      +str(longest_streak_end_date))
    


# In[7]:


#What's my longest period of consecutive weight loss?
longest_set = 0
current_set = 0
longest_streak_end_date = 0

for i in range(len(weight)-1):
    
    if weight.weight[i] > weight.weight[i + 1]:
        current_set += 1
   
    elif weight.weight[i] <= weight.weight[i + 1]:
        longest_set = max(longest_set, current_set)
        current_set = 0 
        
    if current_set > longest_set:
        longest_streak_end_date = weight.date[i + 1]
    
print(str(max(longest_set, current_set))+' days consecutive weight loss ending on '      +str(longest_streak_end_date))
    

    

