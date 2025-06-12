#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        # this whole stupid section is to foil the dumb testcase where theres a board full of A's and the 
        # word has a B
        occurences_in_word = {}
        occurences_in_board = {}

        for i in range(len(word)):
            if occurences_in_word.get(word[i]) == None:
                occurences_in_word[word[i]] = 1
            else: 
                occurences_in_word[word[i]] += 1

        for i in range(len(board)):
            for j in range(len(board[0])):
               if occurences_in_board.get(board[i][j]) == None:
                   occurences_in_board[board[i][j]] = 1
               else: 
                   occurences_in_board[board[i][j]] += 1

        occurences_in_word = {k:v for k, v in sorted(occurences_in_word.items())}
        occurences_in_board = {k:v for k, v in sorted(occurences_in_board.items())}

        for key,val in occurences_in_word.items():
            if occurences_in_board.get(key) == None or occurences_in_board[key] < val:
                # There are less of a certain letter in the board compared to the word, ergo solution is imopssible
                return False

        self.board = board
        self.lettersFound = []
        self.word = word
        self.path = []
        self.visited = {}
        self.allPaths = []
        self.done = False
        # go through board until you find a letter in the word
        positions = []

        # find the positions of the letters that start the word in the board
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != word[0]:
                    continue
                else: 
                    positions.append((i, j))

        # if the starting letter is not found, exit
        if positions == []:
            return False
        
        # starting at the position of where the letter is, explore all possible branches towards the word
        for i in range(len(positions)):
            self.lettersFound.append(word[0])
            self.path.append(positions[i])
            self.search(positions[i])
            self.visited[f'{positions[i][0]}{positions[i][1]}'] = True

            self.path = []
            self.visited = {}
            self.lettersFound = []

        if len(self.allPaths) > 0:
            return True
        else:
            return False
    
    def search(self, pos: tuple):
        if self.done == True:
            return

        nextLetter = self.findNextLetter()
        if nextLetter == None:
            print(f"Found full path!: {self.path}")
            self.allPaths.append(self.path)
            self.done = True
            return

        adjacent_positions = []
        adjacent_squares = []
        matching_letters = 0
        currentLetter = self.board[pos[0]][pos[1]]
        letters_added = []

        adjacent_positions.append((pos[0] - 1, pos[1])) # verticall up
        adjacent_positions.append((pos[0] + 1, pos[1])) # vertically down
        adjacent_positions.append((pos[0], pos[1] - 1)) # horizontally left
        adjacent_positions.append((pos[0], pos[1] + 1)) # horizontally right

        for pose in adjacent_positions:
            if pose[0] < 0 or pose[1] < 0 or (pose[0] > len(self.board) - 1) or (pose[1] > len(self.board[0]) - 1):
                continue
            else: 
                adjacent_squares.append((self.board[pose[0]][pose[1]], pose))

        for i in range(len(adjacent_squares)):
            char = adjacent_squares[i][0]
            pose = adjacent_squares[i]

            # if we've visited this, skip it
            if self.visited.get(f'{pose[1][0]}{pose[1][1]}') != None and self.visited[f'{pose[1][0]}{pose[1][1]}'] is True:
                continue

            if char == nextLetter:
                matching_letters += 1
                self.lettersFound.append(char)
                self.path.append(pose[1])
                letters_added.append(pose[1])
                self.visited[f'{pos[0]}{pos[1]}'] = True
                self.search(pose[1])
 
        you_fucked_up = False
        for i in range(len(letters_added)):
            if letters_added[i] not in self.path:
                you_fucked_up = True

        if matching_letters == 0 or you_fucked_up:
            self.lettersFound.pop()
            self.path.remove(pos)
            self.visited[f'{pos[0]}{pos[1]}'] = False

    
    def findNextLetter(self):
        if self.lettersFound == []:
            return self.word[1]

        i = 0
        found = self.lettersFound[i]
        expected = self.word[i]

        while found != None and expected != None and found == expected:
            i += 1
            found = self.tryGet(self.lettersFound, i)
            expected = self.tryGet(self.word, i)
        
        if expected == None and found == None:
            return None
        elif found == None and expected != None: 
            return expected
        else: 
            return found

    def tryGet(self, s, pos: int):
        try:
            return s[pos]
        except:
            return None

# @lc code=end
f = Solution()
f.exist([["a"]], "ab")
# f.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
# f.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
# f.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
# f.exist([["R","O","H","O"],["S","F","C","R"],["A","D","E","E"]], "HOR")
# f.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")
# f.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB")