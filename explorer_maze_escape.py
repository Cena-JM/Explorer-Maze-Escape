# To find the shortest path, we need to know where we are going in the first place.
# After knowing our destination(goal), we map out a trail to our starting point from the 
# destination(goal) taking the shortest path.

def maze_escape(maze):
    goal_pos = find_goal_pos(maze, [])
    shortest_route(maze, goal_pos, [])

def find_goal_pos(maze, goal_pos):
    for path in range(len(maze)):
        if 9 in maze[path]:
            goal_pos.extend([maze[path].index(9), path])
            break

    return goal_pos

def shortest_route(maze, goal_pos, steps):
    while goal_pos[1] >= 0:
        while goal_pos[0] >= 0:
            i, j = goal_pos[0], goal_pos[1]
            steps.append([i, j])
            if maze[j - 1][i] == 0 and j - 1 >= 0: break

            goal_pos[0] -= 1
        goal_pos[1] -= 1
        
    print(steps[::-1])

maze_escape(
  [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 9]
  ]
)
# => [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [2, 3], [3, 3], [4, 3], [4, 4]]

maze_escape(
  [
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 9],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]
  ]
)
# => [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3]]

maze_escape(
  [[0, 0, 0, 0, 0, 1, 0, 0, 0],
   [0, 1, 0, 1, 0, 1, 1, 0, 1],
   [0, 1, 0, 1, 0, 0, 0, 0, 0],
   [1, 1, 0, 1, 1, 1, 0, 1, 1],
   [0, 0, 0, 0, 0, 1, 0, 0, 1],
   [1, 1, 1, 1, 0, 1, 1, 1, 1],
   [0, 0, 0, 0, 0, 0, 0, 0, 1],
   [0, 1, 1, 0, 0, 1, 1, 0, 9],
   [0, 0, 1, 0, 0, 0, 0, 0, 0]]
)
# => [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 4], [4, 4], [4, 5], [4, 6], [5, 6], [6, 6], [7, 6], [7, 7], [8, 7]]