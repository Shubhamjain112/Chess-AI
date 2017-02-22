import math
import chessBoard as cb
from random import choice
import copy

class chessCom:

	wtKing = 200
	wtQueen = 9
	wtRook = 5
	wtBishop = 3
	wtKnight = 3
	wtPawn = 1
	
	def simulateAction(guiBoard,action1,action2):
		temp = copy.deepcopy(guiBoard.grid)
		temp[acion2[0]][action2[1]] = temp[action1[0]][action1[1]]
		temp[acion1[0]][action1[1]] = 0
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
		move = []
		move2 = self.MINIMAX_DECISION(guiBoard,color)
		move3 = move + move2 
		return move3


	def evaluation_function(self,board,color):
		mat_mobility = calculate_mobility_material(board,color)
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
				Actions2.append(act)

		print(Actions2)
				

		for action in ACTIONS:
			print (action)
			new_state = self.simulateAction(guiBoard,action[0][0],action[0][1])								
			value = MIN_VALUE(new_state,4,antiColor) 
			if value > maxValue:
				value = maxValue
				bestAction = action

		return bestAction		

	def MIN_VALUE(self,board,depth,color):
		minValue = 10000
		ACTIONS = []  # initial position, final position
		myPieces = [] #location, value	

		if depth == 0:
			return evaluation_function(board,color)

		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"


		for r in range(len(temp)):
			for c in range(len(temp[r])):
				if temp[r][c] != 0:
					if color == guiBoard.pieces[temp[r][c]][1]:
						myPieces.append([[r,c],temp[r][c]])

		for p in self.myPieces:
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

		for action in ACTIONS:
			new_state = simulateAction(guiBoard,action[0][0],action[0][1])								
			value = MAX_VALUE(new_state,depth,antiColor) 
			if value < minValue:
				minValue = value
				bestAction = action
		return bestAction	


	def MAX_VALUE(self,board, depth,color):
		maxValue = -10000
		ACTIONS = []  # initial position, final position
		myPieces = [] #location, value	

		if depth == 0:
			return evaluation_function(board,color)

		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"

		for r in range(len(temp)):
			for c in range(len(temp[r])):
				if temp[r][c] != 0:
					if color == guiBoard.pieces[temp[r][c]][1]:
						myPieces.append([[r,c],temp[r][c]])

		for p in self.myPieces:
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

		for action in ACTIONS:
			print (action)
			new_state = simulateAction(guiBoard,action[0][0],action[0][1])								
			value = MIN_VALUE(new_state,depth-1,antiColor) 
			if value > maxValue:
				maxValue = value
				bestAction = action
		return bestAction								

	def calculate_mobility_material(self,temp,color, guiBoard):
		if color == "Black":
			antiColor = "White"
		else:
			antiColor = "Black"

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
				possibleMoves = guiBoard.detPonSpaces(temp,p[0],anticolor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += wtPawn
			elif p[1]%6 == 2:
				possibleMoves = guiBoard.detKnightSpaces(temp,p[0],anticolor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += wtKnight
			elif p[1]%6 == 3:
				possibleMoves = guiBoard.detBishopSpaces(temp,p[0],anticolor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += wtBishop
			elif p[1]%6 == 4:
				possibleMoves = guiBoard.detRookSpaces(temp,p[0],anticolor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += wtRook
			elif p[1]%6 == 5:
				possibleMoves = guiBoard.detQueenSpaces(temp,p[0],anticolor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += wtQueen
			else:
				possibleMoves = guiBoard.detKingSpaces(temp,p[0],anticolor)[:]
				antiMoves += len(possibleMoves)
				antiMaterial += wtKing

		mobility = moves - antiMoves
		mat = material - antiMaterial
		mob_mat = [mat,mobility]
		return mob_mat

