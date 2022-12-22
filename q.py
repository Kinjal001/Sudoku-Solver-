from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
	# your code goes here
	x=pos[0]
	y=pos[1]
	z=0
	if x in range(1,4):
		if y in range(1,4):
			z=1
		if y in range(4,7):
			z=2
		if y in range(7,10):
			z=3

	if x in range(4,7):
		if y in range(1,4):
			z=4
		if y in range(4,7):
			z=5
		if y in range(7,10):	
			z=6
		
	if x in range(7,10):
		if y in range(1,4):
			z=7
		if y in range(4,7):
			z=8
		if y in range(7,10):	
			z=9

	return z
		
	

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	# your code goes here
	x=pos[0]
	y=pos[1]
	return ((x-1)%3)*3 + (y-1)%3 + 1


def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	# your code goes here
	L=[]
	if x==1 or x==2 or x==3:
		i=0
	elif x==4 or x==5 or x==6:
		i=3
	elif x==7 or x==8 or x==9:
		i=6	
	
	if x%3==1:
		for k in range(i,i+3):
			for j in range(0,3):
				L.append(sudoku[k][j])
	elif x%3==2:
		for k in range(i,i+3):
			for j in range(3,6):
				L.append(sudoku[k][j])
	elif x%3==0:
		for k in range(i,i+3):
			for j in range(6,9):
				L.append(sudoku[k][j])
				
	return L

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	# your code goes here
	return sudoku[i-1]
	

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	# your code goes here
	L=[]
	for i in range(9):
		L.append(sudoku[i][x-1])

	return L

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	# your code goes here
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				return (i+1,j+1)
	
	return (-1, -1)

def valid_list(lst: List[int])-> bool:
	"""This function takes a lists as an input and returns true if the given list is valid. 
	The list will be a single block , single row or single column only. 
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	# your code goes here
	L=[]
	q=0
	if len(lst)==9:
		for i in lst:
			if i in range(0,10):
				if i!=0:
					L.append(lst.count(i))
			else:
				q=1
				break
		if (L==[1]*len(L) or lst==[0]*9) and q!=1:
				return True
	return False

def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""This function returns True if the whole Sudoku is valid.
	"""
	# your code goes here
	x,y,z=[],[],[]	
	for i in range(9):
		a=get_row(sudoku,i+1)
		x.append(valid_list(a))
	
	for i in range(9):
		b=get_column(sudoku,i+1)
		y.append(valid_list(b))
	
	for i in range(9):
		c=get_block(sudoku,i+1)
		z.append(valid_list(c))
	
	if x==y==z==[True]*9:
		return True
		
	return False

def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	# your code goes here
	x,y=pos[0],pos[1]
	L=[1,2,3,4,5,6,7,8,9]
	for i in get_row(sudoku, x):
		if i in L:
			L.remove(i)
	for i in get_column(sudoku, y):
		if i in L:
			L.remove(i)
	for i in get_block(sudoku, get_block_num(sudoku, pos)):
		if i in L:
			L.remove(i)
	return L

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""
	# your code goes here
	x,y=pos[0],pos[1]
	sudoku[x-1][y-1]=num
	
	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	# your code goes here
	x,y=pos[0],pos[1]
	sudoku[x-1][y-1]=0

	return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
	""" This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns 
	true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
	It return them in a tuple i.e. `(True, solved_sudoku)`.

	However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
	"""
	# your code goes here

	# to complete this function, you may define any number of helper functions.
	# However, we would be only calling this function to check correctness.
	
	
	first_un = find_first_unassigned_position(sudoku)
	if (first_un[0]==-1):
		return (valid_sudoku(sudoku), sudoku)

	l = get_candidates(sudoku, first_un)

	for i in l:
		newSud = make_move(sudoku, first_un, i)
		cor, corsud = sudoku_solver(newSud)
		if cor:
			return (cor, corsud)
		sudoku = undo_move(sudoku, first_un)

	return (False, sudoku)
	
# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.'''

def in_lab_component(sudoku: List[List[int]]):
	print("Testcases for In Lab evaluation")
	print("Get Block Number:")
	print(get_block_num(sudoku,(4,4)))
	print(get_block_num(sudoku,(7,2)))
	print(get_block_num(sudoku,(2,6)))
	print("Get Block:")
	print(get_block(sudoku,3))
	print(get_block(sudoku,5))
	print(get_block(sudoku,9))
	print("Get Row:")
	print(get_row(sudoku,3))
	print(get_row(sudoku,5))
	print(get_row(sudoku,9))

# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()
	# print(get_block(sudoku, 3))
	# Try to solve the sudoku
	possible, sudoku = sudoku_solver(sudoku)

	# The following line is for the in-lab component
	'''in_lab_component(sudoku)'''
	# Show the result of the same to your TA to get your code evaulated

	# Check if it could be solved
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)



