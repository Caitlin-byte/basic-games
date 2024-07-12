
print("Welcome to our final project!")
#imports
import random
from time import sleep
import urllib.request
import numpy as np

game = 0
while game != 4: #while they don't want to exit
    print('- - - - - - - - - - ') #formatting
    print("MAIN MENU:")
    while game != 1 and game != 2 and game != 3 and game != 4:
        try:
            game = int(input(("Would you like to play \n1. Rock Paper Scissors\n2. Tic Tac Toe\n3. Hangman\n4. Exit the code\n")))
        except:
            print("Invalid input. Please enter 1, 2, 3, or 4\n")
    if game != 4:
        if game == 1:
            
            print("Rock Paper Scissors")
            print("Purpose: to pick the item that beats your opponent’s item")
            print('- - - - - - - - - - ') #formatting
            print("Instructions:")
            print('Each round, select rock, paper or scissors by inputting r, p or s.')
            print('Rock beats scissors, paper beats rock, and scissors beats paper.')
            print('If both pick the same item, the round will result in a tie.')
            print('Once the round is over, the result will be printed, and you will be given the option to play again.')
            
            score = {'comp': 0, 'user': 0}
            options = ['r', 'p', 's']
            again = True
            while again:
                comp = options[random.randrange(3)]
                print('- - - - - - - - - - ') #formatting
                user = input("Select rock, paper or scissors by inputting r, p, or s respectively: ")
                while user != 'r' and user != 's' and user != 'p':
                    user = input("\nInvalid input.\nPlease input r, p, or s: ")
                #if they're the same it's a tie
                if user == comp:
                    result = 'tie'
                #output your choice and determine the result
                if user == 'r':
                    print('You chose rock')
                    if comp == 'p':
                        result = 'comp'
                    elif comp == 's':
                        result = 'user'
                elif user == 'p':
                    print('You chose paper')
                    if comp == 'r':
                        result = 'user'
                    elif comp == 's':
                        result = 'comp'
                elif user == 's':
                    print('You chose scissors')
                    if comp == 'r':
                       result = 'comp'
                    elif comp == 'p':
                        result = 'user'
                #output what the comuter chose
                if comp == 'r':
                    print("The computer chose rock")
                elif comp == 'p':
                    print("The computer chose paper")
                elif comp == 's':
                    print("The computer chose scissors")
                print("")#formatting
                #output the result
                if result == 'tie':
                    print("The game resulted in a tie.")
                elif result == 'user':
                    print("You won!")
                    score['user'] += 1
                elif result == 'comp':
                    print("The computer won")
                    score['comp'] += 1
                sleep(2) #this is the new thing i learned
                print('- - - - - - - - - - ') #formatting
                #keep going or no?
                keep_playing = ''
                while keep_playing != 1 and keep_playing != 2:
                    try:
                        keep_playing = int(input("Would you like to:\n1. Play another round\nor\n2. Return to main menu\nEnter 1 or 2: "))
                    except:
                        print("Invalid input. Please enter 1 or 2")
                if keep_playing == 2:
                    again = False
            print('- - - - - - - - - - ') #formatting
            print("Thank you for playing!")
            print(f'The final score is:\nUser: {score["user"]}\nComputer: {score["comp"]}')
        elif game == 2:
            def tictac():
                #making board indexes
                board_line = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                layout = np.array(board_line)
                layout = layout.reshape((3, 3))
                
                def show(mat):
                    for i in range(3):
                        for j in range(3):
                            print(mat[i][j], end = ' ')
                        print()
                
                win = False
                piece = 'a'
                print("Welcome to TicTacToe")
                print("Purpose: to get three of your piece in a row (horizontally, vertically or diagonally)")
                print('- - - - - - - - - - ') #formatting
                print("Instructions:")
                print('This is a two player game.')
                print('Each round, the current state of the board will be shown.')
                print('Then the current player will choose where to place their piece by entering a number that corresponds to the board layout:')
                show(layout)
                print('You must chose an empty spot.')
                print("Then, the next player goes.")
                print("Players will continue taking turns until someone gets 3 in a row or the board is full.")
                print('Once the round is over, the result will be printed, and you will be given the option to play again.')
                print('- - - - - - - - - - ') #formatting
                while piece != 'X' and piece != 'O':
                    piece = input("Player 1, are you X's or O's? ")
                    try:
                        piece = piece.upper()
                        #this is something we were not taught in class that I used in my code
                    except:
                        continue
                        
                    if piece != 'X' and piece != 'O':
                        print("Please enter x or o.")
                
                #making playing board
                board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
                board = np.array(board)
                board = board.reshape((3, 3))

                def show(mat):
                    for i in range(3):
                        for j in range(3):
                            print(mat[i][j], end = ' ')
                        print()
                #switch chosen piee so the switching each turn works
                
                if piece == 'X':
                    piece = 'O'
                else:
                    piece = 'X'
                    
                while(not win and '-' in board):
                    #assign the piece and announce that
                    if piece == 'X':
                        piece = 'O'
                        print('- - - - - - - - - - ') #formatting
                        print("O's turn")
                    else:
                        piece = 'X'
                        print('') #formatting
                        print("X's turn")
                    #show the layout
                    print("Board Layout: ")
                    show(layout)
                    
                    #show the current board
                    print("Current Board: ")
                    show(board)
                    print()
                    
                    #pick where you want to go

                    loc = 0
                    valid = False
                    while not valid:
                        while loc > 9  or loc < 1:
                            try:
                                loc = int(input(f"{piece}, Where would you like to place your piece? "))
                                if loc > 9 or loc < 1:
                                    print("Please enter a number between 1 and 9")
                            except:
                                print("Please enter a number between 1 and 9")
                            
                        for i in range(3):
                            for j in range(3):
                                if layout[i][j] == loc:
                                    if board[i][j] != '-':
                                        print("This spot is taken, try again.")
                                        loc = 0
                                    else:
                                        board[i][j] = piece
                                        valid = True
                    #check for win
                    if '-' not in board:
                        print('- - - - - - - - - - ') #formatting
                        print("Game Over. The board is full.")
                        print("Final Board: ")
                        show(board)
                
                    #check for wins
                    rwin = False
                    cwin = False
                    for i in range(3):
                        if(board[i][0]==board[i][1]==board[i][2]==piece):
                            rwin= True
                    for j in range(3):
                        if(board[0][j]==board[1][j]==board[2][j]==piece):
                            cwin=True
                    ldig = False
                    rdig = False
                    if(board[0][0]==board[1][1]==board[2][2]==piece):
                        ldig = True
                    if(board[0][2]==board[1][1]==board[2][0]==piece):
                        rdig = True
                    
                    win  = rdig or ldig or rwin or cwin
                if(win):
                    print('- - - - - - - - - - ') #formatting
                    print("Game Over.")
                    print(piece, "has won!")
                again = input("Would you still like to play?\nType yes if so. \nIf not, you will be redirected to the main menu!\n")
                while again == "Yes" or again == 'yes':
                    tictac()
                    again = input("Would you still like to play? If not, you will be redirected to the main menu! Yes or No: ")
                            
            tictac()
                
        elif game == 3:
            # Instructions 
            def instructions(): 
                '''Welcome to the game hangman! 
                The purpose of the game is to guess a random generated word 
                You will have 10 lives at the start of the game
                You must guess all lowercase letters by inputting them
                If the letter is in the word it will be displayed in the correct spot 
                If the letter is wrong you lose a life! 
                10 wrong guesses and the game ends.'''
                return None
            
            help(instructions)
            
            url = "https://www.mit.edu/~ecprice/wordlist.10000"
            response = urllib.request.urlopen(url)
            website_list = response.read().decode()
            words= []
            for word in website_list.splitlines():
                if len(word)==5:
                    words.append(word)
                    if len(words)==100:
                        break
                    
            # select a random word from the list
            secret_word = random.choice(words)
            
            # function to display the board to show the progress of the player  
            def print_board(word, guessed_letters):
                '''Print the current state of the board'''
                display_word = ''.join([letter if letter in guessed_letters else ' _ ' for letter in word])
                print(display_word)
            
            # to show the actual progress through the game 
            def update_board(word, guessed_letter, guessed_letters):
                '''Update the board based on the guessed letter'''
                guessed_letters.add(guessed_letter)
                if guessed_letter not in word:
                    return False  # Guessed letter is incorrect
                return True  # Guessed letter is correct
            
            # main gameplay function
            def main():
                # Initialize game variables
                lives = 10
                guessed_letters = set()
            
                print("Welcome to Hangman!")
                print_board(secret_word, guessed_letters)
            
                while lives > 0:
                    guess = input("Guess a letter: ").lower()
                    if guess.isalpha() and len(guess) == 1:
            
                    # Check if the letter has already been guessed
                        if guess in guessed_letters:
                            print("You've already guessed that letter. Try again.")
                            continue
                
                        # Update the board and check if the guess is correct
                        correct_guess = update_board(secret_word, guess, guessed_letters)
                
                        if correct_guess:
                            print("Correct!")
                        else:
                            lives -= 1
                            print("Incorrect! Lives remaining:", lives)
                
                        # Print the current state of the board
                        print_board(secret_word, guessed_letters)
                    else:
                        print("Invalid guess.")
            
                    # Check if the player has guessed all the letters
                    if set(secret_word) <= guessed_letters:
                        print("Congratulations! You guessed the word:", secret_word)
                        break
            
                # Game over
                if lives == 0:
                    print("Game over! The word was:", secret_word)
            again = True
            while again:
                main()
                keep_playing = ''
                while keep_playing != 1 and keep_playing != 2:
                    try:
                        keep_playing = int(input("Would you like to:\n1. Play another round\nor\n2. Return to main menu\nEnter 1 or 2: "))
                    except:
                        print("Invalid input. Please enter 1 or 2")
                if keep_playing == 2:
                    again = False
            print('- - - - - - - - - - ') #formatting
                #keep going or no?
            
            print('- - - - - - - - - - ') #formatting
            print("Thank you for playing!")

        game = 0


