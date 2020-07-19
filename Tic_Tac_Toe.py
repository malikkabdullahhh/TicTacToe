# get off my ass bruh!




#GAME DESCRIPTION
print("                       <<<<<<<<<>>>>>>>>>")
print("                          TIC-TAC-TOE")
print("                       <<<<<<<<<>>>>>>>>>")	

#INSTRUCTIONS
print("                  Let me first show y'all the mapping of the board.")
print(" ")
print("                               "+"1"+"|"+"2"+"|"+"3")
print("                               "+"=====")
print("                               "+"4"+"|"+"5"+"|"+"6")
print("                               "+"=====")
print("                               "+"7"+"|"+"8"+"|"+"9")
print(" ")
print("                  Both players are expected to choose their ")
print("                  moves according to the mapping or have to ")
print("                        play all over again. GOOD LUCK!")
print(" ")

#INPUT ITERABLES 
xno=["none","X","O","X","O","X","O","X","O","X"]
onx=["none","O","X","O","X","O","X","O","X","O"]
empty_board=["none"," "," "," "," "," "," "," "," "," "]
limit=[1,2,3,4,5,6,7,8,9]

#TIC-TAC-TOE BOARD
def board():
	print("                               "+empty_board[1]+"|"+empty_board[2]+"|"+empty_board[3])
	print("                               "+"=====")
	print("                               "+empty_board[4]+"|"+empty_board[5]+"|"+empty_board[6])
	print("                               "+"=====")
	print("                               "+empty_board[7]+"|"+empty_board[8]+"|"+empty_board[9])

