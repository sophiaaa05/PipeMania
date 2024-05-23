# pipe.py: Template para implementacao do projeto de Inteligencia Artificial 2023/2024.
# Devem alterar as classes e funcoes neste ficheiro de acordo com as instrucoes do enunciado.
# Além das funcoes e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 39:
# 106748 Ines Antunes
# 106369 Sophia Alencar


from sys import stdin
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)

LEFT = 0
ABOVE = 1
RIGHT = 2
DOWN = 3

class PipeManiaState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = PipeManiaState.state_id
        PipeManiaState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe


class Board:
    """Representacao interna de um tabuleiro de PipeMania."""
    
    pipe_description = {
        'FC': (0,1,0,0), 'FB': (0,0,0,1), 'FE': (1,0,0,0), 'FD': (0,0,1,0),
        'BC': (1,1,1,0), 'BB': (1,0,1,1), 'BE': (1,1,0,1), 'BD': (0,1,1,1),
        'VC': (1,1,0,0), 'VB': (0,0,1,1), 'VE': (1,0,0,1), 'VD': (0,1,1,0),
        'LH': (1,0,1,0), 'LV': (0,1,0,1), 'Non': (0,0,0,0)
    }
    
    piece_clockwise = {
        'FC': 'FD', 'FB': 'FE', 'FE': 'FC', 'FD': 'FB', 'BC': 'BD', 'BB': 'BE', 'BE': 'BC',
        'BD': 'BB', 'VC': 'VD', 'VB': 'VE', 'VE': 'VC', 'VD': 'VB', 'LH': 'LV', 'LV': 'LH',
        'None': 'None'
    }
    
    piece_anticlockwise = {
        'FC': 'FE', 'FB': 'FD', 'FE': 'FB', 'FD': 'FC', 'BC': 'BE', 'BB': 'BE', 'BD': 'BC', 
        'VC': 'VE', 'VB': 'VD', 'VE': 'VB', 'VD': 'VC', 'LH': 'LV', 'LV': 'LH', 
        'None': 'None'
    }
    
    def __init__(self, board):
        self.board = board
        self.init_board()

    def get_value(self, row: int, col: int) -> str:
        """Devolve o valor na respetiva posicao do tabuleiro."""
        return self.board[col][row]
        
    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        below = self.get_value(row, col+1) if col < len(self.board)-1 else 'None'
        above = self.get_value(row, col-1) if col > 0 else 'None'
        return above, below

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente a esquerda e a direita,
        respectivamente."""
        left = self.get_value(row-1, col) if row > 0 else 'None'
        right = self.get_value(row+1, col) if row < len(self.board[0])-1 else 'None'
        return left, right
    
    def connected_left(self, pipe: str):
        return self.pipe_description[pipe[:-1]][RIGHT] == 1
    
    def connected_right(self, pipe:str):
        return self.pipe_description[pipe[:-1]][LEFT] == 1
    
    def connected_above(self, pipe: str):
        return self.pipe_description[pipe[:-1]][DOWN] == 1

    def connected_down(self, pipe: str):
        return self.pipe_description[pipe[:-1]][ABOVE] == 1
    
    def correct_form(piece_list: list):
        

        possible_actions = []
        for piece_list in possible_actions :
            
            new_piece_list = []  
            for i in range(len(piece_list)):
                new_action = (piece_list[0][0], piece_list[0][1], piece_list[i])
                new_piece_list.append(new_action)
        
            possible_actions.append(new_piece_list)
    
        return possible_actions  
          
    def actions_pieces(self, unsolved_pieces: list):
        
        possible_actions = []
        
        for unsolved_piece in unsolved_pieces:
            
            actions_for_piece = []
            actions_for_piece.append(unsolved_piece)
            current_piece = self.board[unsolved_piece[0]][unsolved_piece[1]]
            is_locked = 'L'
            is_none = 'n'
            left, right = self.adjacent_horizontal_values(unsolved_piece[1], unsolved_piece[0])
            above, below = self.adjacent_vertical_values(unsolved_piece[1], unsolved_piece[0])
            connected_left = self.connected_left(left)
            connected_right = self.connected_right(right)
            connected_below = self.connected_down(below)
            connected_above = self.connected_above(above)
            piece_type = current_piece[0]
                    
            if piece_type == 'F':
                
                actions_for_piece.append('FCL')
                actions_for_piece.append('FBL')
                actions_for_piece.append('FEL')
                actions_for_piece.append('FDL')
                
                if (not connected_above and (is_locked == above[2] or is_none == above[2])) or above[0] == 'F':
                    if 'FCL' in actions_for_piece:
                        actions_for_piece.remove('FCL')
                
                if (not connected_below and (is_locked == below[2] or is_none == below[2])) or below[0] == 'F':
                    if 'FBL' in actions_for_piece:
                        actions_for_piece.remove('FBL')
                        
                if (not connected_left and (is_locked == left[2] or is_none == left[2])) or left[0] == 'F':
                    if 'FEL' in actions_for_piece:
                        actions_for_piece.remove('FEL')
                        
                if (not connected_right and (is_locked == right[2] or is_none == right[2])) or right[0] == 'F':
                    if 'FDL' in actions_for_piece:
                        actions_for_piece.remove('FDL')
                    
            elif piece_type == 'B':
                
                actions_for_piece.append('BCL')
                actions_for_piece.append('BBL')
                actions_for_piece.append('BEL')
                actions_for_piece.append('BDL')
                
                
                if ( connected_above and is_locked == above[2]):
                    if 'BBL' in actions_for_piece:
                        actions_for_piece.remove('BBL')
                
                if ( connected_below and is_locked == below[2]):
                    if 'BCL' in actions_for_piece:
                        actions_for_piece.remove('BCL')
                
                if ( connected_right and is_locked == right[2]):
                    if 'BEL' in actions_for_piece:
                        actions_for_piece.remove('BEL')
                        
                if ( connected_left and is_locked == left[2]):
                    if 'BDL' in actions_for_piece:
                        actions_for_piece.remove('BDL')
                    
            elif piece_type == 'L':
                
                actions_for_piece.append('LHL')
                actions_for_piece.append('LVL')
                
                if (connected_right and is_locked == right[2]) or (connected_left and is_locked == left[2]):
                    if 'LVL' in actions_for_piece:
                        actions_for_piece.remove('LVL')
                        
                if ( connected_above and is_locked == above[2]) or (connected_below and is_locked == below[2]):
                    if 'LHL' in actions_for_piece:
                        actions_for_piece.remove('LHL')
                
                if (not connected_right and is_locked == right[2]) or (not connected_left and is_locked == left[2]):
                    if 'LHL' in actions_for_piece:
                        actions_for_piece.remove('LHL')
                
                if (not connected_above and is_locked == above[2]) or (not connected_below and is_locked == below[2]):
                    if 'LVL' in actions_for_piece:
                        actions_for_piece.remove('LVL')
                
            elif piece_type == 'V':
                
                actions_for_piece.append('VCL')
                actions_for_piece.append('VBL')
                actions_for_piece.append('VEL')
                actions_for_piece.append('VDL')
                
                if (connected_above and is_locked == above[2]) or (not connected_below and is_locked == below[2]):
                    
                    if 'VBL' in actions_for_piece:
                        actions_for_piece.remove('VBL')

                    if 'VEL' in actions_for_piece:
                        actions_for_piece.remove('VEL')
                
                if (connected_below and is_locked == below[2]) or (not connected_above and is_locked == above[2]):
                    
                    if 'VCL' in actions_for_piece:
                        actions_for_piece.remove('VCL')

                    if 'VDL' in actions_for_piece:
                        actions_for_piece.remove('VDL')
                
                if (connected_left and is_locked == left[2]) or (not connected_right and is_locked == right[2]):
                    
                    if 'VBL' in actions_for_piece:
                        actions_for_piece.remove('VBL')

                    if 'VDL' in actions_for_piece:
                        actions_for_piece.remove('VDL')
                
                if (connected_right and is_locked == right[2]) or (connected_left and is_locked == left[2]):
                    
                    if 'VCL' in actions_for_piece:
                        actions_for_piece.remove('VCL')

                    if 'VEL' in actions_for_piece:
                        actions_for_piece.remove('VEL')
                        
            possible_actions.append(actions_for_piece)
    
        return possible_actions    
    
    def loop_restrictions(self,unsolved_pieces: list):
        board_size = len(self.board)
        unsolved_pieces = []

        for row in range(board_size):
            for col in range(board_size):
                current_piece = self.board[row][col]
                coord = (row, col)
                is_locked = 'L'
                is_none = 'n'
                left, right = self.adjacent_horizontal_values(col, row)
                above, below = self.adjacent_vertical_values(col, row)
                connected_left = self.connected_left(left)
                connected_right = self.connected_right(right)
                connected_below = self.connected_down(below)
                connected_above = self.connected_above(above)
                piece_type = current_piece[0]


                if current_piece[2] != is_locked:
                    
                    if piece_type == 'F':
                        if connected_left and is_locked == left[2]:
                            self.board[row][col] = 'FEL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                            

                        elif connected_right and is_locked == right[2]:
                            self.board[row][col] = 'FDL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                            

                        elif connected_below and is_locked == below[2]:
                            
                            self.board[row][col] = 'FBL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                            

                        elif connected_above and is_locked == above[2]:
                            self.board[row][col] = 'FCL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                            

                        elif ((not connected_above and (is_locked == above[2] or is_none == above[2])) or above[0] == 'F') and \
                        ((not connected_right and (is_locked == right[2] or is_none == right[2])) or right[0] == 'F') and \
                        ((not connected_below and (is_locked == below[2] or is_none == below[2])) or below[0] == 'F'):
                            self.board[row][col] = 'FEL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                            

                        elif ((not connected_below and (is_locked == below[2] or is_none == below[2])) or below[0] == 'F') and \
                        ((not connected_left and (is_locked == left[2] or is_none == left[2])) or left[0] == 'F') and \
                        ((not connected_above and (is_locked == above[2] or is_none == above[2])) or above[0] == 'F'):
                            self.board[row][col] = 'FDL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                        
                        elif ((not connected_right and (is_locked == right[2] or is_none == right[2])) or right[0] == 'F') and \
                        ((not connected_left and (is_locked == left[2] or is_none == left[2])) or left[0] == 'F') and \
                        ((not connected_below and (is_locked == below[2] or is_none == below[2])) or below[0] == 'F'):
                            self.board[row][col] = 'FCL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                        
                        elif ((not connected_above and (is_locked == above[2] or is_none == above[2])) or above[0] == 'F') and \
                        ((not connected_left and (is_locked == left[2] or is_none == left[2])) or left[0] == 'F') and \
                        ((not connected_right and (is_locked == right[2] or is_none == right[2])) or right[0] == 'F'):
                            self.board[row][col] = 'FBL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                            
                        else:                          
                            unsolved_pieces.append(coord)
                            
                    elif piece_type == 'B':
                        if (not connected_above and is_locked== above[2]):
                            self.board[row][col] = 'BBL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)

                        elif(not connected_below and is_locked == below[2]):
                            self.board[row][col] = 'BCL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)

                        elif(not connected_right and is_locked == right[2]):
                            self.board[row][col] = 'BEL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)

                        elif(not connected_left and is_locked == left[2]):
                            self.board[row][col] = 'BDL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)

                        elif (connected_right and is_locked == right[2]) and (connected_left and is_locked == left[2]):
                            if (connected_above and is_locked == above[2]) or (not connected_below and is_locked == below[2]):
                                self.board[row][col] = 'BCL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                                
                            elif (connected_below and is_locked == below[2]) or (not connected_above and is_locked == above[2]):
                                
                                self.board[row][col] = 'BBL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)

                            else:
                                unsolved_pieces.append(coord)
                        
                        elif (connected_above and is_locked == above[2]) and (connected_below and is_locked == below[2]):
                           
                            if (connected_right and is_locked == right[2]) or (not connected_left and is_locked == left[2]):
                                self.board[row][col] = 'BDL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)

                            elif(connected_left and is_locked == left[2]) or (not connected_right and is_locked == right[2]):
                                
                                self.board[row][col] = 'BEL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)

                            else:
                                unsolved_pieces.append(coord)
                                
                        else:
                            
                            unsolved_pieces.append(coord)
                           
                            

                    elif piece_type == 'L':
                        if (connected_above and is_locked == above[2]) or (not connected_left and is_locked == left[2]) or \
                        (connected_below and is_locked == below[2]) or (not connected_right and is_locked == right[2]):
                            
                            self.board[row][col] = 'LVL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)

                        elif (not connected_above and is_locked == above[2]) or (connected_left and is_locked == left[2]) or \
                        (not connected_below and is_locked == below[2]) or (connected_right and is_locked == right[2]):
                            self.board[row][col] = 'LHL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)

                        else:
                            unsolved_pieces.append(coord)
                            

                    elif piece_type == 'V':

                        #VDL
                        if (connected_above and is_locked == above[2]) and (connected_right and is_locked == right[2]):
                            self.board[row][col] = 'VDL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                                continue
                        
                        if(connected_above and is_locked == above[2]):
                            if((connected_right and is_locked == right[2]) or (not connected_left and is_locked == left[2])):
                                self.board[row][col] = 'VDL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)
                        
                        if (not connected_below and (is_locked == below[2] or is_none == below[2])):
                            if((connected_right and is_locked == right[2]) or (not connected_left and (is_locked == left[2] or is_none == left[2]))):
                                self.board[row][col] = 'VDL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)

                        if(not connected_left and is_locked == left[2]):
                            if((connected_above and is_locked == above[2]) or (not connected_below and (is_locked == below[2] or is_none == below[2]))):
                                self.board[row][col] = 'VDL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)
                        


                        #VEL

                        if (connected_left and is_locked == left[2]) and (connected_below and is_locked == below[2]):
                            self.board[row][col] = 'VEL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                                continue
                            
                        elif (connected_below and is_locked == below[2]):                            
                            if((not connected_right and (is_locked == right[2] or is_none == right[2])) or (connected_left and is_locked == left[2])):
                                self.board[row][col] = 'VEL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)
                        
                        elif (not connected_right and (is_locked == right[2] or is_none == right[2])):
                            if(connected_below and is_locked == below[2]) or (not connected_above and (is_locked == above[2] or is_none == above[2])):
                                self.board[row][col] = 'VEL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)

                        elif (not connected_above and (is_locked == above[2] or is_none == above[2])):
                            if(connected_left and is_locked == left[2]):
                                self.board[row][col] = 'VEL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)


                        
                        #VBL
                        
                        if (connected_below and is_locked == below[2]) and (connected_right and is_locked == right[2]):
                            self.board[row][col] = 'VBL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                                continue

                        elif (not connected_above and (is_locked == above[2] or is_none == above[2])):
                            if ((not connected_left and (is_locked == left[2] or is_none == left[2])) or (connected_right and is_locked == right[2])):
                                self.board[row][col] = 'VBL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)


                        elif (not connected_left and (is_locked == left[2] or is_none == left[2])):
                            if ((not connected_above and (is_locked == above[2] or is_none == above[2])) or (connected_below and is_locked == below[2])):
                                self.board[row][col] = 'VBL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)
                        
                        elif (connected_right and is_locked == right[2]):
                        
                            if ((not connected_above and (is_locked == above[2] or is_none == above[2])) or (connected_below and is_locked == below[2])):
                                self.board[row][col] = 'VBL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)

                        
                        #VCL
                        if (connected_left and is_locked == left[2]) and (connected_above and is_locked == above[2]):
                            self.board[row][col] = 'VCL'
                            if coord in unsolved_pieces:
                                unsolved_pieces.remove(coord)
                                continue

                        elif (connected_above and is_locked == above[2]):
                            if ((connected_left and is_locked == left[2]) or (not connected_right and (is_locked == right[2] or is_none == right[2]))):
                                self.board[row][col] = 'VCL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)

                        elif (connected_left and is_locked == left[2]):
                            if (not connected_below and (is_locked == below[2] or is_none == below[2])) or (connected_above and is_locked == above[2]):
                                self.board[row][col] = 'VCL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)


                        elif (not connected_right and (is_locked == right[2] or is_none == right[2])):
                            if (not connected_below and (is_locked == below[2] or is_none == below[2])):
                                self.board[row][col] = 'VCL'
                                if coord in unsolved_pieces:
                                    unsolved_pieces.remove(coord)
                            else:
                                unsolved_pieces.append(coord)

                        else:
                            unsolved_pieces.append(coord)
                                                   
        unsolved_pieces = list(set(unsolved_pieces))
        return unsolved_pieces

    def resolve_next_pieces(self):
        unsolved_pieces = []
        previous_unsolved_pieces = None
        iterations_without_change = 0
        piece = []

        
        unsolved_pieces = self.loop_restrictions(unsolved_pieces)
        
        while unsolved_pieces:
            print(unsolved_pieces)
            if unsolved_pieces == previous_unsolved_pieces:
                iterations_without_change += 1
            else:
                iterations_without_change = 0

            if iterations_without_change >= 1:
                piece = self.actions_pieces(unsolved_pieces)
                print(piece)
                break

            previous_unsolved_pieces = unsolved_pieces.copy()
            unsolved_pieces = self.loop_restrictions(unsolved_pieces)
    
    def resolve_remaining_boarder_pieces(self, unsolved_pieces: list):
        board_size = len(self.board) - 1
        unsolved_pieces = list(set(unsolved_pieces))  # Remove duplicates initially

        previous_unsolved_pieces = None  # To store the state from the last iteration
        iterations_without_change = 0

        while unsolved_pieces:
            if unsolved_pieces == previous_unsolved_pieces:
                iterations_without_change += 1
            else:
                iterations_without_change = 0
            
            if iterations_without_change >= 2:
                break

            previous_unsolved_pieces = unsolved_pieces.copy()
            unsolved_pieces_copy = unsolved_pieces.copy()

            for coord in unsolved_pieces_copy:
                row = coord[0]
                col = coord[1]
                current_piece = self.board[row][col]
                piece_type = current_piece[0]
                is_locked = 'L'
                left, right = self.adjacent_horizontal_values(coord[1], coord[0])
                above, below = self.adjacent_vertical_values(coord[1], coord[0])

                if piece_type == 'F':
                    if self.connected_left(left) and is_locked == left[2]:
                        self.board[row][col] = 'FEL'
                        unsolved_pieces.remove((row, col))
                        continue

                    if self.connected_right(right) and is_locked == right[2]:
                        self.board[row][col] = 'FDL'
                        unsolved_pieces.remove((row, col))
                        continue

                    if self.connected_down(below) and is_locked == below[2]:
                        self.board[row][col] = 'FBL'
                        unsolved_pieces.remove((row, col))
                        continue

                    if self.connected_above(above) and is_locked == above[2]:
                        self.board[row][col] = 'FCL'
                        unsolved_pieces.remove((row, col))
                        continue

                    if ((not self.connected_left(left) and is_locked == left[2]) or left[0] == 'F') \
                        and ((not self.connected_right(right) and is_locked == right[2]) or right[0] == 'F'):
                        if below == 'None':
                            self.board[row][col] = 'FCL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'FBL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if ((not self.connected_above(above) and is_locked == above[2]) or above[0] == 'F') \
                        and ((not self.connected_down(below) and is_locked == below[2]) or below[0] == 'F'):
                        if left == 'None':
                            self.board[row][col] = 'FDL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'FEL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if coord == (0, 0):
                        if not self.connected_right(right) and is_locked == right[2]:
                            self.board[row][col] = 'FBL'
                            unsolved_pieces.remove((row, col))
                            continue
                        if not self.connected_down(below) and is_locked == below[2]:
                            self.board[row][col] = 'FDL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if coord == (0, board_size):
                        if not self.connected_left(left) and is_locked == left[2]:
                            self.board[row][col] = 'FBL'
                            unsolved_pieces.remove((row, col))
                            continue
                        if not self.connected_down(below) and is_locked == below[2]:
                            self.board[row][col] = 'FEL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if coord == (board_size, 0):
                        if not self.connected_right(right) and is_locked == right[2]:
                            self.board[row][col] = 'FCL'
                            unsolved_pieces.remove((row, col))
                            continue
                        if not self.connected_above(above) and is_locked == above[2]:
                            self.board[row][col] = 'FDL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if coord == (board_size, board_size):
                        if not self.connected_left(left) and is_locked == left[2]:
                            self.board[row][col] = 'FCL'
                            unsolved_pieces.remove((row, col))
                            continue
                        if not self.connected_above(above) and is_locked == above[2]:
                            
                            self.board[row][col] = 'FEL'
                            unsolved_pieces.remove((row, col))
                            continue

                if piece_type == 'V':
                    if self.connected_left(left) and is_locked == left[2]:
                        if below == 'None':
                            self.board[row][col] = 'VCL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'VEL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if not self.connected_left(left) and is_locked == left[2]:
                        if below == 'None':
                            self.board[row][col] = 'VDL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'VBL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if self.connected_right(right) and is_locked == right[2]:
                        if below == 'None':
                            self.board[row][col] = 'VDL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'VBL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if not self.connected_right(right) and is_locked == right[2]:
                        if below == 'None':
                            self.board[row][col] = 'VCL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'VEL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if self.connected_down(below) and is_locked == below[2]:
                        if left == 'None':
                            self.board[row][col] = 'VBL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'VEL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if not self.connected_down(below) and is_locked == below[2]:
                        if left == 'None':
                            self.board[row][col] = 'VDL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'VCL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if self.connected_above(above) and is_locked == above[2]:
                        if left == 'None':
                            self.board[row][col] = 'VDL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'VCL'
                            unsolved_pieces.remove((row, col))
                            continue

                    if not self.connected_above(above) and is_locked == above[2]:
                        if left == 'None':
                            self.board[row][col] = 'VBL'
                            unsolved_pieces.remove((row, col))
                            continue
                        else:
                            self.board[row][col] = 'VEL'
                            unsolved_pieces.remove((row, col))
                            continue
            
        return
          
    def init_board(self):
        board_size = len(self.board)-1
        unlocked_pieces = []
        # up_left = (0, 0)
        # up_right = (0, board_size)
        # down_left = (board_size, 0)
        # down_right = (board_size, board_size)

        #VERIFY BOARDERS

        #UP LEFT
        current_piece = self.board[0][0]
        piece_type = current_piece[0]
        left,right = self.adjacent_horizontal_values(0,0)
        above,below = self.adjacent_vertical_values(0,0)

        if piece_type == 'V':
            
            self.board[0][0] = 'VBL'

        if piece_type == 'F':
            if right[0] == 'F' or below[0] in {'L','B'} :
                self.board[0][0] = 'FBL'

            if below[0] == 'F'or right[0] in {'L','B'}:
                self.board[0][0] = 'FDL'

            else: unlocked_pieces.append((0,0))


        #UP RIGHT
        current_piece = self.board[0][board_size]
        piece_type = current_piece[0]
        left,right = self.adjacent_horizontal_values(board_size, 0)
        above,below = self.adjacent_vertical_values(board_size, 0)

        if current_piece[0] == 'V':
            self.board[0][board_size] = 'VEL'

        if piece_type == 'F':
            if left[0] == 'F' or below[0] in {'L','B'}:
                self.board[0][board_size] = 'FBL'
            if below[0] == 'F' or left[0] in {'L','B'}:
                self.board[0][board_size] = 'FEL'
            else: unlocked_pieces.append((0,board_size))


        #DOWN LEFT
        current_piece = self.board[board_size][0]
        piece_type = current_piece[0]
        left,right = self.adjacent_horizontal_values(0,board_size)
        above,below = self.adjacent_vertical_values(0,board_size)

        if current_piece[0] == 'V':
            self.board[board_size][0] = 'VDL'

        if piece_type == 'F':

            if right[0] == 'F' or above[0] in {'L','B'}:
                self.board[board_size][0] = 'FCL'
            if above[0] == 'F' or right[0] in {'L','B'}:
                self.board[board_size][0] = 'FDL'
            else: unlocked_pieces.append((board_size,0))


        #DOWN RIGHT
        current_piece = self.board[board_size][board_size]
        piece_type = current_piece[0]
        left,right = self.adjacent_horizontal_values(board_size,board_size)
        above,below = self.adjacent_vertical_values(board_size,board_size)
        if current_piece[0] == 'V':
            self.board[board_size][board_size] = 'VCL'
        
        if piece_type == 'F':
            if left[0] == 'F' or above[0] in {'L','B'}:
                self.board[board_size][board_size] = 'FCL'
            if above[0] == 'F' or left[0] in {'L','B'}:
                self.board[board_size][board_size] = 'FEL'
            else: unlocked_pieces.append((board_size,board_size))

        lados = [0,board_size]

        # VERIFICA COLUNAS DA BORDA
        for i in range(2):
            for row in range(board_size + 1):
                current_piece = self.board[row][lados[i]]
                left,right = self.adjacent_horizontal_values(lados[i],row)
                above,below = self.adjacent_vertical_values(lados[i],row)
                
                if current_piece[2] != 'L':
                    piece_type = current_piece[0]

                    if piece_type == 'L':
                            self.board[row][lados[i]] = 'LVL'
                            continue
                    
                    if lados[i] == 0:
                        if piece_type == 'B':
                                self.board[row][lados[i]] = 'BDL'
                                continue

                        if piece_type == 'F':
                            
                            if right[0] == 'F' and below[0] == 'F':                             
                                self.board[row][lados[i]] = 'FCL'
                                continue
                            if right[0] == 'F' and above[0] == 'F':
                                self.board[row][lados[i]] = 'FBL'
                                continue
                            if above[0] == 'F' and below[0] == 'F':
                                
                                self.board[row][lados[i]] = 'FDL'
                                continue
                            else: 
                                
                                unlocked_pieces.append((row,lados[i]))
                                continue
                        else: 
                            unlocked_pieces.append((row,lados[i]))
                            continue
                        
                    if lados[i] == board_size:
                    
                        if piece_type == 'B':
                            self.board[row][lados[i]] = 'BEL'
                            continue
                        
                        if piece_type == 'F':

                            if left[0] == 'F' and above[0] == 'F':
                                self.board[row][lados[i]] = 'FBL'
                                continue
                            if left[0] == 'F' and below[0] == 'F':
                                self.board[row][lados[i]] = 'FCL'
                                continue
                            if above[0] == 'F' and below[0] == 'F':
                                self.board[row][lados[i]] = 'FEL'
                                continue
                            else: 
                                
                                unlocked_pieces.append((row,lados[i]))
                                continue
                        else: 
                                            
                            unlocked_pieces.append((row,lados[i]))
                            continue
                            
                    else: 
                        unlocked_pieces.append((row,lados[i]))
                        continue
                

        # VERIFICA LINHAS DA BORDA
        for i in range(2):
            for col in range(board_size + 1):
                
                current_piece = self.board[lados[i]][col]
                left,right = self.adjacent_horizontal_values(row,lados[i])
                above,below = self.adjacent_vertical_values(row,lados[i])
                
                if current_piece[2] != 'L':
                                
                    piece_type = current_piece[0]

                    if piece_type == 'L':
                            self.board[lados[i]][col] = 'LHL'
                            continue
                    
                    if lados[i] == 0:
                        
                        if piece_type == 'B':
                            self.board[lados[i]][col] = 'BBL'
                            continue

                        if piece_type == 'F':
                            
                            if right[0] == 'F' and below[0] == 'F':
                                self.board[lados[i]][col] = 'FEL'
                                continue

                            if left[0] == 'F' and below[0] == 'F':
                                self.board[lados[i]][col] = 'FDL'
                                continue
                            if right[0] == 'F' and left[0] == 'F':
                                self.board[lados[i]][col] = 'FBL'
                                continue
                            else: 
                                
                                unlocked_pieces.append((lados[i],col))
                                continue
                        else: 
                            unlocked_pieces.append((lados[i],col))
                            continue
                    
                    if lados[i] == board_size:
                        
                        if piece_type == 'B':
                            
                            self.board[lados[i]][col] = 'BCL'
                            continue

                        if piece_type == 'F':
                            
                            if right[0] == 'F' and above[0] == 'F':
                                self.board[lados[i]][col] = 'FEL'
                                continue
                            if left[0] == 'F' and above[0] == 'F':
                                self.board[lados[i]][col] = 'FDL'
                                continue
                            if right[0] == 'F' and left[0] == 'F':
                                self.board[lados[i]][col] = 'FCL'
                                continue
                            else: 
                                unlocked_pieces.append((lados[i],col))
                                continue
                        else:
                            unlocked_pieces.append((lados[i], col))
                            continue
                        
                    else: 
                        unlocked_pieces.append((lados[i], col))
                        continue

        self.resolve_remaining_boarder_pieces(unlocked_pieces)
        self.resolve_next_pieces()
        
    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 pipe.py < test-01.txt

            > from sys import stdin
            > line = stdin.readline().split()
        """
        content = stdin.readlines()

        board = []

        for line in content:

            elements = line.strip().split("\t")

            elements = [str(element) + 'U' for element in elements ]

            board.append(elements)


        return Board(board)

    def __str__(self):
        """Retorna uma string formatada do tabuleiro para impressao."""
        rows = ['\t'.join(element[:2 ] for element in row) for row in self.board]
        return '\n'.join(rows)

