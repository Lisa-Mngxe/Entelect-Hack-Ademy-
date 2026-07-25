import heapq
import itertools
import json


graph = {
    "A": [
        {"node": "P1", "time": 4, "risk": 0},
        {"node": "P6", "time": 5, "risk": 2}
    ],

    "B": [
        {"node": "P5", "time": 4, "risk": 0},
        {"node": "P12", "time": 4, "risk": 0}
    ],

    "S1": [
        {"node": "P3", "time": 4, "risk": 0},
        {"node": "P4", "time": 4, "risk": 1},
        {"node": "P9", "time": 5, "risk": 1}
    ],

    "S2": [
        {"node": "P7", "time": 4, "risk": 0},
        {"node": "P8", "time": 5, "risk": 1},
        {"node": "P10", "time": 5, "risk": 2}
    ],

    "S3": [
        {"node": "P1", "time": 4, "risk": 0},
        {"node": "P2", "time": 4, "risk": 1}
    ],

    "S4": [
        {"node": "P4", "time": 5, "risk": 0},
        {"node": "P5", "time": 4, "risk": 0},
        {"node": "P10", "time": 7, "risk": 0}
    ],

    "P1": [
        {"node": "A", "time": 4, "risk": 0},
        {"node": "S3", "time": 4, "risk": 0}
    ],

    "P2": [
        {"node": "S3", "time": 4, "risk": 1},
        {"node": "P3", "time": 3, "risk": 0}
    ],

    "P3": [
        {"node": "P2", "time": 3, "risk": 0},
        {"node": "S1", "time": 4, "risk": 0}
    ],

    "P4": [
        {"node": "S1", "time": 4, "risk": 1},
        {"node": "S4", "time": 5, "risk": 0}
    ],

    "P5": [
        {"node": "S4", "time": 4, "risk": 0},
        {"node": "B", "time": 4, "risk": 0}
    ],

    "P6": [
        {"node": "A", "time": 5, "risk": 2},
        {"node": "P7", "time": 4, "risk": 0}
    ],

    "P7": [
        {"node": "P6", "time": 4, "risk": 0},
        {"node": "S2", "time": 4, "risk": 0},
        {"node": "P11", "time": 4, "risk": 2}
    ],

    "P8": [
        {"node": "S2", "time": 5, "risk": 1},
        {"node": "P9", "time": 4, "risk": 2}
    ],

    "P9": [
        {"node": "P8", "time": 4, "risk": 2},
        {"node": "S1", "time": 5, "risk": 1}
    ],

    "P10": [
        {"node": "S2", "time": 5, "risk": 2},
        {"node": "S4", "time": 7, "risk": 0}
    ],

    "P11": [
        {"node": "P7", "time": 4, "risk": 2},
        {"node": "P12", "time": 5, "risk": 1}
    ],

    "P12": [
        {"node": "P11", "time": 5, "risk": 1},
        {"node": "B", "time": 4, "risk": 0}
    ]
}


def dijkstra(graph, start, end):

    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == end:
            break

        for neighbour in graph[current_node]:

            node = neighbour["node"]
            weight = neighbour["time"] + neighbour["risk"]

            distance = current_distance + weight

            if distance < distances[node]:
                distances[node] = distance
                previous[node] = current_node
                heapq.heappush(priority_queue, (distance, node))

    path = []

    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[end]


stations = ["S1", "S2", "S3", "S4"]

best_cost = float("inf")
best_route = None

for order in itertools.permutations(stations):

    targets = ["A"] + list(order) + ["B"]

    total_cost = 0
    full_route = []

    valid = True

    for i in range(len(targets) - 1):

        path, cost = dijkstra(graph, targets[i], targets[i + 1])

        if cost == float("inf"):
            valid = False
            break

        total_cost += cost

        if len(full_route) == 0:
            full_route.extend(path)
        else:

            full_route.extend(path[1:])

    if valid and total_cost < best_cost:
        best_cost = total_cost
        best_route = full_route


print("=" * 50)
print("BEST ROUTE FOUND")
print("=" * 50)

print("Total Cost:", best_cost)
print()

print("Route:")
print(" -> ".join(best_route))

submission = {
    "route": best_route
}

with open("submission.json", "w") as file:
    json.dump(submission, file, indent=4)

print("\nsubmission.json created successfully.")