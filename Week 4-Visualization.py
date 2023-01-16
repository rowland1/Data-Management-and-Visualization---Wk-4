#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt


# In[3]:


data = pandas.read_csv('nesarc_pds.csv', low_memory=False)


# In[4]:


print (len(data)) 


# In[5]:


print (len(data.columns))


# In[6]:


# Convert data types from 'Object' to 'Float'
data["S2AQ19"] = data["S2AQ19"].apply(pandas.to_numeric,errors="coerce")
data["S4AQ1"] = data["S4AQ1"].apply(pandas.to_numeric,errors="coerce")
data["S5Q1"] = data["S5Q1"].apply(pandas.to_numeric,errors="coerce")
data["S5Q3"] = data["S5Q3"].apply(pandas.to_numeric,errors="coerce")


# In[7]:


# Determine data types for variables of interest post change to 'Float'
data['S2AQ19'].dtype
data['S4AQ1'].dtype
data['S5Q1'].dtype
data['S5Q3'].dtype


# In[8]:


#Adding more descriptive titles for key variables 
print('Counts for S2AQ19: AGE AT START OF PERIOD OF HEAVIEST DRINKING')
c3 = data['S2AQ19'].value_counts(sort = False, normalize=False).sort_index()
print (c3)
#
print('Normalized counts for S2AQ19: AGE AT START OF PERIOD OF HEAVIEST DRINKING')
p3 = data['S2AQ19'].value_counts(sort = False, normalize=True).sort_index()
print (p3)
#
print('Counts for S4AQ1: EVER HAD 2-WEEK PERIOD WHEN FELT SAD, BLUE, DEPRESSED, OR DOWN MOST OF TIME')
c6 = data['S4AQ1'].value_counts(sort = False, normalize=False).sort_index()
print (c6)
#
print('Normalized counts for S4AQ1: EVER HAD 2-WEEK PERIOD WHEN FELT SAD, BLUE, DEPRESSED, OR DOWN MOST OF TIME')
p6 = data['S4AQ1'].value_counts(sort = False, normalize=True).sort_index()
print (p6)
#
print('Counts for S5Q1: HAD 1+ WEEK PERIOD OF EXCITEMENT/ELATION THAT SEEMED NOT NORMAL SELF')
c9 = data['S5Q1'].value_counts(sort = False, normalize=False).sort_index()
print (c9)
#
print('Normalized counts for S5Q1: HAD 1+ WEEK PERIOD OF EXCITEMENT/ELATION THAT SEEMED NOT NORMAL SELF')
p9 = data['S5Q1'].value_counts(sort = False, normalize=True).sort_index()
print (p9)
#
print('Counts for S5Q3 : D 1+ WEEK PERIOD IRRITABLE/EASILY ANNOYED THAT CAUSED YOU TO SHOUT/BREAK THINGS/START FIGHTS OR ARGUMENTS')
c10 = data['S5Q3'].value_counts(sort = False, normalize=False).sort_index()
print (c10)
#
print('Normalized counts for S5Q3 : D 1+ WEEK PERIOD IRRITABLE/EASILY ANNOYED THAT CAUSED YOU TO SHOUT/BREAK THINGS/START FIGHTS OR ARGUMENTS')
p10 = data['S5Q3'].value_counts(sort = False, normalize=True).sort_index()
print (p10)


# In[9]:


# Reduce data set to drinkers <21yrs old
sub1=data[(data['S2AQ19']<=21)]
print (len(sub1))


# In[10]:


# Convert data types from 'Object' to 'Float'
sub1["S2AQ19"] = sub1["S2AQ19"].apply(pandas.to_numeric,errors="coerce")
sub1["S4AQ1"] = sub1["S4AQ1"].apply(pandas.to_numeric,errors="coerce")
sub1["S4AQ6A"] = sub1["S4AQ6A"].apply(pandas.to_numeric, errors="coerce")
sub1["S5Q1"] = sub1["S5Q1"].apply(pandas.to_numeric,errors="coerce")
sub1["S5Q3"] = sub1["S5Q3"].apply(pandas.to_numeric,errors="coerce")
sub1["S5Q8B"] = sub1["S5Q8B"].apply(pandas.to_numeric,errors="coerce")


# In[11]:


print('Frequency Table for S2AQ19: AGE AT START OF PERIOD OF HEAVIEST DRINKING [5-21 Age; 99. Unknown; BL. NA, lifetime abstainer]')
c7 = sub1['S2AQ19'].value_counts(sort = False, normalize=False).sort_index()
print (c7)


# In[12]:


