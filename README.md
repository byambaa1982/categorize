# Categorize rows using description and key words

## Goal
One of my customers ask me to categorize data using describtions and certain key words. 
There are three different tables. `trips.txt calendar.txt and stop_times.txt`. The goal is that we needed to combine them and made some data engineering. 

### Calendar dates

  index  | Name    | Address     | Description
-------- | ------------- | -------- | --------------
0   | The Pushy Goat             | 509 N Lorraine | Our mission at The Pushy Goat is to care for t...
1   | HALO Day Spa	 	    | 1307 N Rose Hill Rd | Halo specializes in organic healing therapies....
2   | Salon Modern Classics            | 9511 Antioch Rd | Full service Salon for EVERYONE! We care about...

### Key words 

  yoga=['yoga', 'yin', 'vinyasa','yoga,', 'yin,', 'vinyasa,']
  spa=['spa','salon','spa,','salon,']
  cbd_services=['cbd services', 'cannabinoid','cbd services,', 'cannabinoid,']
  acupuncture=['acupuncture', 'chinese medicine','acupuncture,', 'chinese medicine,']
  fitness=['fitness', 'gym', 'crossfit', 'boxing','fitness,', 'gym,', 'crossfit,', 'boxing,','muscle,','muscle']
  biohacking=['cyrotherapy','infared','therapy','biohacking','cyrotherapy,','infared,','therapy,','biohacking,']
  beauty=['beauty','facial','hair','saloon','makeup','beauty,','facial,','hair,','saloon,','makeup,']
  massage_therapy=['massage','tissue','masages','massage,','tissue,','masages,']
  meditation=['meditation','meditations','meditation,','meditations,']

