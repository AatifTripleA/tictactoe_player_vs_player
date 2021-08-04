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
    return ['X', 'O']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return p2Name
    else:
        return p1Name


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('Welcome to Tic Tac Toe! This is a two player game!')
instructions = input('Would you like to view the game\'s instructions?')
if instructions.startswith('y'):
    print('''The goal of Tic Tac Toe is to make an uninterrupted line from your chosen letter (x or o). 
    This line can be vertical, horizontal, or diagonal.\nDoing that wins you the round. 
    If you win 5 rounds before your partner, you win the game.\nA tie is possible in a round, but not in the overall game.\n
    The board is set up like a keypad. The bottom row counts 1-3 from left to right, middle row 4-6, and top row 7-9.''')

player_one_wins = 0
player_two_wins = 0

p1Name = input('Who will play x?')
p2Name = input('Who will play o?')

while player_one_wins < 5 and player_two_wins < 5:
    # Reset the board
    theBoard = [' '] * 10
    tictactoe = TicTacToe(theBoard)
    print(p1Name + ' has won ' + str(player_one_wins) + ' rounds.')
    print(p2Name + ' has won ' + str(player_two_wins) + ' rounds.')

    player1Letter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(str(turn) + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == p1Name:
            # Player's turn.
            tictactoe.drawBoard()
            move = tictactoe.getPlayerMove(1)
            tictactoe.makeMove(player1Letter, move)

            if tictactoe.isWinner(player1Letter):
                tictactoe.drawBoard()
                print('Hooray! ' + p1Name +'has won the game!')
                player_one_wins += 1
                gameIsPlaying = False
            else:
                if tictactoe.isBoardFull():
                    tictactoe.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = p2Name

        else:
            # Player2's turn.
            tictactoe.drawBoard()
            move = tictactoe.getPlayerMove(2)
            tictactoe.makeMove(player2Letter, move)

            if tictactoe.isWinner(player2Letter):
                tictactoe.drawBoard()
                print('Hooray! ' + p2Name +' has won the game!')
                player_two_wins += 1
                gameIsPlaying = False
            else:
                if tictactoe.isBoardFull():
                    tictactoe.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = p1Name

    if not playAgain():
        break

if player_one_wins > player_two_wins and player_one_wins >= 5:
    print(p1Name + ' has won!')
elif player_one_wins < player_two_wins and player_two_wins >= 5:
    print(p2Name + ' has won!')
