# pipe.py: Template para implementação do projeto de Inteligência Artificial 2023/2024.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 106748 Inês Antunes
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
    """Representação interna de um tabuleiro de PipeMania."""
    
    pipe_description = {
        'FC': (0,1,0,0), 'FB': (0,0,0,1), 'FE': (1,0,0,0), 'FD': (0,0,1,0),
        'BC': (1,1,1,0), 'BB': (1,0,1,1), 'BE': (1,1,0,1), 'BD': (0,1,1,1),
        'VC': (1,1,0,0), 'VB': (0,0,1,1), 'VE': (1,0,0,1), 'VD': (0,1,1,0),
        'LH': (1,0,1,0), 'LV': (0,1,0,1), 'None': (0,0,0,0)
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
        """Devolve o valor na respetiva posição do tabuleiro."""
        return self.board[col][row]
        
    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        below = self.get_value(row, col+1) if col < len(self.board)-1 else None
        above = self.get_value(row, col-1) if col > 0 else None
        return above, below

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        left = self.get_value(row-1, col) if row > 0 else None
        right = self.get_value(row+1, col) if row < len(self.board[0])-1 else None
        return left, right
        
    def init_board(self):
        up_left = (0, 0)
        up_right = (0, len(self.board)-1)

        down_left = (len(self.board[0])-1, 0)

        down_right = (len(self.board[0])-1, len(self.board)-1)

        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                current_piece = self.board[col][row]
                piece_type = current_piece[0]
                piece_location = (col, row)

                if piece_location == up_left and piece_type == 'V':
                    self.board[col][row] = 'VB'
                if piece_location == down_left and piece_type == 'V':
                    self.board[col][row] = 'VD'
                if piece_location == up_right and piece_type == 'V':
                    self.board[col][row] = 'VE'
                if piece_location == down_right and piece_type == 'V':
                    self.board[col][row] = 'VC'
                if col == 0:
                    if piece_type == 'L':
                        self.board[col][row] = 'LV'
                    if piece_type == 'B':
                        self.board[col][row] = 'BD'
                if col == len(self.board) - 1:
                    if piece_type == 'L':
                        self.board[col][row] = 'LV'
                    if piece_type == 'B':
                        self.board[col][row] = 'BE'
                if row == 0:
                    if piece_type == 'L':
                        self.board[col][row] = 'LH'
                    if piece_type == 'B':
                        self.board[col][row] = 'BB'
                if row == len(self.board) - 1:
                    if piece_type == 'L':
                        self.board[col][row] = 'LH'
                    if piece_type == 'B':
                        self.board[col][row] = 'BC'
                



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

            elements = [str(element) for element in elements ]

            board.append(elements)


        return Board(board)

    def __str__(self):
        """Retorna uma string formatada do tabuleiro para impressão."""
        cols = ['\t'.join(col) for col in self.board]
        return '\n'.join(cols)
        

    # TODO: outros metodos da classe


class PipeMania(Problem):

    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""

        self.initial = PipeManiaState(board)
    
    

    def rotate_clockwise(self, name_pipe):
        """Rotate a pipe 90 degrees clockwise."""
        if name_pipe not in self.piece_clockwise:
            return "None: ????"
        return self.piece_clockwise(name_pipe)
        

    def rotate_anticlockwise(self, name_pipe):
        """Rotate a str 90 degrees anti-clockwise."""
        if name_pipe not in self.piece_anticlockwise:
            return "None: ????"
        return self.piece_anticlockwise(name_pipe)
        


    def actions(self, state: PipeManiaState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""

        possible_actions = []
        up_left=(0,0)
        down_left = (0,len(state.board))
        up_right = (len(state.board),0)
        down_right =(len(state.board),len(state.board))
        

        for row in range(len(state.board)):
            for col in range(len(state.board[row])):
                current_piece = state.board[col][row]
                piece_type = current_piece[0]
                side = current_piece[1]

                above, below = state.board.adjacent_vertical_values(row, col)
                left, right = state.board.adjacent_horizontal_values(row, col)

                for rotation in [True, False]:  # True for clockwise, False for anticlockwise
                    rotated_piece = self.rotate_clockwise(current_piece) if rotation else self.rotate_anticlockwise(current_piece)
                    if self.is_correctly_connected(rotated_piece, above, below, left, right):
                        possible_actions.append((row, col, rotation))


               
                
                # piece_location = (col,row)

                # if piece_location == up_left:
                #     if current_piece in {'FC','FD'}:
                #         possible_actions.append((col,row,True))
                #     elif current_piece in {'FB' ,'FE'}:
                #         possible_actions.append((col,row,False))

                #     elif current_piece == 'VC':
                #         possible_actions.append((col,row,True))
                #         possible_actions.append((col,row,False))
                #     elif current_piece == 'VE':
                #         possible_actions.append((col,row,False))
                #     elif current_piece == 'VD':
                #         possible_actions.append((col,row,True))

                # elif piece_location ==  down_left:
                #     if current_piece in {'FC','FE'}:
                #         possible_actions.append((col,row,True))
                #     elif current_piece in {'FD', 'FB'}:
                #         possible_actions.append((col,row,False))

                #     elif current_piece == 'VC':
                #         possible_actions.append((col,row,True))
                #     elif current_piece == 'VE':
                #         possible_actions.append((col,row,False))
                #         possible_actions.append((col,row,True))
                #     elif current_piece == 'VB':
                #         possible_actions.append((col,row,False))

                # elif piece_location ==  up_right:
                #     if current_piece in {'FC', 'FE'}:
                #         possible_actions.append((col,row,False))
                #     elif current_piece in {'FD','FB'}:
                #         possible_actions.append((col,row,True))

                #     elif current_piece == 'VC':
                #         possible_actions.append((col,row,False))
                #     elif current_piece == 'VE':
                #         possible_actions.append((col,row,False))
                #         possible_actions.append((col,row,True))
                #     elif current_piece == 'VB':
                #         possible_actions.append((col,row,True))

                # elif piece_location == down_right:
                #     if current_piece in {'FC', 'FD'}:
                #         possible_actions.append((col,row,False))
                #     elif current_piece in ['FB' ,'FE']:
                #         possible_actions.append((col,row,True))

                #     elif current_piece == 'VC':
                #         possible_actions.append((col,row,True))
                #         possible_actions.append((col,row,False))
                #     elif current_piece == 'VE':
                #         possible_actions.append((col,row,True))
                #     elif current_piece == 'VD':
                #         possible_actions.append((col,row,False))
                
                # elif col == 0 or col == len(state.board):
                #     if current_piece in {'LH','BE','FE','FD'}:
                #         possible_actions.append((col,row,True))
                #         possible_actions.append((col,row,False))

                #     elif current_piece in {'BC','FC'}:
                #         possible_actions.append((col,row,True))

                #     elif current_piece in {'BB','FB'}:
                #         possible_actions.append((col,row,False))

                # elif row == 0 or row == len(state.board):
                #     if current_piece in {'LV', 'BC','FB','FC'}:
                #         possible_actions.append((col,row,True))
                #         possible_actions.append((col,row,False))
                #     elif current_piece in {'BD','FD'}:
                #         possible_actions.append((col,row,True))
                #     elif current_piece in {'BE','FE'}:
                #         possible_actions.append((col,row,False))

        return possible_actions
        
    def is_correctly_connected(self, pipe, above, below, left, right):
        """Verifica se uma peça está corretamente conectada."""
        desc = Board.pipe_description
        return (
            (pipe == "None" or
            (desc[pipe][LEFT] == (desc[left][RIGHT] if left else 0)) and
            (desc[pipe][ABOVE] == (desc[above][DOWN] if above else 0)) and
            (desc[pipe][RIGHT] == (desc[right][LEFT] if right else 0)) and
            (desc[pipe][DOWN] == (desc[below][ABOVE] if below else 0)))
        )


        
                        

    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""

        row, col, clockwise = action
        new_board = [list(col) for col in state.board]  
        if clockwise:
            new_board[row][col] = self.rotate_clockwise(new_board[row][col])
        else:
            new_board[row][col] = self.rotate_anticlockwise(new_board[row][col])
        return PipeManiaState(new_board)
        

    def goal_test(self, state: PipeManiaState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""

        for row in state.board.board:
            for col in row:
                if self.is_incorrectly_connected(state, row, col): 
                    return False
        return True

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    



if __name__ == "__main__":

    initial_board = Board.parse_instance()  
    pipe_mania_problem = PipeMania(initial_board)
    solution_node = depth_first_tree_search(pipe_mania_problem)

    if solution_node:
        
        solution_board = solution_node.state.board
        print(solution_board)

    #doesent work yet be patient
   # solution_node = depth_first_trese_search(pipe_mania_problem)

    # if solution_node:
    #     print("Solution found:")
    
    # else:

    #     print("No solution found.")


    #TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass
