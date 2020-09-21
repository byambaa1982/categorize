# from google.colab import drive
# drive.mount('/content/gdrive', force_remount=True)
# root_dir = "/content/gdrive/My Drive/categorize"
# base_dir = root_dir + 'byamba-v1/'


# import os
# os.chdir('/content/gdrive/My Drive/categorize')  #change dir
# !mkdir train  #create a directory named train/
# !mkdir test  #create a directory named test/
#!unzip -q varm.zip   #unzip data in StevenCSV

import pandas as pd
import numpy as np

df1=pd.read_excel('results (1).xlsx')


yoga=['yoga', 'yin', 'vinyasa','yoga,', 'yin,', 'vinyasa,']
spa=['spa','salon','spa,','salon,']
cbd_services=['cbd services', 'cannabinoid','cbd services,', 'cannabinoid,']
acupuncture=['acupuncture', 'chinese medicine','acupuncture,', 'chinese medicine,']
fitness=['fitness', 'gym', 'crossfit', 'boxing','fitness,', 'gym,', 'crossfit,', 'boxing,','muscle,','muscle']
biohacking=['cyrotherapy','infared','therapy','biohacking','cyrotherapy,','infared,','therapy,','biohacking,']
beauty=['beauty','facial','hair','saloon','makeup','beauty,','facial,','hair,','saloon,','makeup,']
massage_therapy=['massage','tissue','masages','massage,','tissue,','masages,']
meditation=['meditation','meditations','meditation,','meditations,']


df1['datatype']=df1.Description.map(lambda x : type(x))
# df=df1.loc[type(df1['Description']) != float]
# df['new']=df.Description.map(lambda x: x.split())
# df.new=df.new.map(lambda x: [i.lower() for i in x])


df=df1.loc[df1.datatype==str]

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


df['new']=df.Description.map(lambda x: x.split())
df['new']=df.new.map(lambda x: [i.lower() for i in x])
df['category']=df.new.map(lambda x: checkit(x))


df=df[['Name', 'Address', 'City', 'Phone', 'ZipCode', 'MainPhotoURL',
       'Description','category']]

df.fillna(value=pd.np.nan, inplace=True)
df['nan_col']=df.category.map(lambda x:type(x))
dfnone=df.loc[df.nan_col==float]

#----------- extract hashtag words----------------
# function to print all the hashtags in a text 
def extract_hashtags(text): 
      
    # initializing hashtag_list variable 
    hashtag_list = [] 
      
    # splitting the text into words 
    for word in text.split(): 
          
        # checking the first charcter of every word 
        if word[0] == '#': 
              
            # adding the word to the hashtag_list 
            hashtag_list.append(word) 
    return hashtag_list

df['hashtags']=df.tweets.map(lambda x:extract_hashtags(x))
