network = {
    'Min': ['William', 'Jayden', 'Omar'],
    'William': ['Min', 'Noam'],
    'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren': ['Jayden', 'Omar'],
    'Amelia': ['Jayden', 'Adam', 'Miguel'],
    'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam': ['Nathan', 'Jayden', 'William'],
    'Omar': ['Ren', 'Min', 'Scott'],
}


def getShortestRoute(network, sender, receiver, how_reached):
    breadth_queue = []
    breadth_queue.append(sender)

    while len(breadth_queue) > 0:
        element = breadth_queue.pop(0)
        if element == receiver:
            return reconstruct_path(how_reached, sender, receiver)
        else:
            for name in network[element]:
                if not (name in how_reached):
                    how_reached[name] = element
                    breadth_queue.append(name)

def reconstruct_path(previous_nodes, start_node, end_node):
    reversed_shortest_path = []

    # Start from the end of the path and work backwards
    current_node = end_node
    while current_node:
        reversed_shortest_path.append(current_node)
        current_node = previous_nodes[current_node]

    # Reverse our path to get the right order
    reversed_shortest_path.reverse()  # flip it around, in place
    return reversed_shortest_path  # no longer reversed

how_we_reached_node = {'Jayden': None}
print(getShortestRoute(network, 'Jayden', 'Adam', how_we_reached_node))
