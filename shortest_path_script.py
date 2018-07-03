from Queue import *
# SHORTEST PATH
def find_shortest_path (source_tile, target_tile): # breadth search
    visited_tiles = set()  # contains visited tiles
    number_of_moves = {}  # index - tile number , element - number of moves
    nodes_queue = set()
    nodes_queue.add(source_tile)
    number_of_moves[source_tile] = 0  # the first tile is 0 moves away
    while (len(nodes_queue) > 0):
        node = nodes_queue.pop()
        if (node == target_tile):
            solution = number_of_moves[target_tile]
            break
        else:
            for child in knight_moves_tile(node): # For each possible move
                child = convert_indexes(child)
                if child not in visited_tiles and child not in nodes_queue:
                    number_of_moves[child] = number_of_moves[node] + 1  # the child is one move away from the parent
                    nodes_queue.add(child)
            visited_tiles.add(node)
    return solution


# FUNCTIONS RELATED TO CONVERSIONS AND FINDING POSSIBLE MOVES

def convert_indexes(location_object):
    """converts indexes into tile number"""
    return location_object['x']*8 + location_object['y']


def convert_location(location):
    """converts location into two indexes"""
    index_one = int(location / 8)
    index_two = (location) % 8
    return {
        "x": index_one,
        "y": index_two
    }

def knight_moves_location(location_object):
    """returns an array of location objects after possible moves"""
    return_moves = []

    x = location_object["x"]
    y = location_object["y"]
    moveTransforms = [
        {
            "x": 2,
            "y": 1
        },
        {
            "x": 1,
            "y": 2
        },
        {
            "x": 2,
            "y": -1,
        },
        {
            "x": 1,
            "y": -2
        }
    ]

    factor_array = [1, -1]
    for factor in factor_array:
        for move in moveTransforms:
            move = {
                "x": x + (factor * move["x"]),
                "y": y + (factor * move["y"])
            }
            if valid_location(move):
                return_moves.append(move)
    return return_moves


def knight_moves_tile(tile_number):
    """returns an array of location objects after possible moves"""
    location_object = convert_location(tile_number)
    return knight_moves_location(location_object)


def valid_location(location_object):
    """checks to see if the location is valid"""
    x = location_object["x"]
    y = location_object["y"]
    return (x >= 0 and y >= 0) and (x <= 7 and y <= 7)

"""
tile = 40
possible_moves = knight_moves_tile(tile)
for move in possible_moves:
    print(convert_indexes(move))
"""

print("SHORTEST")
print(find_shortest_path(7, 56))
