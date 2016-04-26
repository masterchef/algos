input = [16, 3, 5, 19, 10, 14, 12, 0, 15]
print input

longest_sequence_from_index = {}

longest_index = 0
for ix in range(0, len(input)):
  longest_sequence_from_index[ix] = [input[ix]]
  ix2 = ix - 1
  while(ix2 >= 0):
    if input[ix2] <= input[ix] and 
      len(longest_sequence_from_index[ix2]) + 1 > len(longest_sequence_from_index[ix]):
      longest_sequence_from_index[ix] = longest_sequence_from_index[ix2] + [input[ix]]
      longest_index = ix
    ix2 -= 1
print longest_sequence_from_index
  





