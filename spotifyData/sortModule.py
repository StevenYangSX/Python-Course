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
def binarySearch(arr):
   return 1 

def binarySearch2D(arr):
    return 1

def bubbleSort(arr):
    return 1


'''bubble sort by index'''
def bubbleSort2D(arr, targetIndex):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if(arr[j][targetIndex] > arr[j+1][targetIndex]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


