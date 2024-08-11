import heapq

# Define the graph (cities and distances)
graph = {
    'arad': [('zerind', 75), ('sibiu', 140), ('timisoara', 118)],
    'zerind': [('arad', 75), ('oradea', 71)],
    'oradea': [('zerind', 71), ('sibiu', 151)],
    'sibiu': [('arad', 140), ('oradea', 151), ('fagaras', 99), ('rimnicu', 80)],
    'timisoara': [('arad', 118), ('lugoj', 111)],
    'lugoj': [('timisoara', 111), ('mehadia', 70)],
    'mehadia': [('lugoj', 70), ('drobeta', 75)],
    'drobeta': [('mehadia', 75), ('craiova', 120)],
    'craiova': [('drobeta', 120), ('rimnicu', 146), ('pitesti', 138)],
    'rimnicu': [('sibiu', 80), ('craiova', 146), ('pitesti', 97)],
    'fagaras': [('sibiu', 99), ('bucharest', 211)],
    'pitesti': [('rimnicu', 97), ('craiova', 138), ('bucharest', 101)],
    'bucharest': [('fagaras', 211), ('pitesti', 101), ('giurgiu', 90), ('urziceni', 85)],
    'giurgiu': [('bucharest', 90)],
    'urziceni': [('bucharest', 85), ('hirsova', 98), ('vaslui', 142)],
    'hirsova': [('urziceni', 98), ('eforie', 86)],
    'eforie': [('hirsova', 86)],
    'vaslui': [('urziceni', 142), ('iasi', 92)],
    'iasi': [('vaslui', 92), ('neamt', 87)],
    'neamt': [('iasi', 87)]
}

def ucs(graph, start, goal):
    queue = [(0, start, [])] # Priority queue to store (cost, current_node, path)
    visited = set() # Set to store visited nodes

    while queue:
        # Get the node with the lowest cost
        cost, node, path = heapq.heappop(queue)

        # Check if node is visited
        if node not in visited:
            visited.add(node)  # Mark node as visited
            path = path + [node]  # Add node to path

            # Check if goal is reached
            if node == goal:
                return cost, path  # Return cost and path

            # Expand the current node
            for next_node, next_cost in graph.get(node, []):
                if next_node not in visited:
                    heapq.heappush(queue, (cost + next_cost, next_node, path))
    
    return None  # Return None if no path is found

# Input the start and end cities from user
start_city = input("Enter the start city: ").strip().lower()
goal_city = input("Enter the goal city: ").strip().lower()

if start_city not in graph or goal_city not in graph:
    print("One or both of the cities are not in the graph.")
else:
    # Find the cheapest route using UCS
    result = ucs(graph, start_city, goal_city)

    if result:  # Check if a path was found
        cost, path = result
        print(f"\nShortest route from {start_city.capitalize()} to {goal_city.capitalize()}:")
        print(f"Route: {' -> '.join(path)}, Cost: {cost}")
    else:
        print(f"No route found from {start_city.capitalize()} to {goal_city.capitalize()}.")