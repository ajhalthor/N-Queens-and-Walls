import copy
import math
import time 
import random
import signal

class mylist (list):
	"""Override the default list() class to ensure negative indices are prohibited."""

	def __getitem__(self, n):
		if n < 0:
			raise IndexError(n ,"Out Of Range")
		return list.__getitem__(self, n)


class State:
	"""Represents an NxN board instance

	Every “State”
	- D: Next column to insert lizard [1:N].
	- N x N board of “Squares”
	"""

	def __init__(self, d, board):
		self.lizard_count = 0
		self.tree_count = 0
		self.d = d
		self.board = board


	def _goal_check(self):
		"""Number of Lizards should be the same as input p."""
		if self.lizard_count != p:
			return False
		return True

	def is_square_safe(self, r, c):
		"""Check if a given cell is safe."""

		rmul = [-1, 1,  0, 0, 1,  1, -1, -1]
		cmul = [ 0, 0, -1, 1, 1, -1,  1, -1]

		for k in range(0, 8):
			i=1
			try:
				while True:
					if self.board[r+i*rmul[k]][c+i*cmul[k]] == 1: return False
					if self.board[r+i*rmul[k]][c+i*cmul[k]] == 2: break
					i+=1			
			except IndexError as e:
				pass

		return True


class Node:
	"""Represents every Node in the Tree.

	Every “Node” has the following properties:
	- State
	- Pointer to Parent node
	- No need of “Action”(there is only 1 general action) and “Path Cost”(irrelevant to BFS & DFS).
	"""

	def __init__(self, d, board, parent=None):
		self.state = State(d=d, board=board)
		self.parent = parent


	"Check if current state is the goal state"
	def is_goal(self):
		return self.state._goal_check()


class Problem:
	"""Definition of a Problem for Solving this N-Lizards-with-Trees Problem

	Every “Problem” has the following properties:
	- Initial state: The input n x n board matrix with the position of trees. (given in input file)
	- Goal State: A board with all lizards and trees such that no lizard can attack
	"""


class BFS(Problem):
	"""Solution to the Problem using BFS"""

	def __init__(self):
		self.frontier = []
		self.explored = []

	def algorithm(self, node):

		bfs.frontier.append(node) #Add node to Frontier

		while True:
			if len(bfs.frontier) == 0:
				return False
				exit()

			node = bfs.frontier.pop(0) #Get 1st node from Frontier
			bfs.explored.append(node) #Add node to Explored

			while node.state.d < ((int(p/N) + 1) * N):
				c = node.state.d % N

				for r in range(0,N):
					if node.state.board[r][c] != 0 or not node.state.is_square_safe(r, c): 
						continue

					#Create a child Node
					child = copy.deepcopy(node)
					child.state.board[r][c] = 1 #We have a lizard there 
					child.state.lizard_count = node.state.lizard_count + 1 #We have a lizard there 
					child.state.d = node.state.d + 1
					child.parent = node #pointer to parent

					if child.is_goal(): 
						solution(child.state.board, N)
						exit()
					else:
						bfs.frontier.append(child)

				node.state.d = node.state.d + 1


class DFS(Problem):
	"""Solution to the Problem using DFS"""

	def __init__(self):
		self.explored = []

	def backtrack(self, node):
		"""Core of DFS

		Args:
			- node (Node): state of current board

		Returns:
			- status (boolean): Fail if no solution was found
		"""
		while node.state.d < ((int(p/N) + 1) * N):
			c = node.state.d % N
			for r in range(0,N):
				if node.state.board[r][c] != 0 or not node.state.is_square_safe(r, c): 
					continue

				#Create a child Node
				child = copy.deepcopy(node)
				child.state.board[r][c] = 1 #We have a lizard there 
				child.state.lizard_count = node.state.lizard_count + 1 #We have a lizard there 
				child.state.d = (node.state.d + 1)
				child.parent = node #pointer to parent

				if child.is_goal(): 
					solution(child.state.board, N)
					exit()
				else:
					self.backtrack(child)

			node.state.d = node.state.d + 1

		return False

