def perfectCity(departure, destination):
    start_x = departure[0]
    start_y = departure[1]
    end_x = destination[0]
    end_y = destination[1]
    
    # Return if we're already here
    if start_x == end_x and start_y == end_y:
        return 0
    
    moves = []
    locations = {}
    moves.append({'x': start_x, 'y': start_y, 'cost': 0})
    while True:
        current = moves.pop(0)
        # Needed for checking if we're in the middle of a block
        rounded_y = round(current['y'])
        rounded_x = round(current['x'])
        
        if current['x'] == end_x and current['y'] == end_y:
            return current['cost']
        
        # Compute all possible next moves
        #right
        next_location = {'x': round(current['x'] + 0.1, 1),
                         'y': current['y'],
                         'cost': round(current['cost'] + 0.1, 1)}
        location_key = str(next_location['x']) + '-' + str(next_location['y'])
        if rounded_y == current['y'] and location_key not in locations.keys():
            locations[location_key] = 1
            moves.append(next_location)
        
        #right
        next_location = {'x': round(current['x'] - 0.1, 1),
                         'y': current['y'],
                         'cost': round(current['cost'] + 0.1, 1)}
        location_key = str(next_location['x']) + '-' + str(next_location['y'])
        if rounded_y == current['y'] and location_key not in locations.keys():
            locations[location_key] = 1
            moves.append(next_location)
        
        #up
        next_location = {'x': current['x'],
                         'y': round(current['y'] + 0.1, 1),
                         'cost': round(current['cost'] + 0.1, 1)}
        location_key = str(next_location['x']) + '-' + str(next_location['y'])
        if rounded_x == current['x'] and location_key not in locations.keys():
            locations[location_key] = 1
            moves.append(next_location)
            
        #down
        next_location = {'x': current['x'],
                         'y': round(current['y'] - 0.1, 1),
                         'cost': round(current['cost'] + 0.1, 1)}
        location_key = str(next_location['x']) + '-' + str(next_location['y'])
        if rounded_x == current['x'] and location_key not in locations.keys():
            locations[location_key] = 1
            moves.append(next_location)
            



#print perfectCity([0.4, 1], [0.9, 3])     
#print perfectCity([2.4, 1], [5, 7.3])     
print perfectCity([0, 0.2], [7, 0.5])     
#print perfectCity([0.4, 1], [0.9, 3])      

