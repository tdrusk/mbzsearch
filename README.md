# mbzsearch
This is a little tool I wrote in Python to query musicbrainz and show exact matches for songs within a certain year range. Once it finishes you will get a html file in the folder mbzsearch.py is in. In this file you can see the results and quickly search youtube for results. It outputs mbz_SONGNAME.html. 

* change songtitle to the song you want
* minyear / maxyear sets limits on the search, but always shows unknown years
* If you set either year to None it will remove that limit.
* It only does exact matches

# How to Use in Windows (for beginners)
This should work with any operating system but these instructions will need to be tweaked.

* Install Python either from the Windows Store or here: https://www.python.org/ 
* Make a new folder on your desktop. 
* Open python IDLE
* File - New File
* Copy and paste the code from mbz.py into the new file and save it
* Click Run - Run Module
* It will take a while to run and once it is finished you should see a new >>> line in IDLE (as it is ready to accept more input)
* Once it completes, go to the folder on your desktop and double-click the html file to review the output.