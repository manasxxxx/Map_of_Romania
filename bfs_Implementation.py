from queue import Queue

# Define the map of Romania and its connections
city_map = {
    'Oradia': ['Zerind', 'Sibiu'], 
    'Zerind': ['Arad', 'Oradia'],
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Sibiu': ['Arad', 'Oradia', 'Fagaras', 'Rimnicu'],  
    'Timisoara': ['Arad', 'Lugoj'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Eforie': ['Hirsova'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

# Performing BFS 
def bfs(startingNode, destinationNode):
    visited = {}  # Dictionary to track visited nodes
    parent = {}   # Dictionary to track parent of each node
    queue = Queue()  # Queue for BFS

    # Initialize visited and parent dictionaries
    for city in city_map.keys():
        visited[city] = False
        parent[city] = None

    # Starting node
    visited[startingNode] = True
    queue.put(startingNode)

    while not queue.empty():
        current = queue.get()  # Get the front element of the queue

        # Explore each neighbor of the current node
        for neighbor in city_map[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.put(neighbor)

    # Reconstruct the path from destination to starting
    path = []
    step = destinationNode
    while step is not None:
        path.append(step)
        step = parent[step]

    path.reverse()  
    
    if startingNode in path and destinationNode in path:
        print(f"\nPath from {startingNode} to {destinationNode}: {' -> '.join(path)}")
    else:
        print(f"No path found from {startingNode} to {destinationNode}.")

# taking Input from user
startingCity = input("Enter the starting city: ").strip().title()
destinationCity = input("Enter the destination city: ").strip().title()

bfs(startingCity, destinationCity)