# input: list of pairs of integers, for example [(1,2), (5,6), (7,3), ...]
# input: a non-negative integer "K"
# output: the "K" points from the input that are closest to the origin (0,0)

# for example: if K=2, [(1,2), (7,3)]

#merge sort
#O(nlog(n))
#memory: 2n

#n + nlong(n) => O(nlog(n))
#memory: n + n => 2n

# n * klong(k) => nklong(k)

#O(nk)
def sort_coordinates(input, k):
    k = 2
    output = []
    #lost you again, goint to continue coding while you call back
    for coordinate in input:
        #calculate relative distance to 0,0
        distance = coordinate(0)**2 + coordinate(1)**2
        current_element = {'dist': distance, 'coordinate': coordinate}
        #insert current_element into output respecting it's order
        output = insert_element(output, current_element, k)
    return output

def insert_element(output, new_element, max_element):
    # check if element is larger than the last element in the output
    if len(output) == max_element and output[-1]['dist'] < new_element['dist']
        return
    
    # loop over output and insert new element
    new_output = []
    for i in range(0, len(output)):
        current_element = output[i]
        # If new element is closer then the current element in the output append it
        # before the current element, otherwise just add current_element
        if new_element['dist'] < current_element['dist']:
            new_output.append(new_element)
            # concetenate the rest of the output to the end of new output
            new_output += output[i:-1]
            break
        else:
            new_output.append(current_element)
            
    return new_output
    
    
return sort_coordinates([(1,2), (5,6), (7,3)], 2)
