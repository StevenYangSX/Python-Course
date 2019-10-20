# Spotify Data Search
import searchAndSortModule

# Main part of program

# Open and read from the file
file = open("spotify.csv")
file.readline() # Remove non-data header
#print(file)
# Create a list of tuples or a list of lists
# containing the data
theData = []
#print(file)
for line in file:
  # strip() removes all the leading and trailing spaces from a string
  # split() returns a list of strings after breaking the given string by the specified separator, here ",". 
  # print()
  # items = line.strip()
  # print("items: {} which is a {}".format(items, type(items)))
  # items = items.split(",")
  # print("items: {} which is a {}".format(items, type(items)))
  items = line.strip().split(",")
  artist = str(items[len(items)-1]) # Get last item
  songtitle = str(items[len(items)-2]) # Get the one before last 
  danceability = float(items[2])

  if artist == "Rain Man" : #"David Bowie":
    theData.append( (danceability, songtitle, artist) )

# How many songs of this artist are there:

# Sort those hits
sortedData = searchAndSortModule.selectionSort2D(theData)
# Print result of sort
print("\nsortedData : {}". format(sortedData))

# Print result of search


for each in sortedData:
  print("{:<10}{:<20}".format(each[0], each[1]))


#search some song exist
searchDanceability = 0.8
searchResult = searchAndSortModule.binarySearch2D(sortedData, searchDanceability)
print(searchResult)
