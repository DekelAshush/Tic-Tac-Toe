from IPython.core.display_functions import clear_output

def display_game(game_list):
  print("Here is the current list:")
  print(game_list)

def position_choice():
    acceptable_range = range(0,9)
    choice = ""
    within_range=False

    while not choice.isdigit() or within_range==False:
        choice = input("Choose an index position(0-8): ")
        if not choice.isdigit():
            print("Sorry that is not a number!")
        else:
            if int(choice) in acceptable_range:
                within_range= True
            else:
                print("Sorry, you are out of acceptable range (0-8)")
    return int(choice)

def gameon_choice():
    choice = ""
    while choice not in['Y','N']:
        choice = input("Keep Playing? (Y or N)")
        if choice not in['Y','N']:
            print("Sorry wrong input,Please choose Y or N")
    if choice=="Y":
        return True
    else:
        return False

def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at position: ")
    game_list[position]= user_placement
    return game_list

def display_board(board):
        clear_output(board)
        print("Here is the current board:")
        print(board[0] + '|' +board[1] + '|'+ board[2])
        print(board[3] + '|' +board[4] + '|'+ board[5])
        print(board[6] + '|' +board[7] + '|'+ board[8])

def player_input():
    choice = ""
    while choice!='X' and choice!='O':
        choice = input("Player 1, choose X or O: ")

    player1= choice
    if player1=='X':
        player2='O'
    else:
        player2 = 'X'
    return player1,player2

def win(board,player_choice):
    for i in range(0,len(board),3):
        if board[i]==board[i+1]==board[i+2]==player_choice:
            return True

    for i in range(0,3):
        if board[i]==board[i+3]==board[i+6]==player_choice:
            return True

    if board[0]==board[4]==board[8]==player_choice:
        return True

    if board[2]==board[4]==board[6]==player_choice:
        return True
    return False


def start_game():
    print("Welcome to Tic TAC TOE")
    game_on=True
    test_board=['']*9
    already_taken=[]

    while game_on:
        tie=0
        display_board(test_board)
        player1_choice,player2_choice = player_input()
        end_game=False
        while not end_game:
            draw_board(player1_choice,test_board,already_taken)

            if win(test_board,player1_choice):
                print("Congratulation player1 Wins")
                if gameon_choice():
                    tie=0
                    test_board=['']*9
                    already_taken=[]
                else:
                    game_on=False
                    break
            tie+=1
            if tie==10:
                print("Its A Tie!")
                if gameon_choice():
                    tie=0
                    test_board=['']*9
                    already_taken=[]
                else:
                    game_on=False

            draw_board(player2_choice,test_board,already_taken)

            if win(test_board,player2_choice):
                    print("Congratulation player2 Wins")
                    if gameon_choice():
                        tie=0
                        test_board=['']*9
                        already_taken=[]
                    else:
                        game_on=False

            tie+=1
            if tie==10:
                print("Its A Tie!")
                if gameon_choice():
                    tie=0
                    test_board=['']*9
                    already_taken=[]
                else:
                    game_on=False


def draw_board(player_choice,test_board,already_taken):

    move=position_choice()
    while move in already_taken:
        print("Spot Already Taken, Please enter new value: ")
        move=position_choice()
    already_taken.append(move)
    test_board[move] = player_choice
    display_board(test_board)


start_game()



