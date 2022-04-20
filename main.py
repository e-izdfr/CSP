from time import time
from Binairo import *
from Cell import *
from State import *
import random
## w b

def main():
    input_numbers = []  ## first row = size of puzzle(n)  ## second row = number of cells that have color in the statrt  (m)  ## row 3 to row 3+m : 
    Input = open('input2.txt').readlines()
    for line in Input:
        line = line.rstrip()
        numbers = line.split(' ')
        n = [int(number) for number in numbers]
        input_numbers.append(n)

    board = []
    size_puzzle = input_numbers[0][0]
    for i in range(0, size_puzzle):
        row = []
        for j in range(0, size_puzzle):
            cell = Cell(i, j)
            row.append(cell)
        board.append(row) 
   
    for i in range(2, len(input_numbers)):
        if input_numbers[i][2] == 0: # w
            board[input_numbers[i][0]][input_numbers[i][1]].value = 'W'
            board[input_numbers[i][0]][input_numbers[i][1]].domain = ['n']

        if input_numbers[i][2] == 1:  # b
            board[input_numbers[i][0]][input_numbers[i][1]].value = 'B'
            board[input_numbers[i][0]][input_numbers[i][1]].domain = ['n']
       
    state = State(size_puzzle, board)  
    print('initial board:')
    state.print_board()
    
    def Whether_len_is_0_or_not(cell):
        return len(cell.domain) == 0 and cell.value == '_'
    
    def Whether_len_is_1_or_not(cell):
        return len(cell.domain) == 1 and cell.value == '_'
    
    def Whether_len_is_2_or_not(cell):
        return len(cell.domain) == 2 and cell.value == '_'
    
    def MRV(state):
        list_of_0s = []
        for row in state.board:
            list_of_0s += list(filter(Whether_len_is_0_or_not, row))
        if len(list_of_0s) != 0:
            return 'failure'
        list_of_1s = []
        list_of_2s = []
        for row in state.board:
            list_of_1s += list(filter(Whether_len_is_1_or_not, row))
        if list_of_1s != []:
            rand_int = random.randint(0, len(list_of_1s) - 1)
            return list_of_1s[rand_int]
        for row in state.board:
            list_of_2s += list(filter(Whether_len_is_2_or_not, row))
        if list_of_2s != []:
            rand_int = random.randint(0, len(list_of_2s) - 1)
            return list_of_2s[rand_int]
    
    def find_empty_cells(state):
        empty_cells = []
        for row in state.board:
            for cell in row:
                if cell.value == '_':
                    empty_cells.append(cell)
        return empty_cells
    
    def is_consistant2(var, cell, state):
        if cell.x != var.x:
            if state.board[cell.x][var.y].value.upper() == var.value.upper():
                key = 0
                for j in [x0 for x0 in range(state.size) if x0 != var.y]:
                    if state.board[cell.x][j].value.upper() != state.board[var.x][j].value.upper() or state.board[cell.x][j].value\
                    == '_':
                        key = 1
                        break
                    
                if key == 0:
                    return False
            if cell.y != var.y:
                if state.board[var.x][cell.y].value.upper() == var.value.upper():
                    key = 0
                    for i in [x0 for x0 in range(state.size) if x0 != var.x]:
                        if state.board[i][cell.y].value.upper() != state.board[i][var.y].value.upper() or state.board[i][cell.y].value\
                        == '_':
                            key = 1
                            break
                        
                    if key == 0:
                        return False
            
            else:
                num_white_circles = 0
                num_black_circles = 0
                
                for i in range(0, state.size):
                    if(state.board[i][var.y].value.upper() == 'W'):
                        num_white_circles += 1
            
                    if(state.board[i][var.y].value.upper() == 'B'):
                        num_black_circles += 1
                        
                if num_white_circles > state.size / 2 or num_black_circles > state.size / 2:
                    return False
                
                if cell.x == var.x - 2:
                    if state.board[cell.x][var.y].value.upper() == state.board[var.x - 1][var.y].value.upper() and \
                    state.board[var.x - 1][var.y].value.upper() == var.value.upper():
                        return False
                
                elif cell.x == var.x - 1:
                    try:
                        if(state.board[var.x - 2][var.y].value.upper() == state.board[cell.x][var.y].value.upper() and \
                            state.board[cell.x][var.y].value.upper() == var.value.upper()):
                            return False
                        
                    except:
                        pass
                    
                    try:
                        if(state.board[cell.x][var.y].value.upper() == var.value.upper() and var.value.upper() ==\
                           state.board[var.x + 1][var.y].value.upper()):
                            return False
                        
                    except:
                        pass
                
                elif cell.x == var.x + 1:
                    try:
                        if(state.board[var.x - 1][var.y].value.upper() == var.value.upper() and var.value.upper() == \
                            state.board[cell.x][var.y].value.upper()):
                            return False
                    
                    except:
                        pass
                    
                    try:
                        if(var.value.upper() == state.board[cell.x][var.y].value.upper() and state.board[cell.x][var.y].value.upper() ==\
                            state.board[var.x + 2][var.y].value.upper()):
                            return False
                        
                    except:
                        pass
                
                elif cell.x == var.x + 2:
                    if(var.value.upper() == state.board[var.x + 1][var.y].value.upper() and \
                        state.board[var.x + 1][var.y].value.upper() == state.board[cell.x][var.y].value.upper()):
                        return False
                        
        else:
            if state.board[var.x][cell.y].value.upper() == var.value.upper():
                key = 0
                for i in [x0 for x0 in range(state.size) if x0 != var.x]:
                    if state.board[i][cell.y].value.upper() != state.board[i][var.y].value.upper() or state.board[i][cell.y].value == '_':
                        key = 1
                        break
                    
                if key == 0:
                    return False
            
            num_white_circles = 0
            num_black_circles = 0
            
            for j in range(0, state.size):
                if(state.board[var.x][j].value.upper() == 'W'):
                    num_white_circles += 1
            
                if(state.board[var.x][j].value.upper() == 'B'):
                    num_black_circles += 1
                        
            if num_white_circles > state.size / 2 or num_black_circles > state.size / 2:
                return False
            
            if cell.y == var.y - 2:
                if state.board[var.x][cell.y].value.upper() == state.board[var.x][var.y - 1].value.upper() and \
                    state.board[var.x][var.y - 1].value.upper() == var.value.upper():
                        return False
                
            elif cell.y == var.y - 1:
                try:
                    if(state.board[var.x][var.y - 2].value.upper() == state.board[var.x][cell.y].value.upper() and \
                        state.board[var.x][cell.y].value.upper() == var.value.upper()):
                        return False
                        
                except:
                    pass
                    
                try:
                    if(state.board[var.x][cell.y].value.upper() == var.value.upper() and var.value.upper() ==\
                        state.board[var.x][var.y + 1].value.upper()):
                        return False
                        
                except:
                    pass
                
            elif cell.y == var.y + 1:
                try:
                    if(state.board[var.x][var.y - 1].value.upper() == var.value.upper() and var.value.upper() == 
                       state.board[var.x][cell.y].value.upper()):
                        return False
                    
                except:
                    pass
                    
                try:
                    if(var.value.upper() == state.board[var.x][cell.y].value.upper() and state.board[var.x][cell.y].value.upper() ==\
                        state.board[var.x][var.y + 2].value.upper()):
                        return False
                        
                except:
                    pass
                
            elif cell.y == var.y + 2:
                if(var.value.upper() == state.board[var.x][var.y + 1].value.upper() and state.board[var.x][var.y + 1].value.upper() == \
                    state.board[var.x][cell.y].value.upper()):
                    return False
                
        return True
    
    def LCV(var, state):
        if len(var.domain) == 1:
            return var.domain[0]
        
        num_of_constraint_violations = []
        for value in var.domain:
            var.value = value
            
            count = 0
            for cell in find_empty_cells(state):
                for v in cell.domain:
                    cell.value = v
                    if not is_consistant2(var, cell, state):
                        count += 1    
                cell.value = '_'
            num_of_constraint_violations.append(count)
        
        if num_of_constraint_violations[0] > num_of_constraint_violations[1]:
            return var.domain[1]
        
        elif num_of_constraint_violations[0] < num_of_constraint_violations[1]:
            return var.domain[0]
        
        return var.domain[random.randint(0, 1)]
    
    def forward_checking(var, cell, state):
        if cell.x != var.x:
            if state.board[cell.x][var.y].value.upper() == var.value.upper():
                key = 0
                for j in [x0 for x0 in range(state.size) if x0 != var.y]:
                    if state.board[cell.x][j].value.upper() != state.board[var.x][j].value.upper() or state.board[cell.x][j].value\
                    == '_':
                        key = 1
                        break
                    
                if key == 0:
                    return False
            if cell.y != var.y:
                if state.board[var.x][cell.y].value.upper() == var.value.upper():
                    key = 0
                    for i in [x0 for x0 in range(state.size) if x0 != var.x]:
                        if state.board[i][cell.y].value.upper() != state.board[i][var.y].value.upper() or state.board[i][cell.y].value\
                        == '_':
                            key = 1
                            break
                        
                    if key == 0:
                        return False
            
            else:
                num_white_circles = 0
                num_black_circles = 0
                
                for i in range(0, state.size):
                    if(state.board[i][var.y].value.upper() == 'W'):
                        num_white_circles += 1
            
                    if(state.board[i][var.y].value.upper() == 'B'):
                        num_black_circles += 1
                        
                if num_white_circles > state.size / 2 or num_black_circles > state.size / 2:
                    return False
                
                if cell.x == var.x - 2:
                    if state.board[cell.x][var.y].value.upper() == state.board[var.x - 1][var.y].value.upper() and \
                    state.board[var.x - 1][var.y].value.upper() == var.value.upper():
                        return False
                
                elif cell.x == var.x - 1:
                    try:
                        if(state.board[var.x - 2][var.y].value.upper() == state.board[cell.x][var.y].value.upper() and \
                            state.board[cell.x][var.y].value.upper() == var.value.upper()):
                            return False
                        
                    except:
                        pass
                    
                    try:
                        if(state.board[cell.x][var.y].value.upper() == var.value.upper() and var.value.upper() ==\
                           state.board[var.x + 1][var.y].value.upper()):
                            return False
                        
                    except:
                        pass
                
                elif cell.x == var.x + 1:
                    try:
                        if(state.board[var.x - 1][var.y].value.upper() == var.value.upper() and var.value.upper() == \
                            state.board[cell.x][var.y].value.upper()):
                            return False
                    
                    except:
                        pass
                    
                    try:
                        if(var.value.upper() == state.board[cell.x][var.y].value.upper() and state.board[cell.x][var.y].value.upper() ==\
                            state.board[var.x + 2][var.y].value.upper()):
                            return False
                        
                    except:
                        pass
                
                elif cell.x == var.x + 2:
                    if(var.value.upper() == state.board[var.x + 1][var.y].value.upper() and \
                        state.board[var.x + 1][var.y].value.upper() == state.board[cell.x][var.y].value.upper()):
                        return False
                        
        else:
            if state.board[var.x][cell.y].value.upper() == var.value.upper():
                key = 0
                for i in [x0 for x0 in range(state.size) if x0 != var.x]:
                    if state.board[i][cell.y].value.upper() != state.board[i][var.y].value.upper() or state.board[i][cell.y].value == '_':
                        key = 1
                        break
                    
                if key == 0:
                    return False
            
            num_white_circles = 0
            num_black_circles = 0
            
            for j in range(0, state.size):
                if(state.board[var.x][j].value.upper() == 'W'):
                    num_white_circles += 1
            
                if(state.board[var.x][j].value.upper() == 'B'):
                    num_black_circles += 1
                        
            if num_white_circles > state.size / 2 or num_black_circles > state.size / 2:
                return False
            
            if cell.y == var.y - 2:
                if state.board[var.x][cell.y].value.upper() == state.board[var.x][var.y - 1].value.upper() and \
                    state.board[var.x][var.y - 1].value.upper() == var.value.upper():
                        return False
                
            elif cell.y == var.y - 1:
                try:
                    if(state.board[var.x][var.y - 2].value.upper() == state.board[var.x][cell.y].value.upper() and \
                        state.board[var.x][cell.y].value.upper() == var.value.upper()):
                        return False
                        
                except:
                    pass
                    
                try:
                    if(state.board[var.x][cell.y].value.upper() == var.value.upper() and var.value.upper() ==\
                        state.board[var.x][var.y + 1].value.upper()):
                        return False
                        
                except:
                    pass
                
            elif cell.y == var.y + 1:
                try:
                    if(state.board[var.x][var.y - 1].value.upper() == var.value.upper() and var.value.upper() == 
                       state.board[var.x][cell.y].value.upper()):
                        return False
                    
                except:
                    pass
                    
                try:
                    if(var.value.upper() == state.board[var.x][cell.y].value.upper() and state.board[var.x][cell.y].value.upper() ==\
                        state.board[var.x][var.y + 2].value.upper()):
                        return False
                        
                except:
                    pass
                
            elif cell.y == var.y + 2:
                if(var.value.upper() == state.board[var.x][var.y + 1].value.upper() and state.board[var.x][var.y + 1].value.upper() == \
                    state.board[var.x][cell.y].value.upper()):
                    return False
                
        return True
            
    def Whether_cell_is_assigned_or_not(cell):
        return cell.domain == ['n']
    
    def Whether_cell_is_colorful_or_not(cell, color):
        return cell.value.lower() == color
    
    def find_empty_row_cells(row):
        return list(filter(lambda x: x.value == '_', row))
    
    def AC3(state):
        for row in state.board:
            for cell in find_empty_cells(row):
                for value in cell.domain:
                    cell.value = value
                    try:
                        if(state.board[cell.x - 1][cell.y].value.upper() == cell.value.upper() and 
                        state.board[cell.x - 2][cell.y].value.upper() == cell.value.upper()):
                            cell.domain.remove(cell.value)
                            if cell.domain == []:
                                return False
                            
                    except:
                        pass
                    
                    try:
                        if state.board[cell.x - 1][cell.y].value == '_' and state.board[cell.x - 2][cell.y].value.upper() == \
                            cell.value.upper():
                                if state.board[cell.x - 1][cell.y].domain == [cell.value]:
                                    cell.domain.remove(cell.value)
                                    if cell.domain == []:
                                        return False 
                                    
                    except:
                        pass 
                            
                    try:
                        if state.board[cell.x - 2][cell.y].value == '_' and state.board[cell.x - 1][cell.y].value.upper() == \
                            cell.value.upper():
                                if state.board[cell.x - 2][cell.y].domain == [cell.value]:
                                    cell.domain.remove(cell.value)
                                    if cell.domain == []:
                                        return False
                                    
                    except:
                        pass
                                
                    try:
                        if state.board[cell.x - 2][cell.y].domain == [cell.value] and state.board[cell.x - 1][cell.y].domain ==\
                            [cell.value]:
                                cell.domain.remove(cell.value)
                                if cell.domain == []:
                                    return False
                                
                    except:
                        pass
                            
                    try:
                        if(state.board[cell.x][cell.y - 1].value.upper() == cell.value.upper() and 
                        state.board[cell.x][cell.y - 2].value.upper() == cell.value.upper()):
                            cell.domain.remove(cell.value)
                            if cell.domain == []:
                                return False
                            
                    except:
                        pass
                        
                    try:
                        if state.board[cell.x][cell.y - 1].value == '_' and state.board[cell.x][cell.y - 2].value.upper() == \
                            cell.value.upper():
                                if state.board[cell.x][cell.y - 1].domain == [cell.value]:
                                    cell.domain.remove(cell.value)
                                    if cell.domain == []:
                                        return False
                                    
                    except:
                        pass
                                
                    try:
                        if state.board[cell.x][cell.y - 2].value == '_' and state.board[cell.x][cell.y - 1].value.upper() == \
                            cell.value.upper():
                                if state.board[cell.x][cell.y - 2].domain == [cell.value]:
                                    cell.domain.remove(cell.value)
                                    if cell.domain == []:
                                        return False
                                    
                    except:
                        pass
                                
                    try:
                        if state.board[cell.x][cell.y - 2].domain == [cell.value] and state.board[cell.x][cell.y - 1].domain ==\
                            [cell.value]:
                                cell.domain.remove(cell.value)
                                if cell.domain == []:
                                    return False
                                
                    except:
                        pass
                            
                    try:
                        if(state.board[cell.x + 1][cell.y].value.upper() == cell.value.upper() and 
                        state.board[cell.x + 2][cell.y].value.upper() == cell.value.upper()):
                            cell.domain.remove(cell.value)
                            if cell.domain == []:
                                return False
                            
                    except:
                        pass
                    
                    try:
                        if state.board[cell.x + 1][cell.y].value == '_' and state.board[cell.x + 2][cell.y].value.upper() == \
                            cell.value.upper():
                                if state.board[cell.x + 1][cell.y].domain == [cell.value]:
                                    cell.domain.remove(cell.value)
                                    if cell.domain == []:
                                        return False
                                    
                    except:
                        pass
                                
                    try:
                        if state.board[cell.x + 2][cell.y].value == '_' and state.board[cell.x + 1][cell.y].value.upper() == \
                            cell.value.upper():
                                if state.board[cell.x + 2][cell.y].domain == [cell.value]:
                                    cell.domain.remove(cell.value)
                                    if cell.domain == []:
                                        return False
                                    
                    except:
                        pass
                                
                    try:
                        if state.board[cell.x + 2][cell.y].domain == [cell.value] and state.board[cell.x + 1][cell.y].domain ==\
                            [cell.value]:
                                cell.domain.remove(cell.value)
                                if cell.domain == []:
                                    return False
                                
                    except:
                        pass
                            
                    try:
                        if(state.board[cell.x][cell.y + 1].value.upper() == cell.value.upper() and 
                        state.board[cell.x][cell.y + 2].value.upper() == cell.value.upper()):
                            cell.domain.remove(cell.value)
                            if cell.domain == []:
                                return False
                            
                    except:
                        pass
                        
                    try:
                        if state.board[cell.x][cell.y + 1].value == '_' and state.board[cell.x][cell.y + 2].value.upper() == \
                            cell.value.upper():
                                if state.board[cell.x][cell.y + 1].domain == [cell.value]:
                                    cell.domain.remove(cell.value)
                                    if cell.domain == []:
                                        return False
                                    
                    except:
                        pass
                                
                    try:
                        if state.board[cell.x][cell.y + 2].value == '_' and state.board[cell.x][cell.y + 1].value.upper() == \
                            cell.value.upper():
                                if state.board[cell.x][cell.y + 2].domain == [cell.value]:
                                    cell.domain.remove(cell.value)
                                    if cell.domain == []:
                                        return False
                                    
                    except:
                        pass
                                
                    try:
                        if state.board[cell.x][cell.y + 2].domain == [cell.value] and state.board[cell.x][cell.y + 1].domain ==\
                            [cell.value]:
                                cell.domain.remove(cell.value)
                                if cell.domain == []:
                                    return False
                                
                    except:
                        pass  
                    
                    if len(list(filter(Whether_cell_is_colorful_or_not(color=cell.value), row))) > state.size / 2:
                        cell.domain.remove(cell.value)
                        if cell.domain == []:
                            return False
                        
                    elif len(list(filter(Whether_cell_is_colorful_or_not(color=cell.value), find_empty_row_cells(row)))) < state.size -\
                    len(list(filter(Whether_cell_is_colorful_or_not(color=cell.value), row))) or\
                    len(list(filter(Whether_cell_is_colorful_or_not(color=['b', 'w'].remove(cell.value))[0],
                                    find_empty_row_cells(row)))) < state.size -\
                    len(list(filter(Whether_cell_is_colorful_or_not(color=['b', 'w'].remove(cell.value))[0], row))):
                        cell.domain.remove(cell.value)
                        if cell.domain == []:
                            return False
                        
                    col = [state.board[i][cell.y] for i in range(state.size)]
                    if len(list(filter(Whether_cell_is_colorful_or_not(color=cell.value), col))) > state.size / 2:
                        cell.domain.remove(cell.value)
                        if cell.domain == []:
                            return False
                        
                    elif len(list(filter(Whether_cell_is_colorful_or_not(color=cell.value), find_empty_row_cells(col)))) < state.size -\
                    len(list(filter(Whether_cell_is_colorful_or_not(color=cell.value), col))) or\
                    len(list(filter(Whether_cell_is_colorful_or_not(color=['b', 'w'].remove(cell.value))[0],
                                    find_empty_row_cells(col)))) < state.size -\
                    len(list(filter(Whether_cell_is_colorful_or_not(color=['b', 'w'].remove(cell.value))[0], col))):
                        cell.domain.remove(cell.value)
                        if cell.domain == []:
                            return False
                        
                cell.value = '_'
                
        for row in state.board:
            if list(filter(Whether_len_is_2_or_not, [c for c in row if c!= cell]) == [] and
                    len(list(filter(Whether_cell_is_assigned_or_not, row)) != state.size)):
                for row2 in state.board[state.board.index(row) + 1:]:
                    if list(filter(Whether_len_is_2_or_not, [c for c in row2 if c!= cell])):
                        s = set()
                        for c in find_empty_cells(row):
                            c.value = c.domain[0]
                            s.add(c) 
                        
                        for c in find_empty_cells(row2):
                            c.value = c.domain[0]
                            s.add(c)
                            
                        if [c.value for c in row ] == [c.value for c in row2]:
                            return False
                            
                        for c in s:
                            c.value = '_'
                            
        transpose = [[state.board[j][i] for j in range(state.size)] for i in range(state.size)]
        for col in transpose:
            if list(filter(Whether_len_is_2_or_not, [c for c in col if c!= cell]) == [] and
                    len(list(filter(Whether_cell_is_assigned_or_not, col)) != state.size)):
                for col2 in state.board[state.board.index(col) + 1:]:
                    if list(filter(Whether_len_is_2_or_not, [c for c in col2 if c!= cell])):
                        s = set()
                        for c in find_empty_cells(col):
                            c.value = c.domain[0]
                            s.add(c) 
                        
                        for c in find_empty_cells(col2):
                            c.value = c.domain[0]
                            s.add(c)
                            
                        if [c.value for c in col ] == [c.value for c in col2]:
                            return False
                            
                        for c in s:
                            c.value = '_'
        return True
        
    def backTrack(state):  #implement backTrack and other csp functions in Binairo.py
        key = 1
        if check_termination(state):
            state.print_board()
        
        else:
            var = MRV(state)
            if var == 'failure':
                return 'failure'
            
            value = LCV(var, state)
            var.value = value
            if is_consistent(state):
                s = set()
                for cell in find_empty_cells(state):
                    for v in cell.domain:
                        cell.value = v
                        if not forward_checking(var, cell, state):
                            cell.domain.remove(v)
                            s.add(f'{cell.x}{cell.y}{v}')
                            
                            if len(cell.domain) == 0:
                                key = 0
                                break
                    
                    cell.value = '_'
                    
                    if key == 0:
                        break 
                    
                if key == 1:
                    result = backTrack(state)
                    if result != 'failure':
                        return result
                
                for i in s:
                    if len(i) == 3:
                        state.board[int(i[0])][int(i[1])].domain.append(i[2])
                        
                    elif len(i) == 4:
                        state.board[int(i[0])][int(i[1])].domain.extend([i[2], i[3]])
                 
            var.value = '_'
            
            try:
                key = 1
                var.value = var.domain[1 - var.domain.index(value)]
                if is_consistent(state):
                    s = set()
                    for cell in find_empty_cells(state):
                        for v in cell.domain:
                            cell.value = v
                            if not forward_checking(var, cell, state):
                                cell.domain.remove(v)
                                s.add(f'{cell.x}{cell.y}{v}')
                                
                                if len(cell.domain) == 0:
                                    key = 0
                                    break
                    
                        cell.value = '_'
                        
                        if key == 0:
                            break
                    
                    if key == 1:
                        result = backTrack(state)
                        if result != 'failure':
                            return result
                    
                    for i in s:
                        if len(i) == 3:
                            state.board[int(i[0])][int(i[1])].domain.append(i[2])
                            
                        elif len(i) == 4:
                            state.board[int(i[0])][int(i[1])].domain.extend([i[2], i[3]])
                        
                var.value = '_'
                return 'failure'
                
            except:
                var.value ='_'
                return 'failure'
            
    start_time = time()
    result = backTrack(state) 
    if result == 'failure':
        print('No solution exists.')   
    end_time = time()
    print('time: ',end_time-start_time)

if __name__ == '__main__':
    main() 