class SA(Problem):
	"""Solution with Simulated Annealing"""


	def random_board(self, node):
		"""Randomly place p lizards on the board"""
		if p <= N:
			c = 0

			while node.state.lizard_count != p:
				for r in range(0, N):
					if node.state.board[r][c] == 0:
						node.state.board[r][c] = 1 #Place Lizard
						node.state.lizard_count += 1
						break
				c = (c+1) % N

		else:
			c = 0

			while node.state.lizard_count != p:
				for r in range(0, N):
					if node.state.lizard_count >= N:
						#check if current column is safe
						if node.state.is_square_safe(r, c) and node.state.board[r][c] == 0:
							node.state.board[r][c] = 1
							node.state.lizard_count += 1
							break
					else:
						if node.state.board[r][c] == 0:
							node.state.board[r][c] = 1 #Place Lizard
							node.state.lizard_count += 1
							break
				c = (c+1) % N

		return node

	def schedule(self, t):
		"""Scheduling function

		Args:
			- t (int): time/iteration number

		Returns:
			- Scheduling function as a function of t
		"""

		return 1 /(1+math.log(1+t*10))

	def choose_successor(self, node):
		"""Choose the next state to traverse

		Args:
			- node (Node): current state of the board

		Returns:
			- node (Node): Next state
		"""

		while True:
			r = random.randint(0, N-1)
			c = random.randint(0, N-1)

			if node.state.board[r][c] == 0:

				#Assign the first lizard in this column to 0
				i=(r+1) % N
				while i != r:
					if node.state.board[i][c] == 1:
						node.state.board[i][c] = 0
						break
					i = (i+1) % N

				node.state.board[r][c] = 1
				return node

	def num_safe_lizards(self, node):
		"Return number of safe lizards on current board"

		safe_lizards = 0
		for r in range(0, N):
			for c in range(0, N):
				if node.state.board[r][c] == 1:
					#print(r , ", ", c ," is safe")
					if node.state.is_square_safe(r, c):
						safe_lizards = safe_lizards + 1

		return safe_lizards


	def algorithm(self, node):
		"""Core of Simulated Annealing

		Args:
			- node (Node): current state of the board
		"""

		node = self.random_board(node)
		t = 0
		Tmax = 50

		T = Tmax
		while True:

			safe_lizards = self.num_safe_lizards(node)
			if safe_lizards == p:
				# Solution is found
				solution(node.state.board, N)
				exit()


			if T < 0.1: 
				# No solution in Time
				fail()

			successor = self.choose_successor(node)

			delta_E = (self.num_safe_lizards(successor) - safe_lizards)/p

			if delta_E > 0 or math.exp(delta_E/T) < random.random():
				node = successor

			t += 1
			T = Tmax/math.log(1+t)


def solution(board, N):
	"""Write solution to an output file

	Args:
		- board (list of list of int): positions of Lizards and trees on final board.
		- N (int): Dimensions of board

	Note:
		This function, when called, directly terminates the program.
	"""

	with open('output.txt',"w+") as out:
		out.write("OK\n")
		for i in range(0,N):
			for j in range(0,N):
				out.write(str(board[i][j]))
			out.write("\n")

	exit()


def fail():
	"""Triggered in the case of time out or no solution to board"""

	with open('output.txt',"w+") as out:
		out.write("FAIL\n")
	exit()

def handler(signum, frame):
	"""Triggered when too much time is taken to find a solution"""
	end_time = time.time()
	print("Too long....")
	print(end_time-start_time)
	fail()

	
if __name__ == '__main__':

	start_time = time.time()

	lines = tuple(open("sample_inputs/input_4.txt", 'r'))
	lines = [l.strip() for l in lines]
	print(lines)
	algorithm = lines[0]
	N = int(lines[1])
	p = int(lines[2])

	input_board = mylist()
	for i in range(0,N):
		row = mylist()
		row.extend([int(l) for l in list(lines[3+i])])
		input_board.append(row)


	node = Node(d=0, board=input_board) #node.create_state(board=input_board)
	if node.is_goal(): 
		solution(node.state.board, N)#return node
		exit()

	signal.signal(signal.SIGALRM, handler)
	signal.alarm(290)

	if algorithm.lower() == 'bfs':
		bfs = BFS()
		status = bfs.algorithm(node)

	elif algorithm.lower() == 'dfs':
		dfs = DFS()
		status = dfs.backtrack(node)
	else:
		sa = SA()
		status = sa.algorithm(node)

	if not status:
		fail()

"""
Possible Scheduling functions:
T(t) = 1/1+math.log(t)
T(t) = 2 *(1-1/(1+math.exp(-t*0.001)))
T(t) = 1/(math.log(2+t) * t*t*t)
T = 0.9*T
T = Tmax-t*0.0001
T = 1- (Tmax/(1+math.exp(-t)))
T = 1-(1/(1+t))
T = 1/1+math.log(t)
T = T-0.00001*t
T = T*0.99
"""



	
