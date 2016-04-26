input = 10
input = 16
input = 32
input = 109
song_list = []
song_suffix = '.mp3'

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

def insert_into_song_list(new_song, song_list):
  new_list = []
  added = False
  # print 'adding:', new_song, 'to:', song_list
  for song in song_list:
    if smaller(new_song, song) and not added:
      new_list.append(new_song)
      new_list.append(song)
      added = True
    else:
      new_list.append(song)
  if not added:
    new_list.append(new_song)

  return new_list


for i in range(1, input+1):
  current_song = str(i)
  song_list = insert_into_song_list(current_song, song_list)

print song_list