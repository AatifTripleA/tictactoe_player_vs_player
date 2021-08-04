# Tic Tac Toe

import random


class TicTacToe:

    def __init__(self, board):
        self.board = board

    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                " board='" + str(self.board) + "'"
                                               ">")

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or  # across the top
                (self.board[4] == le and self.board[5] == le and self.board[6] == le) or  # across the middle
                (self.board[1] == le and self.board[2] == le and self.board[3] == le) or  # across the bottom
                (self.board[7] == le and self.board[4] == le and self.board[1] == le) or  # down the left side
                (self.board[8] == le and self.board[5] == le and self.board[2] == le) or  # down the middle
                (self.board[9] == le and self.board[6] == le and self.board[3] == le) or  # down the right side
                (self.board[7] == le and self.board[5] == le and self.board[3] == le) or  # diagonal
                (self.board[9] == le and self.board[5] == le and self.board[1] == le))  # diagonal

    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def getPlayerMove(self, playerNum):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print('Player' + str(playerNum) + ': What is your next move? (1-9)')
            move = input()
        return int(move)

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'player2'
    else:
        return 'player1'


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('Welcome to Tic Tac Toe! This is a two player game!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    tictactoe = TicTacToe(theBoard)

    player1Letter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player1':
            # Player's turn.
            tictactoe.drawBoard()
            move = tictactoe.getPlayerMove(1)
            tictactoe.makeMove(player1Letter, move)

            if tictactoe.isWinner(player1Letter):
                tictactoe.drawBoard()
                print('Hooray! Player1 has won the game!')
                gameIsPlaying = False
            else:
                if tictactoe.isBoardFull():
                    tictactoe.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            # Player2's turn.
            tictactoe.drawBoard()
            move = tictactoe.getPlayerMove(2)
            tictactoe.makeMove(player2Letter, move)

            if tictactoe.isWinner(player2Letter):
                tictactoe.drawBoard()
                print('Hooray! Player2 has won the game!')
                gameIsPlaying = False
            else:
                if tictactoe.isBoardFull():
                    tictactoe.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not playAgain():
        break