#GAME FUNCTION
def game():
	player1=""
	while player1!="X" and player1!="O":
		player1=input("                  Player-1, Either choose X or O: ").upper()
    
    
	if player1 == "X":
		print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*"+"\n                  Player-1: X , Player-2: O\n"+"                  *-*-*-*-*-*-*-*-*-*-*-*-*-*")  #decorations
		
        #WINNER CHECK
		for i in xno[1:]:
			
			if empty_board[3]==empty_board[6]==empty_board[9]=="X":
				print("                  Player-1 Wins!")
				break 
			if empty_board[3]==empty_board[6]==empty_board[9]=="O":
				print("                  Player-2 Wins!")
				break
			if empty_board[7]==empty_board[5]==empty_board[3]=="X":
				print("                  Player-1 Wins!")
				break
			if empty_board[7]==empty_board[5]==empty_board[3]=="O":
				print("                  Player-2 Wins!")
				break
			if empty_board[4]==empty_board[5]==empty_board[6]=="X":
				print("                  Player-1 Wins!")
				break
			if empty_board[4]==empty_board[5]==empty_board[6]=="O":
				print("                  Player-2 Wins!")
				break
			if empty_board[1]==empty_board[2]==empty_board[3]=="X":
				print("                  Player-1 Wins!")
				break
			if empty_board[1]==empty_board[2]==empty_board[3]=="O":
				print("                  Player-2 Wins!")
				break
			if empty_board[2]==empty_board[5]==empty_board[8]=="X":
				print("                  Player-1 Wins!")
				break
			if empty_board[2]==empty_board[5]==empty_board[8]=="O":
				print("                  Player-2 Wins!")
				break
			if empty_board[7]==empty_board[8]==empty_board[9]=="X":
				print("                  Player-1 Wins!")
				break
			if empty_board[7]==empty_board[8]==empty_board[9]=="O":
				print("                  Player-2 Wins!")
				break
			if empty_board[1]==empty_board[4]==empty_board[7]=="X":
				print("                  Player-1 Wins!")
				break
			if empty_board[1]==empty_board[4]==empty_board[7]=="O":
				print("                  Player-2 Wins!")
				break
			if empty_board[1]==empty_board[5]==empty_board[9]=="X":
				print("                  Player-1 Wins!")
				break
			if empty_board[1]==empty_board[5]==empty_board[9]=="O":
				print("                  Player-2 Wins!")
				break

			#PLAYER-1's MOVE	
			if (xno[1:].index(i))%2==0:
				ata=0
				while ata<1:
					try:
						move=int(input("                  Choose your move, Player-1 :- "))
					except:
						print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
						print("                  YOU CAN'T INPUT ANYTHING EXCEPT 1,2,3,4,5,6,7,8,9 SORRY")
						print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
						print(" ")
					if empty_board[move]==" ":
						empty_board[move]=i
						ata=2
					print("\n"*100)
					board()
					print("\n"*3)
					

			#PLAYER-2's MOVE	
			else:
				iti=0
				while iti<1:
					try:
						move=int(input("                  Choose your move, Player-2 :- "))
					except:
						print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
						print("                  YOU CAN'T INPUT ANYTHING EXCEPT 1,2,3,4,5,6,7,8,9 SORRY")
						print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
						print(" ")
					if empty_board[move]==" ":
						empty_board[move]=i
						iti=2
					print("\n"*100)
					board()
					print("\n"*3)
					

	elif player1=="O":
		print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*"+"\n                  Player-1: O , Player-2: X\n"+"                  *-*-*-*-*-*-*-*-*-*-*-*-*-*")

		#WINNER CHECK
		for i in onx[1:]:
			

			if empty_board[3]==empty_board[6]==empty_board[9]=="X":
				print("                  Player-2 Wins!")
				break 
			if empty_board[3]==empty_board[6]==empty_board[9]=="O":
				print("                  Player-1 Wins!")
				break
			if empty_board[7]==empty_board[5]==empty_board[3]=="X":
				print("                  Player-2 Wins!")
				break
			if empty_board[7]==empty_board[5]==empty_board[3]=="O":
				print("                  Player-1 Wins!")
				break
			if empty_board[4]==empty_board[5]==empty_board[6]=="X":
				print("                  Player-2 Wins!")
				break
			if empty_board[4]==empty_board[5]==empty_board[6]=="O":
				print("                  Player-1 Wins!")
				break
			if empty_board[1]==empty_board[2]==empty_board[3]=="X":
				print("                  Player-2 Wins!")
				break
			if empty_board[1]==empty_board[2]==empty_board[3]=="O":
				print("                  Player-1 Wins!")
				break
			if empty_board[2]==empty_board[5]==empty_board[8]=="X":
				print("                  Player-2 Wins!")
				break
			if empty_board[2]==empty_board[5]==empty_board[8]=="O":
				print("                  Player-1 Wins!")
				break
			if empty_board[7]==empty_board[8]==empty_board[9]=="X":
				print("                  Player-2 Wins!")
				break
			if empty_board[7]==empty_board[8]==empty_board[9]=="O":
				print("                  Player-1 Wins!")
				break
			if empty_board[1]==empty_board[4]==empty_board[7]=="X":
				print("                  Player-2 Wins!")
				break
			if empty_board[1]==empty_board[4]==empty_board[7]=="O":
				print("                  Player-1 Wins!")
				break
			if empty_board[1]==empty_board[5]==empty_board[9]=="X":
				print("                  Player-2 Wins!")
				break
			if empty_board[1]==empty_board[5]==empty_board[9]=="O":
				print("                  Player-1 Wins!")
				break

			#PLAYER-1's MOVE
			if (onx[1:].index(i))%2==0:
				bata=0
				while bata<1:
					try:
						move=int(input("                  Choose your move, Player-1 :- "))
					except:
						print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
						print("                  YOU CAN'T INPUT ANYTHING EXCEPT 1,2,3,4,5,6,7,8,9 SORRY")
						print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
						print(" ")
					if empty_board[move]==" ":
						empty_board[move]=i
						bata=2
					print("\n"*100)
					board()
					print("\n"*3)
					

			#PLAYER-2's MOVE	
			else:
				lata=0
				while lata<1:
					try:
						move=int(input("                  Choose your move, Player-2 :- "))
					except:
						print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
						print("                  YOU CAN'T INPUT ANYTHING EXCEPT 1,2,3,4,5,6,7,8,9 SORRY")
						print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
						print(" ")
					if empty_board[move]==" ":
						empty_board[move]=i
					print("\n"*100)
					board()
					print("\n"*3)
					

 

#REAL TALK 		
game()
print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*")

#IN CASE THEY WANNA REPLAY !
replay=""
while replay!="yes" and replay !="no":
	empty_board=["none"," "," "," "," "," "," "," "," "," "]
	replay=input("                  Do you want to play again? (yes/no) ")
	if replay=="yes":
		print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*")
		print("                  Welcome back fellas !")
		print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*")
		game()
		replay=""
	elif replay=="no":
		print("                  *-*-*-*-*-*-*-*-*-*-*-*-*-*")
		break



