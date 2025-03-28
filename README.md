# Algorithm-Portfolio-Project
An algorithm that finds the shortest path through a maze.

I designed this by implementing an algorithm that utilizes BFS to find the shortest distance from the starting point to the ending cell. I then used a queue to store cells to visit and a few 2D arrays to store the parent node of each cell, whether the cell has been visited or not, and the string direction taken to get to the cell. 

For each cell in the queue, the algorithm checks to see if it is the ending cell, if it is, the algorithm returns the path to that cell along with the string directions to get there. If it is not the ending cell, the algorithm checks the validity of the move, and add neighbor cells to the queue if they have not already been visited.