class PipeMania(Problem):

    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""

        self.initial = PipeManiaState(board)

    def actions(self, state: PipeManiaState, unsolved_pieces: list):
        """Retorna uma lista de acoes que podem ser executadas a
        partir do estado passado como argumento."""

        possible_actions = []
        possible_actions_correct = []
        possible_actions = state.board.actions_pieces(self, unsolved_pieces)
        possible_actions_correct = state.board.correct_form(possible_actions)

        return possible_actions_correct
        
    def is_correctly_connected(self, state: PipeManiaState, pipe, row: int, col: int):
        """Verifica se uma peca esta corretamente conectada."""
        desc = state.board.description
        above, below = state.board.adjacent_vertical_values(row, col)
        left, right = state.board.adjacent_horizontal_values(row, col)

        return (
            (desc[pipe [:-1]][LEFT] == (desc[left][RIGHT] if left else 0)) and
            (desc[pipe [:-1]][ABOVE] == (desc[above][DOWN] if above else 0)) and
            (desc[pipe [:-1]][RIGHT] == (desc[right][LEFT] if right else 0)) and
            (desc[pipe [:-1]][DOWN] == (desc[below][ABOVE] if below else 0))
        )

    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A acao a executar deve ser uma
        das presentes na lista obtida pela execucao de
        self.actions(state)."""

        row, col, new_piece = action
        state.board[row][col] = new_piece
        
        return state
        
    def goal_test(self, state: PipeManiaState):
        """Retorna True se e so se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posicoes do tabuleiro
        estao preenchidas de acordo com as regras do problema."""
        
        #board_size = len(state.board)
        is_locked = 'L'

        for row in range(len(state.board[0])):
            for col in range(len(state.board[0])):
                current_piece = state.board[row][col]
                if current_piece[2] != is_locked:
                    return False
        return True

    def h(self, node: Node):
        """Funcao heuristica utilizada para a procura A*."""
        # TODO
        pass

if __name__ == "__main__":

    initial_board = Board.parse_instance()  
    pipe_mania_problem = PipeMania(initial_board)
    
    solution_node = depth_first_tree_search(pipe_mania_problem)
    # solution_node = depth_first_tree_search(pipe_mania_problem)
    # if solution_node:     
    #     solution_board = solution_node.state.board
    #     print(solution_board)
    # is_goal = pipe_mania_problem.goal_test(pipe_mania_problem.initial)
    
    # Imprimir o resultado
   # print("O estado inicial é um estado objetivo?", is_goal)
    print(initial_board)
    pass
