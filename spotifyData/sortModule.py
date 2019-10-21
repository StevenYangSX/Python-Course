# test = [['0.465', "Don't Let Me Down - Zomboy Remix", 'The Chainsmokers'], 
# ['0.68', 'Faded - Slushii Remix', 'Alan Walker'], 
# ['0.619', "Can't Get Enough - Pegboard Nerds Remix", 'Tommie Sunshine'], 
# ['0.52', 'Light - Loosid Remix', 'San Holo'], 
# ['0.484', 'Something Just Like This - ARMNHMR Remix', 'The Chainsmokers'],
#  ['0.583', 'Without U', 'Steve Aoki'], ['0.562', 'Hold Up', 'Borgeous'],
#   ['0.595', 'Phone Down - Dodge & Fuski Remix', 'Lost Kings'], 
#   ['0.526', 'Spoon Me - Slushii Remix', 'Elliphant'], 
#   ['0.501', 'Scared To Be Lonely (Conro Remix)', 'Martin Garrix'],
#    ['0.639', 'Let It Go - Scott Melker & Mister Gray Remix', 'NERVO'], 
#    ['0.646', 'Call On Me - EDWYNN X TIKAL, Spirix Remix', 'Starley'], 
#    ['0.595', 'Aamon', 'Kuuro'], ['0.624', 'Hey Baby - Steve Aoki Remix', 'Dimitri Vegas & Like Mike'], 
#    ['0.528', 'Brightside - Borgeous Remix', 'Icona Pop'], 
#    ['0.584', 'Like A Bitch - Kill The Noise Remix', 'Kill The Noise']]
def binarySearch(data, target):
  """ Search data for target.
      Input: data must be sorted, target (element to find)   
      Output (return): Boolean - whether target is present or not
  """
  first = 0    # index of 1st element
  last = len(data) - 1  # index of last element
  found = False

  # While target not yet found and we are still within data
  while (not found) and first <= last: 
    midpoint = (first + last) // 2  # divide and round
    if data[midpoint] == target:
      found = True 
    else:
      if target < data[midpoint]:  # target on left of midpoint
        last = midpoint - 1
      else:   # target on right of midpoint
        first = midpoint + 1
  
  return found

def binarySearch2D(data, query):
  """ Search data tuple for query (within 0.1 of query).
      Input: data must be sorted, target (element to find)   
      Output (return): Boolean - whether target is present or not
  """
  # Initialize first/last indices
  first = 0
  last = len(data) - 1

  # Loop as long as our search space is not null
  while first <= last:

    # Check midpoint
    midpoint = (first+last)//2  

    # If the midpoint is our element, return ...
    if abs(data[midpoint][0] - query) < 0.1:
      return data[midpoint]
      # return midpoint - This would return the index
    
    # If our query is greater than the midpoint value
    elif query > data[midpoint][0]:
      # Cut out left hand side of search space
      first = midpoint + 1
    
    # Query is less than midpoint value
    else:
      # Cut out right hand side of search space
      last = midpoint - 1

  # Haven't found query
  return None

def bubbleSort(arr):
    return 1


'''bubble sort by index'''
def bubbleSort2D(arr, targetIndex):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if(arr[j][targetIndex] > arr[j+1][targetIndex]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


