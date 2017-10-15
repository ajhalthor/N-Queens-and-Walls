# N Queens and Walls

DFS, BFS and Simulated Annealing implementation of an extension of the N-Queens Problem. 

Most Queens are greedy. They want exclusive rights to the throne and will destroy anyone who poses a threat. If a Queen sees another on their turf (row, column or diagonal), they will not hesitate to wage war against the other. We live in a time of peace (relatively) and hence task our selves with the goal of placing these queens on the board such that no war needs to be faught. The typical N-Queens problem involves arranging N such queens on an N x N board such that peace is maintained.  

We are going to solve the N Queens problem, but with a twist: Aside from the usual queens on the board, we have walls! The objective is to place Queens on a board such that no queen can kill another. Walls act as a barrier, so no queen can pass through them. As such, it is possible to place muliple queens on the same row, column or diagonal depending on the location of these walls. And .. Oh yeah, there is a time limit of 300 seconds to figure out the solution. 

It is possible to add the number of Queens greater than the dimension of the board. We are going to solve this problem in **3 different methods** because thats how cool we are. 
- Depth First Search 
- Breadth First Search 
- Simulated Annealing

## Input File Structure

The file input.txt in the current directory of your program will be formatted as follows:

- **First line**: instruction of which algorithm to use: BFS, DFS or SA
- **Second line**: strictly positive 32-bit integer N, the width and height of the square nursery
- **Third line**:  strictly positive 32-bit integer p, the number of queens
- **Next N lines**: the N x N board, one file line per row (to show you where the walls are). It will have a 0 where there is nothing, and a 2 where there is a wall.

##  Output File Structure
 
The file output.txt which your program creates in the current directory should be formatted as follows:
- **First line**: OK or FAIL, indicating whether a solution was found or not. If FAIL, any following lines are ignored.
- **Next N lines**: the n x n nursery, one line in the file per nursery row, including the baby lizards and trees. It will have a 0 where there is nothing, a 1 where you placed a baby lizard, and a 2 where there is a tree.

## Execution

Change the file path on line 330 in the code:

```
lines = tuple(open(`<input file name>`, 'r'))
```

Run the file with the following command:

```
$ python queens_n_walls.py
```

## Examples


Here is a sample input file:
```
SA
8
8
00000000
00000000
00000000
00002000
00000000
00000200
00000000
00000000
```
We need to use Simulated Annealing to place 8 Queens on an 8 x 8 board with 2 trees. Here is the output file my program generated:

```
OK
01000000
00001000
10000000
00002001
00000100
00100200
00000010
00010000
```

Lets consider an input in which the number of queens is greater than the dimesions of the board:

```
BFS
7
8
0000000
0002000
0000000
0000200
0000000
0002020
0000000
```

We place 8 queens on a 7 x 7 board using Breadth First Search. Here is the output:

```
OK
1000000
0012100
0000000
0100210
0001000
0002021
0001000
```

Let us consider an even more difficult board with 15 queens on a 11 x 11 board. This time, we use Depth First Search to solve the problem.

```
DFS
11
15
00020000200
00200002000
02000020000
20000200000
00000000000
00002020000
00020002000
00200000200
02000000020
20000000002
00000000000
```

And the solution:
```
OK
10020000200
00200102001
02010020100
21000210000
00000000010
00102021000
00020002000
00201000200
12000001020
20000100002
00010000000
```
