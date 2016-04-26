#input = [1, 7, 4, 9, 2, 5] #6
#input = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8] #7
#input = [1, 2, 3, 4, 5, 6, 7, 8, 9] #2
#input =  [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32] #8
input = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
249, 22, 176, 279, 23, 22, 617, 462, 459, 244] #36
print input

longest_negative_sequence_from_index = {}
longest_positive_sequence_from_index = {}

longest_pos_seq = []
longest_neg_seq = []
if len(input) == 1:
  print 1
  exit

for ix in range(1, len(input)):
  ix2 = ix - 1
  while(ix2 >= 0):
    diff = input[ix] - input[ix2]

    # Let's set the first diff for the current index if it doesnt yet exist
    if ix not in longest_negative_sequence_from_index.keys():
      longest_negative_sequence_from_index[ix] = []
    if ix not in longest_positive_sequence_from_index.keys():
      longest_positive_sequence_from_index[ix] = []
    if ix2 not in longest_negative_sequence_from_index.keys():
      longest_negative_sequence_from_index[ix2] = [input[ix2]]
    if ix2 not in longest_positive_sequence_from_index.keys():
      longest_positive_sequence_from_index[ix2] = [input[ix2]]

    # print 'ix:', ix, 'ix2:', ix2, 'diff:', diff
    
    if diff == 0:
      ix2 -= 1
      continue

    if diff < 0:
      # check if we habe a positive sequence we can add to from a previous digit
      # print 'previous post seq, for:', ix2, longest_positive_sequence_from_index[ix2]
      if len(longest_positive_sequence_from_index[ix2]) + 1 > len(longest_negative_sequence_from_index[ix]):
        longest_negative_sequence_from_index[ix] = longest_positive_sequence_from_index[ix2] + [input[ix]]
        # print 'neg', longest_negative_sequence_from_index
    else:
      # print 'previous neg seq, for:', ix2, longest_negative_sequence_from_index[ix2]
      # check if we have a negative sequence we can add tofrom a previous digit
      if len(longest_negative_sequence_from_index[ix2]) + 1 > len(longest_positive_sequence_from_index[ix]):
        longest_positive_sequence_from_index[ix] = longest_negative_sequence_from_index[ix2] + [input[ix]]
        # print 'pos', longest_positive_sequence_from_index

    if ix in longest_negative_sequence_from_index.keys() and len(longest_negative_sequence_from_index[ix]) > len(longest_neg_seq):
      longest_neg_seq = longest_negative_sequence_from_index[ix]
    if ix in longest_positive_sequence_from_index.keys() and len(longest_positive_sequence_from_index[ix]) > len(longest_pos_seq):
      longest_pos_seq = longest_positive_sequence_from_index[ix]

    #print 'current postive:', longest_positive_sequence_from_index
    #print 'current negative:', longest_negative_sequence_from_index
    ix2 -= 1

#print longest_positive_sequence_from_index
#print longest_negative_sequence_from_index

print input
print 'longest neg: ', longest_neg_seq, 'len:', len(longest_neg_seq)
print 'longest pos: ', longest_pos_seq, 'len:', len(longest_pos_seq)
  





