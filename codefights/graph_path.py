# def FriendEnemy(matrix, start, end, path):
#     #print start, end, path
#     # Find all possible next moves
#     for i in range(0, len(matrix)):
#         if matrix[start][i] == path[0]:
#             #print matrix[start][i], i, end
#             # If we found the end of our path and we're can reach the end vertex then return True
#             if len(path) == 1 and i == end:
#                 return True
#             if len(path) > 1:
#                 return FriendEnemy(matrix, i, end, path[1:])
#     return False


def FriendEnemy(matrix, start, end, path):
    if len(path) == 0:
        return False
    
    endpoints = [()]*len(path)
    for j in range(len(matrix)):
        if matrix[start][j] == path[0]:
            endpoints[0] += (j,) 

    i = 0
    while i < len(path):
        # Go over all next endpoints
        for e in range(0, len(endpoints[i])):
            # Check where they would lead to next
            for j in range(len(matrix)):
                # Return true if we reached the end of the path
                if i+1 == len(path):
                    return True
                elif matrix[e][j] == path[i+1] and j not in endpoints:
                        endpoints[i+1] += (j,)
        i += 1
    return False
    
matrix = [["E","F","-","-"], 
 ["F","-","-","-"], 
 ["-","-","-","-"], 
 ["-","-","-","-"]]
start = 0
end =  0
path = "EFF"

# matrix = [["E","F","-","-"], 
#  ["F","-","-","-"], 
#  ["-","-","-","-"], 
#  ["-","-","-","-"]]
# start = 0
# end = 0
# path = "F"

# matrix = [["E","F","E","E"], 
#  ["F","E","F","F"], 
#  ["E","F","F","E"], 
#  ["F","F","F","E"]]
# start = 0
# end = 3
# path = "EEF"

# matrix = [["F","E","E","E","E","E","F"], 
#  ["F","F","F","F","F","E","-"], 
#  ["F","F","F","E","F","-","-"], 
#  ["F","F","F","-","-","E","-"], 
#  ["F","F","F","E","-","-","-"], 
#  ["F","F","F","E","-","F","-"], 
#  ["F","F","F","E","F","E","F"]]
# start = 0
# end = 6
# path = "EEFEFFEFEEFFEEEFE"

# matrix = [["-","F","-","-"], 
#  ["-","-","F","-"], 
#  ["-","-","-","E"], 
#  ["E","-","-","-"]]
# start = 3
# end = 2
# path = "EFFEEFFEEFFEEFFEEFFEEFFEEFF"

# matrix = [[]]
# start = 3
# end = 2
# path = "EFFEEFFEEFFEEFFEEFFEEFFEEFF"

# matrix = [["F","E","E","E","E","E","F"], 
#  ["F","F","F","F","F","E","-"], 
#  ["F","F","F","E","F","-","-"], 
#  ["F","F","F","-","-","E","-"], 
#  ["F","F","F","E","-","-","-"], 
#  ["F","F","F","E","-","F","-"], 
#  ["F","F","F","E","F","E","F"]]
# start = 0
# end = 6
# path = "FEFFF"


print FriendEnemy(matrix, start, end, path)