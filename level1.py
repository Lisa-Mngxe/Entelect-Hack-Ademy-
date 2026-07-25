import heapq
import json

graph = {
    "A": [{"node": "C", "weight": 4}, {"node": "D", "weight": 2}],
    "B": [{"node": "E", "weight": 4}, {"node": "F", "weight": 7}],
    "C": [{"node": "A", "weight": 4}, {"node": "D", "weight": 1}, {"node": "E", "weight": 5}],
    "D": [{"node": "A", "weight": 2}, {"node": "C", "weight": 1},
          {"node": "E", "weight": 3}, {"node": "F", "weight": 6}],
    "E": [{"node": "C", "weight": 5}, {"node": "D", "weight": 3},
          {"node": "F", "weight": 2}, {"node": "B", "weight": 4}],
    "F": [{"node": "D", "weight": 6}, {"node": "E", "weight": 2},
          {"node": "B", "weight": 7}]
}


def dijkstra(graph, start, end):

    pq = [(0, start)]


    distances = {node: float("inf") for node in graph}
    distances[start] = 0


    previous = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)


        if current_distance > distances[current_node]:
            continue


        if current_node == end:
            break


        for neighbour in graph[current_node]:
            next_node = neighbour["node"]
            weight = neighbour["weight"]

            distance = current_distance + weight

            if distance < distances[next_node]:
                distances[next_node] = distance
                previous[next_node] = current_node
                heapq.heappush(pq, (distance, next_node))


    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[end]


def main():
    start = "A"
    end = "B"

    route, total_cost = dijkstra(graph, start, end)

    print("Shortest Route:", " -> ".join(route))
    print("Total Cost:", total_cost)

    answer = {
        "route": route
    }

    print("\nSubmission JSON:")
    print(json.dumps(answer, indent=4))

    with open("answer.txt", "w") as file:
        json.dump(answer, file, indent=4)

    print("\nanswer.txt has been created.")


if __name__ == "__main__":
    main()
import os

print("Current working directory:", os.getcwd())