---
title: "Categorize rows using description and key words"
date: 2020-03-25 11:33:00 +0800
categories: [Blogging, Python]
tags: [pandas, lambda, dataengineering]
---


All code is in [my github](https://github.com/byambaa1982/categorize/blob/master/main.py)

## Goal
One of my customers ask me to categorize data using describtions and certain key words. 
There are three different tables. `trips.txt`, `calendar.txt` and `stop_times.txt`. The goal is that we needed to combine them and made some data engineering. 

### Calendar dates

  index  | Name    | Address     | Description
-------- | ------------- | -------- | --------------
0   | The Pushy Goat             | 509 N Lorraine | Our mission at The Pushy Goat is to care for t...
1   | HALO Day Spa          | 1307 N Rose Hill Rd | Halo specializes in organic healing therapies....
2   | Salon Modern Classics            | 9511 Antioch Rd | Full service Salon for EVERYONE! We care about...

### Key words 

```python
yoga=['yoga', 'yin', 'vinyasa','yoga,', 'yin,', 'vinyasa,']
spa=['spa','salon','spa,','salon,']
cbd_services=['cbd services', 'cannabinoid','cbd services,', 'cannabinoid,']
acupuncture=['acupuncture', 'chinese medicine','acupuncture,', 'chinese medicine,']
fitness=['fitness', 'gym', 'crossfit', 'boxing','fitness,', 'gym,', 'crossfit,', 'boxing,','muscle,','muscle']
biohacking=['cyrotherapy','infared','therapy','biohacking','cyrotherapy,','infared,','therapy,','biohacking,']
beauty=['beauty','facial','hair','saloon','makeup','beauty,','facial,','hair,','saloon,','makeup,']
massage_therapy=['massage','tissue','masages','massage,','tissue,','masages,']
meditation=['meditation','meditations','meditation,','meditations,']
```

### Goal

  index  | Name    | Address     | Description | Category
-------- | ------------- | -------- | -------------- | -------------------
0   | The Pushy Goat             | 509 N Lorraine | Our mission at The Pushy Goat is to care for t...| None
1   | HALO Day Spa          | 1307 N Rose Hill Rd | Halo specializes in organic healing therapies....   | Spa
2   | Salon Modern Classics            | 9511 Antioch Rd | Full service Salon for EVERYONE! We care about...| Beauty

In order acheive our goal, we use pandas. 

```python
import pandas as pd
import numpy as np
```
Read excel file and make it into Dataframe. 

```python
df1=pd.read_excel('results (1).xlsx')
```


```python
df=df1.loc[df1.datatype==str]
```

```python
def checkit(x):
  for i in x:
    if i in beauty:
      return 'Beauty'
    elif i in spa:
      return 'Spa'
    elif i in massage_therapy:
      return 'Massage Therapy'
    elif i in yoga:
      return 'Yoga'
    elif i in cbd_services:
      return 'CBD Service'
    elif i in acupuncture:
      return 'Acupuncture'
    elif i in biohacking:
      return 'Biohacking'
    elif i in meditation:
      return 'Meditation'
    else:
      'notype'
```

#### Lambda

```python
df['new']=df.Description.map(lambda x: x.split())
df['new']=df.new.map(lambda x: [i.lower() for i in x])
df['category']=df.new.map(lambda x: checkit(x))
```

```python
df=df[['Name', 'Address', 'City', 'Phone', 'ZipCode', 'MainPhotoURL',
           'Description','category']]
df.fillna(value=pd.np.nan, inplace=True)
df['nan_col']=df.category.map(lambda x:type(x))
dfnone=df.loc[df.nan_col==float]
```
    

If you have anything to ask, please contact me clicking following link?


You can hire me [here](https://www.fiverr.com/coderjs)

Thank you
