import numpy as np,random


sudoku = np.zeros((9,9),dtype=np.int)
pull=[1,2,3,4,5,6,7,8,9]

# sudoku=np.array([[1,5,7,8,3,2,4,6,9],[3,9,6,7,4,5,2,8,1],[2,8,4,1,9,6,7,3,5],[6,7,2,9,8,4,5,1,3],[8,3,1,2,5,7,6,9,4],[5,4,9,6,1,3,8,7,2],[7,6,3,4,2,9,1,5,8],[4,1,5,3,7,8,9,2,6],[9,2,8,5,6,1,3,4,7]])

def helper(x,y,b):
	sudokupart=0
	if 0<=x<=2 and 0<=y<=2:
		sudokupart=b[0:3,0:3]
	if 3<=x<=5 and 0<=y<=2:
		sudokupart=b[3:6,0:3]
	if 6<=x<=9 and 0<=y<=2:
		sudokupart=b[6:10,0:3]
	if 0<=x<=2 and 3<=y<=5:
		sudokupart=b[0:3,3:6]
	if 3<=x<=5 and 3<=y<=5:
		sudokupart=b[3:6,3:6]
	if 6<=x<=9 and 3<=y<=5:
		sudokupart=b[6:10,3:6]
	if 0<=x<=2 and 6<=y<=9:
		sudokupart=b[0:3,6:10]
	if 3<=x<=5 and 6<=y<=9:
		sudokupart=b[3:6,6:10]
	if 6<=x<=9 and 6<=y<=9:
		sudokupart=b[6:10,6:10]
	return(sudokupart.reshape(1,9))

def RowConverter(row,table):
	line=[]
	for i in range(9):
		line.append(table[row,i])

	return line
def ColumnConverter(column,table):
	line=[]
	for i in range(9):
		line.append(table[i,column])
	return line



def RowChecker(row,table):
	flag=False
	if sorted(table[row,:]) == pull:
		flag=True
	return flag
def ColumnChecker(column,table):
	flag=False
	if ColumnConverter(column,table) == pull:
		flag=True
	return flag

def BlockChecker(x,y,table):
	flag=False
	line=helper(x,y,table)[0,:]
	if sorted(line) == pull:
		flag=True
	return flag

def Validator(table):
	flag=False
	k=0
	for i in range(9):
		for j in range(9):
			if BlockChecker(i,j,table)==True and RowChecker(i,table)==True and ColumnChecker(j,table)==True:
				k=k+1
	if k==81:
		flag=True
	return flag

def Checker(x,y,table):
	allowed=[]
	row=RowConverter(x,table)
	column=ColumnConverter(y,table)
	block=helper(x,y,table)[0,:]
	if len(allowed)==0:
		allowed.append(random.randint(1,9))

	for i in pull:
		if i not in row and i not in column and i not in block and i not in allowed:
			allowed.append(i)
	

	return allowed	
k=0


# print(sudoku)
# print(RowConverter(0,sudoku))
# print(ColumnConverter(0,sudoku))
# print(3 in RowConverter(0,sudoku))

print(Checker(0,0,sudoku))

while True:
	for i in range(9):
		for j in range(9):
			sudoku[i,j]=random.choice(Checker(i,j,sudoku))
	if Validator(sudoku)==True:
		print(sudoku)
		break
	else:
		k+=1
	print(k)
	if k>100:
		break



	