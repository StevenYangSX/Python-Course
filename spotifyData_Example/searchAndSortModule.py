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


def selectionSort(data):
  """ 
    Sort in ascending order
    Input: unsorted list of numbers
    Output (return): sorted list of numbers
  """
  for i in range(len(data)):
    # Initialize some variables
    smallestNumber = data[i]   
    smallestNumberIndex = i

    # Loop through all remaining elements to find smallest
    for j in range(i+1, len(data)):
      if data[j] < smallestNumber:
        smallestNumber = data[j]        
        smallestNumberIndex = j

    # Once we have smallest, swap the smallest element with the first element of our outer list
    data[smallestNumberIndex], data[i] = data[i], data[smallestNumberIndex]

  return data

def selectionSort2D(data):
  """ 
    Sort in ascending order, by element at index 0.
    Input: unsorted list of numbers
    Output (return): sorted list of numbers
  """

  # Outer loop
  for i in range(len(data)):

  # Inner loop to find out if there's a smaller element in rest of list

    # Initialize min score and index
    minScore = data[i][0]
    minIndex = i

    # Look through sublist to see if there's something smaller
    for j in range(i+1, len(data)):
      if data[j][0] < minScore:
        minScore = data[j][0]
        minIndex = j
    
    # Swap in the minimum value found
    data[minIndex], data[i] = data[i], data[minIndex]
  
  return data
