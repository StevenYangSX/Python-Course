#read in the csv file
import csv
import sortModule

with open('spotify.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

#print(your_list[0])

#get data we need. Data cleaning

theData = []

for song in your_list:
    artist = song[len(song)-1]
    title = song[len(song)-2]
    danceability = song[2]
    
    element = [danceability, title, artist]
    
    theData.append(element)
print(theData)

#TODO: using data got above , do analysis and filters.
#TODO: write sort and search modules to support some function

sortedData = sortModule.bubbleSort2D(theData,0)

#for each in sortedData:
  #print("{:<10}{:<20}".format(each[0], each[1]))


sortedDataByLetter = sortModule.bubbleSort2D(theData,1)

for each in sortedDataByLetter:
  print("{:<10}{:<20}".format(each[0], each[2]))

#TODO: sort by multiple data
#Need to change sorting function