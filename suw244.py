############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Songmeng Wang"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math
import random
from itertools import combinations

############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    result = int((math.factorial(n*n)/math.factorial(n*n-n))/math.factorial(n))
    return result

def num_placements_one_per_row(n):
    return (n**n)

def n_queens_valid(board):
    for i in range (len(board)):
        x = board[i]
        if (board.index(x) != i):
            return False
        for j in range(i):
            y = board[j]
            if abs(x-y) == abs(i-j):
                return False
    return True;
    
def n_queens_helper(n,board):
    line = len(board)
    for i in range(n):
        board.append(i)
        if ((n_queens_valid(board))==True):
            if len(board)==n:
                yield (board)
            for i in n_queens_helper(n,board):
                yield i[:]           
        board.pop(line)
    
def n_queens_solutions(n):
    num = len(list(n_queens_helper(n,[])))
    result = []
    f = n_queens_helper(n,[])
    for i in f:
    	result.append(i)
    return (iter(result))

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board

    def get_board(self):
        return (self.board)

    def perform_move(self, row, col):
        ## up(-1,0) down(+1,0) left(0,-1) right(0,+1)
        self.board[row][col] = not(self.board[row][col])
        if row>=1:
            self.board[row-1][col] = not(self.board[row-1][col])
        if row<(len(self.board)-1):
            self.board[row+1][col] = not(self.board[row+1][col])
        if col>=1:
            self.board[row][col-1] = not(self.board[row][col-1])
        if col <(len(self.board[0])-1):
            self.board[row][col+1] = not(self.board[row][col+1])
        
    def scramble(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if(random.random()<0.5):
                    self.perform_move(i,j)
    

    def is_solved(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if(self.board[i][j]!=False):
                    return False
        return True

    def copy(self):
        result = []
        for i in range(len(self.board)):
            line = []
            for j in range(len(self.board[i])):
                line.append(self.board[i][j])
            result.append(line)
        return (LightsOutPuzzle(result))

    def successors(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                newboard = self.copy()
                newboard.perform_move(i,j)
                yield (i,j),newboard

    def find_solution(self):
        solution = []
        num_row = len(self.board)
        num_col = len(self.board[0])
        num_light = num_row * num_col
        light_arr = []
        
        #create light_arr
        for i in range(num_light):
            light_arr.append(i)
        
        for i in range(1,num_light+1): #1~num
            mylight = list(combinations(light_arr,i))
            
            for j in range(len(mylight)):
                myboard = self.copy()
                cur_sol = mylight[j]
                solution = []
                for k in range(i):
                    row = int (int(cur_sol[k]) / int(num_col))
                    col = int (int(cur_sol[k]) % int(num_col))
                    myboard.perform_move(row,col)
                    solution.append((row,col))
                if (myboard.is_solved()):
                    return solution
        return None
                    
            
                
            
        

def create_puzzle(rows, cols):
    result = []
    for j in range(rows):
        line = []
        for i in range(cols):
            line.append(False)
        result.append(line)
    return (LightsOutPuzzle(result))

############################################################
# Section 3: Linear Disk Movement
############################################################

class disk(object):

    def __init__(self,line):
        self.line = line

    def copy(self):
        result = []
        for i in range(len(self.line)):
            result.append(self.line[i])
        return disk(result)

    def issolved1(self,num):
        for i in range(1,num+1):
            if (self.line[len(self.line)-i] <= 0):
                return False
        return True

    def issolved2(self,num):
        for i in range(1,num+1):
            if ((self.line[len(self.line)-i]) != i):
                return False
        return True

    def move(self,curr,target):
        self.line[target] = self.line[curr]
        self.line[curr] = 0

    def possi(self):
        curr = []
        for i in range(len(self.line)):
            if (self.line[i] > 0):
                curr.append(i)
        for i in curr:
            newline = self.copy()
            if (((i+1) not in curr) and ((i+1)<len(self.line))):
                newline.move(i,i+1)
                yield (i,i+1),newline
            elif (((i+2) not in curr) and ((i+2)<len(self.line))):
                newline.move(i,i+2)
                yield (i,i+2),newline
            newline = self.copy()
            if (((i-1) not in curr) and ((i-1)>= 0)):
                newline.move(i,i-1)
                yield (i,i-1),newline
            elif (((i-2) not in curr) and ((i-2)>=0)):
                newline.move(i,i-2)
                yield (i,i-2),newline     

    
def createline(length,n):
    myline = []
    for i in range(1,n+1):
        myline.append(i)
    for i in range(n+1,length+1):
        myline.append(0)
    return (disk(myline))

def solve_identical_disks(length, n):
    myline = createline(length,n)
    mydict = {myline:[]}

    while (True):
        newdict = { }
        for prev_line in mydict:
            prev_step = mydict[prev_line]
            for step,new_line in prev_line.possi():
                new_step = prev_step + [step]
                if (new_line.issolved1(n)):
                    return new_step
                if new_line not in mydict:
                    newdict[new_line] = new_step
        mydict = newdict
        
def solve_distinct_disks(length, n):
    myline = createline(length,n)
    mydict = {myline:[]}
    
    while (True):
        newdict = { }
        for prev_line in mydict:
            prev_step = mydict[prev_line]
            for step,new_line in prev_line.possi():
                new_step = prev_step + [step]
                if (new_line.issolved2(n)):
                    return new_step
                if new_line not in mydict:
                    newdict[new_line] = new_step
        mydict = newdict

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
11 hours
"""

feedback_question_2 = """
The solution blocks is especially challenging
This first solution part (n queen) struggle me for a while
"""

feedback_question_3 = """
the second part is interesting.
I would delete one of the puzzle part.
Solving all these kind of puzzle is boring
"""