print('Frequency Table for Percentage of Drinkers <21yrs old by age')
pt2 = sub1.groupby('S2AQ19').size() * 100 / len(sub1)
print(pt2)
#
print()


# In[13]:


# Data Management Action 1: Set aside missing data
sub1['S4AQ1']=sub1['S4AQ1'].replace(9,numpy.nan)
sub1['S5Q1']=sub1['S5Q1'].replace(9,numpy.nan)
sub1['S5Q3']=sub1['S5Q3'].replace(9,numpy.nan)


# In[14]:


# Data Management Action 1: Frequency tables to confirm '9' missing values have been coded out
print('Counts for S4AQ1: EVER HAD 2-WEEK PERIOD WHEN FELT SAD, BLUE, DEPRESSED, OR DOWN MOST OF TIME')
c6 = sub1['S4AQ1'].value_counts(sort = False, normalize=False).sort_index()
print (c6)
#
print('Normalized counts for S4AQ1: EVER HAD 2-WEEK PERIOD WHEN FELT SAD, BLUE, DEPRESSED, OR DOWN MOST OF TIME')
p6 = sub1['S4AQ1'].value_counts(sort = False, normalize=True).sort_index()
print (p6)
#
print('Counts for S5Q1: HAD 1+ WEEK PERIOD OF EXCITEMENT/ELATION THAT SEEMED NOT NORMAL SELF')
c9 = sub1['S5Q1'].value_counts(sort = False, normalize=False).sort_index()
print (c9)
#
print('Normalized counts for S5Q1: HAD 1+ WEEK PERIOD OF EXCITEMENT/ELATION THAT SEEMED NOT NORMAL SELF')
p9 = sub1['S5Q1'].value_counts(sort = False, normalize=True).sort_index()
print (p9)
#
print('Counts for S5Q3 : D 1+ WEEK PERIOD IRRITABLE/EASILY ANNOYED THAT CAUSED YOU TO SHOUT/BREAK THINGS/START FIGHTS OR ARGUMENTS')
c10 = sub1['S5Q3'].value_counts(sort = False, normalize=False).sort_index()
print (c10)
#
print('Normalized counts for S5Q3 : D 1+ WEEK PERIOD IRRITABLE/EASILY ANNOYED THAT CAUSED YOU TO SHOUT/BREAK THINGS/START FIGHTS OR ARGUMENTS')
p10 = sub1['S5Q3'].value_counts(sort = False, normalize=True).sort_index()
print (p10)


# In[15]:


# Data Management Action 2: Create secondary varialbe 'MentalHealthScore'
sub1['MentalHealthScore']=sub1['S4AQ1']+sub1['S5Q1']+sub1['S5Q3']


# In[16]:


# Data Management Action 2: Frequency table to confirm seconday variable 'MentalHealthScore'
print('Top 25 Rows Confirming MentalHealthScore Calculation')
sub2=sub1[['IDNUM', 'S4AQ1','S5Q1', 'S5Q3', 'MentalHealthScore']]
sub2.head(25)


# In[17]:


# Data Management Action 3: Grouping values within individual variables to create MentalHealthCondition based off MentalHealthScore
def MentalHealthCondition (row):
    if row['MentalHealthScore'] == 3:
        return 'Yes'
    if row['MentalHealthScore'] > 3:
        return 'No'
    
sub1['MentalHealthCondition'] = sub1.apply (lambda row: MentalHealthCondition (row), axis=1)

print('Top 25 Rows Confirming MentalHealthCondition Calculation')
sub2=sub1[['IDNUM', 'S2AQ19','S4AQ1','S5Q1', 'S5Q3', 'MentalHealthScore', 'MentalHealthCondition']]
sub2.head(25)


# In[18]:


# Data Management Action 3: Frequency table for grouping values within individual variables to create MentalHealthCondition based off MentalHealthScore
print('Counts for MentalHealthCondition; 1 = BiPolar; 2 = Not BiPolar')
c11 = sub2['MentalHealthCondition'].value_counts(sort = False, normalize=False).sort_index()
print (c11)
#
print('Percentages for for MentalHealthCondition; 1 = BiPolar; 2 = Not BiPolar')
p11 = sub2['MentalHealthCondition'].value_counts(sort = False, normalize=True).sort_index()
print (p11)
#


# In[19]:


# After applying the various data managment actions and creating frequency tables, the number of people who experience BiPolar disorder is 423 of 14162,
# or ~3%. This count excludes those with missing data. This shows that BiPolar disorder is experienced by a small portion of the population.
# However, the number of observations for responsdents with BiPolar disorder should be enough to show a correlation with drinking at a young age.
# Further analysis can be done on individual aspects of BiPolar disorder that occur in isolation, including depression, anger and elevation


