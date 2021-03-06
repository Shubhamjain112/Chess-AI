import math
import chessBoard as cb
from random import choice
import copy
import time


class chessCom:

	wtKing = 200
	wtQueen = 9
	wtRook = 5
	wtBishop = 3
	wtKnight = 3
	wtPawn = 1
	
	def simulateAction(self,guiBoard,inital_Pos,final_Pos):
		#print(inital_Pos)
		#print(final_Pos)
		#print()
		temp = copy.deepcopy(guiBoard.grid)
		temp[final_Pos[0]][final_Pos[1]] = temp[inital_Pos[0]][inital_Pos[1]]
		temp[inital_Pos[0]][inital_Pos[1]] = 0
		return temp

	def makeMove(self,guiBoard,color):
#		temp = [0]*8
#		for i in range(len(temp)):
#			temp[i]=guiBoard.grid[i][:]
		temp = copy.deepcopy(guiBoard.grid)
		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"
		move = [[]]
		start = time.time()
		move2 = self.ABMAX_VALUE(guiBoard,guiBoard.grid,1,color,-100000,100000)
		move4 = move2[1]
		move3 = move + move4
		print("--- %s seconds ---" % (time.time()-start)) 
		print(move3)
		return move3


	def evaluation_function(self,guiBoard,grid,color):
		mat_mobility = self.calculate_mobility_material(guiBoard,grid,color)
		fina_val = mat_mobility[0]+mat_mobility[1]
		return fina_val

