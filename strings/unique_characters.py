

input = 'stringissostringy'
input = 'string'
input = 'aaaa'
input = 'abababa'
input = 'abcdefg'

char_count = {}
for i in range(0, len(input)):
  c = input[i]

unique_characters = []
for i in range(0, len(input)):
  c = input[i]
  if c in char_count.keys():
    index = char_count[c]
    if index >= 0:
      unique_characters.remove(c)
      # indicate that we have already removed non unique char
      char_count[c] = -1
  else:
    # Set index of the first occurence of the character
    char_count[c] = i
    unique_characters.append(c)

print ''.join(unique_characters)