# In[20]:


# Counts for single conditions and MentalHealthCondition 
print('Percentages for depression only: 1=Yes, 2=No')
p11 = sub2['S4AQ1'].value_counts(sort = False, normalize=True).sort_index()
print (p11)
#
print('Percentages for elation only: 1=Yes, 2=No')
p12 = sub2['S5Q1'].value_counts(sort = False, normalize=True).sort_index()
print (p12)
#
print('Percentages for irritable only: 1=Yes, 2=No')
p13 = sub2['S5Q3'].value_counts(sort = False, normalize=True).sort_index()
print (p13)
#
print('Percentages for for MentalHealthCondition; 1 = BiPolar; 2 = Not BiPolar')
p14 = sub2['MentalHealthCondition'].value_counts(sort = False, normalize=True).sort_index()
print (p14)
#


# In[21]:


# Univariant bar graph for categorical variable S2AQ19
# First change format from numerical to categorical
sub2["S2AQ19"] = sub2["S2AQ19"].astype('category')
seaborn.countplot(x="S2AQ19", data=sub1)
plt.xlabel('AGE AT START OF PERIOD OF HEAVIEST DRINKING')
plt.title('S2AQ19: AGE AT START OF PERIOD OF HEAVIEST DRINKING in the NESARC Study')


# In[ ]:


# The 'S2AQ19: AGE AT START OF PERIOD OF HEAVIEST DRINKING' graph reveals a bimodal distribution with peaks for young adults 
# who startd their heaviest drinking at 18 and 21yrs of age' Since this analysis is a categorical to categorical, we'll also
# look the relationship of drinking with only depression, elation or irritability, along with bi-polar disorder


# In[22]:


# Univariant bar graph for categorical variable S2AQ19
# First change format from numerical to categorical
sub2["MentalHealthCondition"] = sub2["MentalHealthCondition"].astype('category')
seaborn.countplot(x="MentalHealthCondition", data=sub2)
plt.xlabel('MentalHealthCondition')
plt.title('MentalHealthCondition')


# In[41]:


# Reduce data set to bi-polar and separate
sub3=sub1[(sub1['MentalHealthCondition']=='Yes')]
sub4=sub1[(sub1['MentalHealthCondition']=='No')]
print (len(sub3))
print (len(sub4))


# In[ ]:


#The distribution of 'No' is much higher at 423 than 'Yes' at 13472


# In[23]:


#confirm variables are categorical
sub2['S2AQ19'] = sub2['S2AQ19'].astype('category')
sub2['MentalHealthCondition'] = sub2['MentalHealthCondition'].astype('category')
#seaborn.barplot(x='MentalHealthCondition', y='S2AQ19', data=sub2)
sub2['S2AQ19'].dtype
sub2['MentalHealthCondition'].dtype


# In[24]:


#Change S2AQ19 back to 'float' to enable comparison of variables
sub2=sub2.explode('S2AQ19')
sub2['S2AQ19'] = sub2['S2AQ19'].astype('float')
seaborn.barplot(x='MentalHealthCondition', y='S2AQ19', data=sub2)
plt.ylabel('Age')
plt.title('Age of Early Drinking by Bi-Polar Indicator')


# In[ ]:


#The barplot illustraed a slight differences between the age of heavist drinking and bipolar indicator of 'yes' and 'no'; 
#Other graphs will be necessary to illustrate any differences


# In[25]:


seaborn.boxplot(x='MentalHealthCondition', y='S2AQ19', data=sub2) 


# In[ ]:


#The boxplot illustrates a difference between the age of heavist drinking and bipolar indicator of 'yes' and 'no';
#the average age of heaviest drinking is ~18yrs old for bi-polar while it is ~19yrs old for non bi-polar; 
#the boxplot also shows that the upper and lower quartiles for 'Yes' are below 'No'


# In[40]:


print('mean')
meanYes = sub3['S2AQ19'].mean()
meanNo = sub4['S2AQ19'].mean()
print (meanYes)
print (meanNo)


# In[ ]:


#A comparison of means confirms the 'No' averge age is approximiatly .5 yrs older than 'Yes'


# In[26]:


seaborn.violinplot(x='MentalHealthCondition', y='S2AQ19', data=sub2) 


# In[ ]:


#The violin chart shows that 'Yes' is denser in general for younger ages, reducing the average age below that of 'No'


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




