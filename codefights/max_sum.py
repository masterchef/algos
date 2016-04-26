def max_sum(x, n, k):
    possible_ints = []
   
    # Collect all possible integers for our array
    for i in range(0, 2**k):
        if i & x == x:
            possible_ints.append(i)
    # Check for edge case
    if len(possible_ints) <= n:
        return sum(possible_ints)
    
    # sort integers
    possible_ints = sorted(possible_ints, reverse=True)
    return sum(possible_ints[:n-1]) + x
        
print max_sum(4, 2, 3)
print max_sum(0, 0, 0)
print max_sum(1, 1, 1)
print max_sum(11, 4, 8)
print max_sum(1000000000, 2, 30)