## alpha beta pruning here


	def ABMIN_VALUE(self,guiBoard,grid,depth,color,a,b):
		alpha = a
		beta = b
		if depth == 0:
			return [-self.evaluation_function(guiBoard,grid,color),[]]

		ACTIONS = []  # initial position, final position
		myPieces = [] #location, value	
		temp = copy.deepcopy(grid)
		temp2 = []

		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"


		



		for r in range(len(temp)):
			for c in range(len(temp[r])):
				if temp[r][c] != 0:
					if color == guiBoard.pieces[temp[r][c]][1]:
						myPieces.append([[r,c],temp[r][c]])


		#print(myPieces)				



		for p in myPieces:
			if p[1]%6 == 1:
				ACTIONS.append(guiBoard.detPonSpaces(temp,p[0],color)[:])
			elif p[1]%6 == 2:
				ACTIONS.append(guiBoard.detKnightSpaces(temp,p[0],color)[:])
			elif p[1]%6 == 3:
				ACTIONS.append(guiBoard.detBishopSpaces(temp,p[0],color)[:])
			elif p[1]%6 == 4:
				ACTIONS.append(guiBoard.detRookSpaces(temp,p[0],color)[:])
			elif p[1]%6 == 5:
				ACTIONS.append(guiBoard.detQueenSpaces(temp,p[0],color)[:])
			else:
				ACTIONS.append(guiBoard.detKingSpaces(temp,p[0],color)[:])	

		Actions2 = [];
		print("--------")
		print(ACTIONS)
		print("-------")
		for action in ACTIONS:
			for act in action:
				if len(act) != 0 and act[1][0] >= 0 and act[1][1] >= 0 and act[1][0] < 8 and act[1][1] < 8 and guiBoard.moveValid(temp,act[0],act[1]):
					Actions2.append(act)


		bestAction = []			
		for action in Actions2:
			new_grid = self.simulateAction(guiBoard,action[0],action[1])								
			tt = self.ABMAX_VALUE(guiBoard,new_grid, depth-1 ,antiColor,alpha,beta) 
			value = tt[0]
			if value <= alpha:
				return [alpha,action]
			if value<beta:
				beta = value
				bestAction = action

		return [beta,bestAction]	


	def ABMAX_VALUE(self,guiBoard,grid,depth,color,a,b):
		alpha = a
		beta = b
		ACTIONS = []  # initial position, final position
		myPieces = [] #location, value	
		temp = copy.deepcopy(grid)


		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"

		if depth == 0:
			return [self.evaluation_function(guiBoard,grid,color),[]]


		for r in range(len(temp)):
			for c in range(len(temp[r])):
				if temp[r][c] != 0:
					if color == guiBoard.pieces[temp[r][c]][1]:
						myPieces.append([[r,c],temp[r][c]])

		for p in myPieces:
			if p[1]%6 == 1:
				ACTIONS.append(guiBoard.detPonSpaces(temp,p[0],color)[:])
			elif p[1]%6 == 2:
				ACTIONS.append(guiBoard.detKnightSpaces(temp,p[0],color)[:])
			elif p[1]%6 == 3:
				ACTIONS.append(guiBoard.detBishopSpaces(temp,p[0],color)[:])
			elif p[1]%6 == 4:
				ACTIONS.append(guiBoard.detRookSpaces(temp,p[0],color)[:])
			elif p[1]%6 == 5:
				ACTIONS.append(guiBoard.detQueenSpaces(temp,p[0],color)[:])
			else:
				ACTIONS.append(guiBoard.detKingSpaces(temp,p[0],color)[:])	

		Actions2 = [];
		print("--------")
		print(ACTIONS)
		print("-------")

		#print(ACTIONS)
		for action in ACTIONS:
			for act in action:
				if len(act) != 0 and act[1][0] >= 0 and act[1][1] >= 0 and act[1][0] < 8 and act[1][1] < 8 and guiBoard.moveValid(temp,act[0],act[1]):
					Actions2.append(act)

		#print(Actions2)
		#exit()
		bestAction = []
		for action in Actions2:
			print (action)
			new_grid = self.simulateAction(guiBoard,action[0],action[1])								
			tt = self.ABMIN_VALUE(guiBoard,new_grid,depth-1,antiColor,alpha,beta) 
			value = tt[0]
			#print(action,value)
			if value>=beta:
				return [beta,action]

			if value>alpha:
				alpha = value
				bestAction = action

		return [alpha,bestAction]	


	def calculate_mobility_material(self,guiBoard,grid,color):
		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"

		temp = copy.deepcopy(grid)
		moves = 0
		antiMoves = 0	

		material = 0
		antiMaterial = 0

		myPieces = []
		antiPieces = []

		for r in range(len(temp)):
			for c in range(len(temp[r])):
				if temp[r][c] != 0:
					if color == guiBoard.pieces[temp[r][c]][1]:
						myPieces.append([[r,c],temp[r][c]])
					else:
						antiPieces.append([[r,c],temp[r][c]])	

		#print("IN CALCULATE MOBILITY")
		#print(color)				
	#	print("myPieces",myPieces)

	#	print('n',"Antipieces",antiPieces)

		for p in myPieces:
			if p[1]%6 == 1:
				possibleMoves = guiBoard.detPonSpaces(temp,p[0],color)[:]
				moves += len(possibleMoves)
				material += self.wtPawn
			elif p[1]%6 == 2:
				possibleMoves = guiBoard.detKnightSpaces(temp,p[0],color)[:]
				moves += len(possibleMoves)
				material += self.wtKnight
			elif p[1]%6 == 3:
				possibleMoves = guiBoard.detBishopSpaces(temp,p[0],color)[:]
				moves += len(possibleMoves)
				material += self.wtBishop
			elif p[1]%6 == 4:
				possibleMoves = guiBoard.detRookSpaces(temp,p[0],color)[:]
				moves += len(possibleMoves)
				material += self.wtRook
			elif p[1]%6 == 5:
				possibleMoves = guiBoard.detQueenSpaces(temp,p[0],color)[:]
				moves += len(possibleMoves)
				material += self.wtQueen
			else:
				possibleMoves = guiBoard.detKingSpaces(temp,p[0],color)[:]
				moves += len(possibleMoves)
				material += self.wtKing

		#print(material-antiMaterial)		
		for p in antiPieces:
			if p[1]%6 == 1:
				possibleMoves = guiBoard.detPonSpaces(temp,p[0],antiColor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += self.wtPawn
			elif p[1]%6 == 2:
				possibleMoves = guiBoard.detKnightSpaces(temp,p[0],antiColor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += self.wtKnight
			elif p[1]%6 == 3:
				possibleMoves = guiBoard.detBishopSpaces(temp,p[0],antiColor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += self.wtBishop
			elif p[1]%6 == 4:
				possibleMoves = guiBoard.detRookSpaces(temp,p[0],antiColor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += self.wtRook
			elif p[1]%6 == 5:
				possibleMoves = guiBoard.detQueenSpaces(temp,p[0],antiColor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += self.wtQueen
			else:
				possibleMoves = guiBoard.detKingSpaces(temp,p[0],antiColor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += self.wtKing

		#print(moves,antiMoves)
		mobility = (moves - antiMoves)
		mat = (material - antiMaterial)
		mob_mat = [mat,mobility]
		return mob_mat

