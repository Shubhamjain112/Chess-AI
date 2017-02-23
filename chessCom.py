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
		move2 = self.MINIMAX_DECISION(guiBoard,color)
		move3 = move + move2
		print("--- %s seconds ---" % (time.time()-start)) 
		print(move3)
		return move3


	def evaluation_function(self,guiBoard,grid,color):
		mat_mobility = self.calculate_mobility_material(guiBoard,grid,color)
		fina_val = mat_mobility[0]+mat_mobility[1]
		return fina_val


	def MINIMAX_DECISION(self,guiBoard,color):

		temp = copy.deepcopy(guiBoard.grid)
		maxValue = -10000
		ACTIONS = []   # inital Position, Final Position
		myPieces = []  # location, value

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
				ACTIONS.append(guiBoard.detBishopSpaces(temp,p[0],antiColor)[:])
			elif p[1]%6 == 4:
				ACTIONS.append(guiBoard.detRookSpaces(temp,p[0],antiColor)[:])
			elif p[1]%6 == 5:
				ACTIONS.append(guiBoard.detQueenSpaces(temp,p[0],antiColor)[:])
			else:
				ACTIONS.append(guiBoard.detKingSpaces(temp,p[0],color)[:])

		Actions2 = [];
		for action in ACTIONS:
			for act in action:
				if len(act) != 0 and act[1][0] >= 0 and act[1][1] >= 0 and act[1][0] < 8 and act[1][1] < 8:
					Actions2.append(act)

		
				

		for action in Actions2:
			initial = action[0]
			final = action[1]
			new_grid = self.simulateAction(guiBoard,initial,final)								
			value = self.MIN_VALUE(guiBoard,new_grid,3,antiColor) 
			if value > maxValue:
				value = maxValue
				bestAction = action

		return bestAction		

	def MIN_VALUE(self,guiBoard,grid,depth,color):
		if depth == 0:
			#print("here")
			return self.evaluation_function(guiBoard,grid,color)



		minValue = 10000
		ACTIONS = []  # initial position, final position
		myPieces = [] #location, value	
		temp = copy.deepcopy(grid)
		temp2 = []

		#print("IN MIN")
		#print(depth)



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
		for action in ACTIONS:
			for act in action:
				if len(act) != 0 and act[1][0] >= 0 and act[1][1] >= 0 and act[1][0] < 8 and act[1][1] < 8:
					Actions2.append(act)
		

		bestAction = []			
		for action in Actions2:
			new_grid = self.simulateAction(guiBoard,action[0],action[1])								
			value = self.MAX_VALUE(guiBoard,new_grid, depth-1 ,antiColor) 
			if value < minValue:
				minValue = value 

		return minValue	


	def MAX_VALUE(self,guiBoard,grid,depth,color):
		if depth == 0:
			return self.evaluation_function(guiBoard,grid,color)

		maxValue = -10000
		ACTIONS = []  # initial position, final position
		myPieces = [] #location, value	
		temp = copy.deepcopy(grid)

		#print("IN MAX")

		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"

		for r in range(len(temp)):
			for c in range(len(temp[r])):
				if temp[r][c] != 0:
					if color == guiBoard.pieces[temp[r][c]][1]:
						myPieces.append([[r,c],temp[r][c]])

		
		#print(depth)
		


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
		for action in ACTIONS:
			for act in action:
				if len(act) != 0 and act[1][0] >= 0 and act[1][1] >= 0 and act[1][0] < 8 and act[1][1] < 8:
					Actions2.append(act)

		#print(len(Actions2))

		for action in Actions2:
			#print (action)
			new_grid = self.simulateAction(guiBoard,action[0],action[1])								
			value = self.MIN_VALUE(guiBoard,new_grid,depth-1, antiColor) 
			if value > maxValue:
				maxValue = value

		return maxValue							

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

		mobility = moves - antiMoves
		mat = material - antiMaterial
		mob_mat = [mat,mobility]
		return mob_mat

