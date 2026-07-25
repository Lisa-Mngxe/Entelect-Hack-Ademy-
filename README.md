<<<<<<< HEAD
# Ranger's Rescue Route — Level 1 Submission

## What this is
A Python implementation of Dijkstra's algorithm that finds the shortest
path from Point A to Point B on the Level 1 reserve trail network.

## Requirements
- Python 3.7+ (uses only the standard library: `heapq`, `json`)

## How to run
```bash
python3 solve.py
```

This will:
1. Build the Level 1 adjacency list (hard-coded from the challenge spec).
2. Run Dijkstra's algorithm from node "A" to node "B".
3. Print the shortest route and its total cost.
4. Write the result to `answer.txt` in the required submission format:
   ```json
   {
     "route": ["A", "D", "E", "B"]
   }
   ```

## Result
- **Route:** A → D → E → B
- **Total cost:** 9 (2 + 3 + 4)

This was the cheapest of all reasonable candidate routes checked
(A-D-F-B = 15, A-C-E-B = 13, A-C-D-E-B = 12), confirming optimality.

## Files
- `solve.py` — Dijkstra implementation and graph data
- `answer.txt` — generated submission file
- `README.md` — this file
=======
# Entelect-Hack-Ademy-
>>>>>>> d84919158669abf379203e31be50d0fb683fd5dc
