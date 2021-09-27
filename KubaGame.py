# Author: Kent Chau
# Date: 6/9/21
# Description: Kuba game_

class KubaGame:
    """create the Kuba game"""
    def __init__(self, set1, set2):
        """constructor that takes ini player and color, while setting up
        other datamembers"""
        self._player1, self._color1 = set1
        self._player2, self._color2 = set2

        self._currentTurn = None
        self._currentColorTurn = None
        self._lastPlayer = None
        self._lastMove = None
        self._playerOne = []
        self._playerTwo = []
        self._countBlack = self._playerOne.count('B')
        self._countBlack = self._playerOne.count('W')

        self._previousBoard = None

        self._winner = None

        self._kubaboard = {}
        for row in range(7):
            for col in range(7):
                self._kubaboard[(row, col)] = '.'
        # setupWhite
        self._kubaboard[0, 0] = 'W'
        self._kubaboard[0, 1] = 'W'
        self._kubaboard[1, 0] = 'W'
        self._kubaboard[1, 1] = 'W'
        self._kubaboard[5, 5] = 'W'
        self._kubaboard[5, 6] = 'W'
        self._kubaboard[6, 5] = 'W'
        self._kubaboard[6, 6] = 'W'
        # setupBlack
        self._kubaboard[0, 5] = 'B'
        self._kubaboard[0, 6] = 'B'
        self._kubaboard[1, 5] = 'B'
        self._kubaboard[1, 6] = 'B'
        self._kubaboard[5, 0] = 'B'
        self._kubaboard[6, 0] = 'B'
        self._kubaboard[5, 1] = 'B'
        self._kubaboard[6, 1] = 'B'
        # setupRed
        self._kubaboard[1, 3] = 'R'
        self._kubaboard[2, 2] = 'R'
        self._kubaboard[2, 3] = 'R'
        self._kubaboard[2, 4] = 'R'
        self._kubaboard[3, 1] = 'R'
        self._kubaboard[3, 2] = 'R'
        self._kubaboard[3, 3] = 'R'
        self._kubaboard[3, 4] = 'R'
        self._kubaboard[3, 5] = 'R'
        self._kubaboard[4, 2] = 'R'
        self._kubaboard[4, 3] = 'R'
        self._kubaboard[4, 4] = 'R'
        self._kubaboard[5, 3] = 'R'

    def get_board(self):
        """return the board"""
        return self._kubaboard

    def get_board_visual(self):
        """bring out the board visually into terminal"""
        for i in range(0, 7):
            for j in range(0,7):
                print(self._kubaboard[i,j], end="  ")
            else:
                print()

    def get_current_turn(self):
        """return the player that has a turn"""
        if self._currentTurn is None:
            return None
        elif self._currentTurn == self._player1:
            return self._player1
        elif self._currentTurn == self._player2:
            return self._player2

    def set_current_turn(self, player=None):
        """takes in player parameter, set the current tur to specific player"""
        self._currentTurn = player

    def make_move(self, player, tple, dir):
        """take player and coordinates and executes on the board"""
        board = self._kubaboard
        y, x = tple
        if self._winner != None:
            return False
        if self._lastPlayer == player:
            return False
        #assuming player 1 and color below
        #player1 moving their color forward
        if player == self._player1 and dir == 'F' and board[y,x] == self._color1 and board[y-1,x] != '.':
            listbuffer = []
            for m in range(0,y):
                 listbuffer.append(board[m,x])
            if listbuffer[0] == self._color1 and '.' not in listbuffer:
                listbuffer.clear()
                return False
            for i in range(y,0, -1):
                if board[i,x] == '.':
                    for j in range(i,y):
                        board[j,x] = board[j+1,x]
                    board[y,x] = '.'
                    listbuffer.clear()
                    wh, re, bl = self.get_marble_count()
                    if re == 0 or bl == 0 or wh == 0:
                        self._winner = player
                        return
                    self.set_scores(player)
                    self._lastPlayer = player
                    self._lastMove = tple
                    self.change_player()
                    return True
            for k in range(0,y):
                listbuffer.clear()
                board[k,x] = board[k +1,x]
            board[y,x] = '.'
            wh, re, bl = self.get_marble_count()
            if re == 0 or bl == 0 or wh == 0:
                self._winner = player
                return
            listbuffer.clear()
            self._lastPlayer = player
            self._lastMove = tple
            self.change_player()
            self.set_scores(player)
            return True
        #-----------------------------------------------------------------------
        #player1 white left

        elif player == self._player1 and dir == 'L' and board[y, x] == self._color1 and board[y, x-1] != '.':
            listbuffer = []
            for m in range(0, x):
                listbuffer.append(board[y, m])
            # from edge your moving toward
            if listbuffer[0] == self._color1 and '.' not in listbuffer:
                listbuffer.clear()
                return False
            for i in range(x,0, -1):
                if board[y,i] == '.':
                    for j in range(i,x):
                        board[y, j] = board[y,j+1]
                    board[y,x] = '.'
                    wh, re, bl = self.get_marble_count()
                    if re == 0 or bl == 0 or wh == 0:
                        self._winner = player
                        return
                    self.set_scores(player)
                    self._lastPlayer = player
                    self._lastMove = tple
                    self.change_player()
                    listbuffer.clear()
                    return True
            for k in range(0,x):
                board[y,k] = board[y,k +1]
            board[y,x] = '.'
            wh, re, bl = self.get_marble_count()
            if re == 0 or bl == 0 or wh == 0:
                self._winner = player
                return
            listbuffer.clear()
            self._lastPlayer = player
            self.change_player()
            self.set_scores(player)
            self._lastMove = tple
            return True
        #player moving white right

        elif player == self._player1 and dir == 'R' and board[y,x] == self._color1 and board[y,x+1] != '.':
            listbuffer = []
            for m in range(6, x, -1):
                listbuffer.append(board[y, m])
            if listbuffer[0] == self._color1 and '.' not in listbuffer:
                listbuffer.clear()
                return False
            for i in range(x,6):
                if board[y,i] == '.':
                    for j in range(i, x, -1):
                        board[y,j] = board[y,j-1]
                    board[y,x] = '.'
                    wh, re, bl = self.get_marble_count()
                    if re == 0 or bl == 0 or wh == 0:
                        self._winner = player
                        return
                    self.set_scores(player)
                    self._lastPlayer = player
                    self._lastMove = tple
                    self.change_player()
                    listbuffer.clear()
                    return True
            for k in range(6, x, -1):
                listbuffer.clear()
                board[y,k] = board[y,k -1]
            board[y,x] = '.'
            wh, re, bl = self.get_marble_count()
            if re == 0 or bl == 0 or wh == 0:
                self._winner = player
                return
            self._lastPlayer = player
            self._lastMove = tple
            self.change_player()
            self.set_scores(player)
            return True

        #-----------------------------------------------------------------------
        #player move white backward
        elif player == self._player1 and dir == 'B' and board[y, x] == self._color1 and board[y+1,x] != '.':
            listbuffer = []
            for m in range(6, y, -1):
                listbuffer.append(board[m,x])
            # from edge your moving toward
            if listbuffer[0] == self._color1 and '.' not in listbuffer:
                listbuffer.clear()
                return False
            for i in range(y,6):
                if board[i, x] == '.':
                    for j in range(i, y, -1):
                        board[j,x] = board[j - 1, x]
                    board[y, x] = '.'
                    wh, re, bl = self.get_marble_count()
                    if re == 0 or bl == 0 or wh == 0:
                        self._winner = player
                        return
                    listbuffer.clear()
                    self.set_scores(player)
                    self._lastPlayer = player
                    self._lastMove = tple
                    self.change_player()
                    return True
            for k in range(6, y, -1):
                board[k, x] = board[k - 1, x]
            board[y, x] = '.'
            wh, re, bl = self.get_marble_count()
            if re == 0 or bl == 0 or wh == 0:
                self._winner = player
                return
            listbuffer.clear()
            self._lastPlayer = player
            self._lastMove = tple
            self.change_player()
            self.set_scores(player)
            return True
        # -------------------------------------------------------------
        ##
        # player2 moving their color forward
        elif player == self._player2 and dir == 'F' and board[y, x] == self._color2 and board[y - 1, x] != '.':
            listbuffer = []
            for m in range(0, y):
                listbuffer.append(board[m, x])
            if listbuffer[0] == self._color1 and '.' not in listbuffer:
                listbuffer.clear()
                return False
            for i in range(y, 0, -1):
                if board[i, x] == '.':
                    for j in range(i, y):
                        board[j, x] = board[j + 1, x]
                    board[y, x] = '.'
                    listbuffer.clear()
                    wh, re, bl = self.get_marble_count()
                    if re == 0 or bl == 0 or wh == 0:
                        self._winner = player
                        return
                    self.set_scores(player)
                    self._lastPlayer = player
                    self._lastMove = tple
                    self.change_player()
                    return True
            for k in range(0, y):
                listbuffer.clear()
                board[k, x] = board[k + 1, x]
            board[y, x] = '.'
            wh, re, bl = self.get_marble_count()
            if re == 0 or bl == 0 or wh == 0:
                self._winner = player
                return
            listbuffer.clear()
            self._lastPlayer = player
            self._lastMove = tple
            self.change_player()
            self.set_scores(player)
            return True
        # -----------------------------------------------------------------------
        # player2 white left

        elif player == self._player2 and dir == 'L' and board[y, x] == self._color2 and board[y, x - 1] != '.':
            listbuffer = []
            for m in range(0, x):
                listbuffer.append(board[y, m])
            # from edge your moving toward
            if listbuffer[0] == self._color1 and '.' not in listbuffer:
                listbuffer.clear()
                return False
            for i in range(x, 0, -1):
                if board[y, i] == '.':
                    for j in range(i, x):
                        board[y, j] = board[y, j + 1]
                    board[y, x] = '.'
                    wh, re, bl = self.get_marble_count()
                    if re == 0 or bl == 0 or wh == 0:
                        self._winner = player
                        return
                    self.set_scores(player)
                    self._lastPlayer = player
                    self._lastMove = tple
                    self.change_player()
                    listbuffer.clear()
                    return True
            for k in range(0, x):
                board[y, k] = board[y, k + 1]
            board[y, x] = '.'
            wh, re, bl = self.get_marble_count()
            if re == 0 or bl == 0 or wh == 0:
                self._winner = player
                return
            listbuffer.clear()
            self._lastPlayer = player
            self.change_player()
            self.set_scores(player)
            self._lastMove = tple
            return True
        # player2 moving white right

        elif player == self._player2 and dir == 'R' and board[y, x] == self._color2 and board[y, x + 1] != '.':
            listbuffer = []
            for m in range(6, x, -1):
                listbuffer.append(board[y, m])
            if listbuffer[0] == self._color1 and '.' not in listbuffer:
                listbuffer.clear()
                return False
            for i in range(x, 6):
                if board[y, i] == '.':
                    for j in range(i, x, -1):
                        board[y, j] = board[y, j - 1]
                    board[y, x] = '.'
                    wh, re, bl = self.get_marble_count()
                    if re == 0 or bl == 0 or wh == 0:
                        self._winner = player
                        return
                    self.set_scores(player)
                    self._lastPlayer = player
                    self._lastMove = tple
                    self.change_player()
                    listbuffer.clear()
                    return True
            for k in range(6, x, -1):
                listbuffer.clear()
                board[y, k] = board[y, k - 1]
            board[y, x] = '.'
            wh, re, bl = self.get_marble_count()
            if re == 0 or bl == 0 or wh == 0:
                self._winner = player
                return
            self._lastPlayer = player
            self._lastMove = tple
            self.change_player()
            self.set_scores(player)
            return True

        # -----------------------------------------------------------------------
        # player2 move backward
        elif player == self._player2 and dir == 'B' and board[y, x] == self._color2 and board[y + 1, x] != '.':
            listbuffer = []
            for m in range(6, y, -1):
                listbuffer.append(board[m, x])
            # from edge your moving toward
            if listbuffer[0] == self._color1 and '.' not in listbuffer:
                listbuffer.clear()
                return False
            for i in range(y, 6):
                if board[i, x] == '.':
                    for j in range(i, y, -1):
                        board[j, x] = board[j - 1, x]
                    board[y, x] = '.'
                    wh, re, bl = self.get_marble_count()
                    if re == 0 or bl == 0 or wh == 0:
                        self._winner = player
                        return
                    listbuffer.clear()
                    self.set_scores(player)
                    self._lastPlayer = player
                    self._lastMove = tple
                    self.change_player()
                    return True
            for k in range(6, y, -1):
                board[k, x] = board[k - 1, x]
            board[y, x] = '.'
            wh, re, bl = self.get_marble_count()
            if re == 0 or bl == 0 or wh == 0:
                self._winner = player
                return
            listbuffer.clear()
            self._lastPlayer = player
            self._lastMove = tple
            self.change_player()
            self.set_scores(player)
            return True
        # -------------------------------------------------------------
        else:
            return False

    def change_player(self):
        """will switch player to affect player turn"""
        if self._lastPlayer == self._player1:
            self.set_current_turn(self._player2)
        if self._lastPlayer == self._player2:
            self.set_current_turn(self._player1)

    def set_scores(self, player):
        """will set scores for each player by filling their
        respective lists in data members"""
        w, b, r = self.get_marble_count()
        self._playerOne.clear()
        self._playerTwo.clear()
        for a in range(0, (8-b)):
            self._playerOne.append('B')
            self._playerTwo.append('B')
        for c in range(0, (8-w)):
            self._playerOne.append('W')
            self._playerTwo.append('W')
        if player == self._player1:
            for d in range(0, (13 - r)):
                self._playerOne.append('R')
        if player == self._player2:
            for e in range(0, (13 - r)):
                self._playerTwo.append('R')

    def get_winner(self):
        """return winner if there is one, otherwise None"""
        return self._winner

    def get_captured(self, player):
        """return list of captured marbles for a player"""
        #divide scores on player param
        if player == self._player1:
            return self._playerOne.count('R')
        if player == self._player2:
            return self._playerTwo.count('R')

    def get_marble(self, tup):
        """return the marble at a specific location"""
        board = self._kubaboard
        if board[tup] == '.':
            return 'X'
        else:
            return board[tup]

    def get_marble_count(self):
        """returns the number of white marbles, black marbles
        and red marbles"""
        board = self._kubaboard
        w = 0
        b = 0
        r = 0
        for i in range(0,7):
            for j in range(0,7):
                if board[i,j] == "W":
                    w +=1
                if board[i,j] == "B":
                    b +=1
                if board[i,j] == "R":
                    r +=1
        tup = (w, b, r)
        return tup


