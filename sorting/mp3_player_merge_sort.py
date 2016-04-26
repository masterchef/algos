input = 10
#input = 16
#input = 32
input = 10000
list = range(1, input+1)
song_list = map(lambda x: str(x), list)

# 1. A is a proper prefix of B;
# 2. There is an index i such that the first (i-1) characters of A and B are equal, 
#    and character i of A has a smaller ASCII value than character i of B.
def smaller(a, b):
  # Check if a is a proper prefix of B
  if a == b[:len(a)]:
    return True
  # Check if it has characters smaller than current
  index = 0
  for char in a:
    if int(char) < int(b[index]):
      return True
    elif char == b[index]:
      index += 1
      if index >= len(b):
        break
    else:
      break
  return False

def merge_sort(input):
  #print 'merging:', input
  if len(input) == 1:
    return input

  middle = len(input) / 2
  left = merge_sort(input[:middle])
  right = merge_sort(input[middle:])
  #print 'left:', left, 'right:', right
  sorted_list = []
  d_ix = 0
  l_ix = 0
  r_ix = 0
  while d_ix < len(input):
    # print d_ix, l_ix, r_ix
    if l_ix == len(left):
      sorted_list.append(right[r_ix])
      r_ix += 1
    elif r_ix == len(right):
      sorted_list.append(left[l_ix])
      l_ix += 1
    elif smaller(left[l_ix], right[r_ix]):
      sorted_list.append(left[l_ix])
      l_ix += 1
    else:
      sorted_list.append(right[r_ix])
      r_ix += 1
    d_ix += 1
  return sorted_list

print merge_sort(song_list)




