# Name: Anthony Stark
# OSU Email: starkan@oregonstate.edu
# Course: CS325 - Analysis of Algorithms
# Assignment: 8 Portfolio Project Puzzle
# Due Date: 3/3/2025
# Description: Utilizes BFS to find the shortest distance from a starting cell to an ending cell in a 2D matrix.

def solve_puzzle(Board, Source, Destination):
    '''
    Finds the shortest path from the source to destination across the board.
    :param Board: 2D matrix containing "-" (passable) or "#" (obstacle)
    :param Source: tuple representing coordinates of starting cell
    :param Destination: tuple representing coordinates of ending cell
    :return: A list of tuples containing shortest path from source to destination
    '''

    from queue import Queue

    # calculate distances of matrix, m = rows, n = columns
    m = len(Board)
    n = len(Board[0])

    # initialize 2D arrays to store parent node, direction and visited status
    parent_arr = [[None] * n for _ in range(m)]
    visited_arr = [[False] * n for _ in range(m)]
    direction_arr = [[None] * n for _ in range(m)]

    # find row and column of source tuple
    source_row = Source[0]
    source_col = Source[1]

    # find row and column of destination tuple
    dest_row = Destination[0]
    dest_col = Destination[1]

    # initialize starting values for visited array
    visited_arr[source_row][source_col] = True

    # initialize queue (row, column)
    q = Queue()
    start = (source_row, source_col)
    q.put(start)

    # Directions for traversal (Up, Down, Right, Left)
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, 1, 'R'), (0, -1, 'L')]

    # main loop
    while not q.empty():
        current = q.get()
        current_row, current_col = current[0], current[1]
        # check for destination cell
        if current_row == dest_row and current_col == dest_col:
            # initialize path and direction lists
            path = []
            directions = ''
            # work backwards to add parent nodes to path list and direction strings to direction list
            while current is not None:
                path.append((current[0], current[1]))
                if parent_arr[current[0]][current[1]] is not None:
                    directions += direction_arr[current[0]][current[1]]
                current = parent_arr[current[0]][current[1]]
            # reverse path and string
            path.reverse()
            directions = directions[::-1]
            # add direction list to the end of path
            return (path, directions)

        # moves to neighbor
        for dr, dc, d_char in directions:
            new_row, new_col = current_row + dr, current_col + dc

            # validity check
            if (0 <= new_row < m and 0 <= new_col < n
                    and Board[new_row][new_col] != '#' and not visited_arr[new_row][new_col]):
                # mark visited
                visited_arr[new_row][new_col] = True
                # update parent array
                parent_arr[new_row][new_col] = (current_row, current_col)
                # update direction array
                direction_arr[new_row][new_col] = d_char
                # add cell to queue
                q.put((new_row, new_col))

    # if no path exists
    return None

def main():
  # Test case 1
  Board = [
      ['-', '-', '-', '-', '-'],
      ['-', '-', '#', '-', '-'],
      ['-', '-', '-', '-', '-'],
      ['#', '-', '#', '#', '-'],
      ['-', '#', '-', '-', '-']
  ]
  input = (0,2)
  destination = (2,2)
  print(f"Test case 1: Puzzle({input}, {destination}) = {solve_puzzle(Board, input, destination)} (Expected: [(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR')]")

  # test case 2
  Board = [
      ['-', '-', '-', '-', '-'],
      ['-', '-', '#', '-', '-'],
      ['-', '-', '-', '-', '-'],
      ['#', '-', '#', '#', '-'],
      ['-', '#', '-', '-', '-']
  ]
  input = (0,0)
  destination = (4,4)
  print(f"Test case 1: Puzzle({input}, {destination}) = {solve_puzzle(Board, input, destination)} [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 'RRRRDDDD')]")
if __name__ == "__main__":
  main()