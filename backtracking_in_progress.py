import numpy 
import random

#Создание доски судоку 9х9, заполненной нулями
sudoku = numpy.zeros((9,9),dtype=numpy.int)


#Получение координат (строка, столбец) следующей для заполения клетки
def find_empty(board):

	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j]==0:
				return (i,j) #row,column

	return None

#Генерация списка цифр 1-9 в случайном порядке, используется для уникальности заполнения
def randomline():

	line=[]
	pull=[1,2,3,4,5,6,7,8,9]

	for i in range(9):
		number=random.choice(pull)
		line.append(number)
		pull.remove(number)

	return line

#Рекурсивное заполнение. 
def backtracker(board):

	find=find_empty(board) #Базовый случай рекурсии - вся доска заполнена
	if not find:
		return True
	else:                  #Если нет - берем первую пустую клетку
		row,column=find

	for i in randomline(): #Рекурсивный случай. Заполняем случайным числом, если получаем противоречие - заполняем нулем и возвращаемся 
		if validator(board,i,(row,column)):
			board[row][column]=i

			if backtracker(board):
				return True

			board[row][column]=0

	return False


k=0 #Счетчик попыток

#Определяет можно ли ставить данную цифру num в положение pos
def validator(board,num,pos):
	global k
	k=k+1
	#print(board) <-------------------------------------------Можно смотреть процесс пошагово

	for i in range(len(board[0])): #Цифры нет в строке
		if board[pos[0]][i]==num and pos[1]!=i:
			return False

	for i in range(len(board)): #Цифры нет в столбце
		if board[i][pos[1]]==num and pos[0]!=i:
			return False

	box_x=pos[1]//3   #получение подблоков доски размером 3х3
	box_y=pos[0]//3

	for i in range(box_y*3,box_y*3+3):     #Цифры нет в подблоке
		for j in range(box_x*3,box_x*3+3):
			if board[i][j]==num and (i,j)!=pos:
				return False

	return True


#Печать с разделительными линиями

# def print_sudoku(board):

# 	for i in range(len(board)):
# 		if i%3==0 and i!=0:
# 			print("-------------------")

# 		for j in range(len(board[0])):
# 			if j%3==0 and j!=0:
# 				print("|",end="")

# 			if j==8:
# 				print(board[i][j])
# 			else:
# 				print(str(board[i][j])+" ",end="")




# print_sudoku(sudoku)
backtracker(sudoku)
print(sudoku)
print(k)