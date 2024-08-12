from queue import Queue
import heapq

# Define the map of Romania with connections and costs
city_graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
    'Rimnicu': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

def bfs(start, goal):
    visited = {city: False for city in city_graph}
    parent = {city: None for city in city_graph}
    queue = Queue()

    visited[start] = True
    queue.put((start, 0))

    while not queue.empty():
        current, cost = queue.get()

        if current == goal:
            break

        for neighbor, travel_cost in city_graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = (current, travel_cost)
                queue.put((neighbor, cost + travel_cost))

    return reconstruct_path(parent, start, goal)

def dfs(start, goal):
    visited = {city: False for city in city_graph}
    parent = {city: None for city in city_graph}
    stack = [(start, 0)]
    visited[start] = True

    while stack:
        current, cost = stack.pop()

        if current == goal:
            break

        for neighbor, travel_cost in city_graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = (current, travel_cost)
                stack.append((neighbor, cost + travel_cost))

    return reconstruct_path(parent, start, goal)

def ucs(start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == goal:
                return path, cost

            for next_node, next_cost in city_graph.get(node, []):
                if next_node not in visited:
                    heapq.heappush(queue, (cost + next_cost, next_node, path))

    return None, 0

def reconstruct_path(parent, start, goal):
    path, total_cost = [], 0
    step = goal

    while step is not None:
        path.append(step)
        step_info = parent[step]
        if step_info is not None:
            step, travel_cost = step_info
            total_cost += travel_cost
        else:
            step = None

    path.reverse()
    return (path, total_cost) if start in path and goal in path else (None, 0)

def main():
    startingCity = input("Enter the starting city: ").strip().title()
    destinationCity = input("Enter the destination city: ").strip().title()

    # BFS Path and Cost
    bfs_path, bfs_cost = bfs(startingCity, destinationCity)
    if bfs_path:
        print(f"\nBFS Path from {startingCity} to {destinationCity}: {' -> '.join(bfs_path)}, Cost: {bfs_cost}")
    else:
        print(f"No BFS path found from {startingCity} to {destinationCity}.")

    # DFS Path and Cost
    dfs_path, dfs_cost = dfs(startingCity, destinationCity)
    if dfs_path:
        print(f"\nDFS Path from {startingCity} to {destinationCity}: {' -> '.join(dfs_path)}, Cost: {dfs_cost}")
    else:
        print(f"No DFS path found from {startingCity} to {destinationCity}.")

    # UCS Path and Cost
    ucs_path, ucs_cost = ucs(startingCity, destinationCity)
    if ucs_path:
        print(f"\nUCS Path from {startingCity} to {destinationCity}: {' -> '.join(ucs_path)}, Cost: {ucs_cost}")
    else:
        print(f"No UCS path found from {startingCity} to {destinationCity}.")

    # Determine the optimal path
    paths_costs = [('BFS', bfs_path, bfs_cost), ('DFS', dfs_path, dfs_cost), ('UCS', ucs_path, ucs_cost)]
    optimal_method, optimal_path, optimal_cost = min((pc for pc in paths_costs if pc[1]), key=lambda x: x[2])

    print(f"\nOptimal Path using {optimal_method}: {' -> '.join(optimal_path)}, Cost: {optimal_cost}")

if __name__ == "__main__":
    main()
