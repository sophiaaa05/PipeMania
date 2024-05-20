# pipe.py: Template para implementacao do projeto de Inteligencia Artificial 2023/2024.
# Devem alterar as classes e funcoes neste ficheiro de acordo com as instrucoes do enunciado.
# Além das funcoes e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
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
    
    def resolve_remaining_pieces(self):
        board_size = len(self.board)-1

        for row in range(len(self.board) - 1):
            for col in range(len(self.board) - 1):
                current_piece = self.get_value(row,col)
                piece_type = current_piece[0]
                lock = current_piece[2]
                left,right = self.adjacent_horizontal_values(col, row)
                above,below = self.adjacent_vertical_values(col, row)

                if lock == 'U':
                    if piece_type == 'B':

    
        
    def init_board(self):
        board_size = len(self.board)-1
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

        if  piece_type== 'V':
            self.board[0][0] = 'VBL'

        if piece_type == 'F':
            if right[0] == 'F' or below[0] in {'L','B'} :
                self.board[0][0] = 'FBL'
            if below[0] == 'F'or right[0] in {'L','B'}:
                self.board[0][0] = 'FDL'


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


        #DOWN LEFT
        current_piece = self.board[board_size][0]
        piece_type = current_piece[0]
        left,right = self.adjacent_horizontal_values(0,board_size)
        above,below = self.adjacent_vertical_values(0,board_size)

        if current_piece[0] == 'V':
            self.board[board_size][0] = 'VDL'

        if piece_type == 'F':
  
            if right[0] == 'F' or above in {'LV','BD'}:
                self.board[board_size][0] = 'FCL'
            if above[0] == 'F' or right in {'LH','BC'}:
                self.board[board_size][0] = 'FDL'
  

        #DOWN RIGHT
        current_piece = self.board[board_size][board_size]
        piece_type = current_piece[0]
        left,right = self.adjacent_horizontal_values(board_size,board_size)
        above,below = self.adjacent_vertical_values(board_size,board_size)
        if current_piece[0] == 'V':
            self.board[board_size][board_size] = 'VCL'
        
        if piece_type == 'F':
            if left[0] == 'F' or above in {'L','B'}:
                self.board[board_size][board_size] = 'FCL'
            if above[0] == 'F' or left in {'L','B'}:
                self.board[board_size][board_size] = 'FEL'

        lados = [0,board_size]

        # VERIFICA COLUNAS DA BORDA
        for i in range(2):
            for row in range(board_size):
                current_piece = self.board[row][lados[i]]
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
                            self.board[row][lados[i]] = 'FEL'
                            continue
                        if left[0] == 'F' and below[0] == 'F':
                            self.board[row][lados[i]] = 'FDL'
                            continue
                        if above[0] == 'F' and below[0] == 'F':
                            self.board[row][lados[i]] = 'FDL'
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

                

        # VERIFICA LINHAS DA BORDA
        for i in range(2):
            for col in range(board_size):
                current_piece = self.board[lados[i]][col]
                piece_type = current_piece[0]

                if piece_type == 'L':
                        self.board[lados[i]][col] = 'LVL'
                        continue
                
                if lados[i] == 0:
                    if piece_type == 'B':
                        self.board[lados[i]][col] = 'BBL'
                        continue

                    if piece_type == 'F':

                        if right[0] == 'F' and above[0] == 'F':
                            self.board[lados[i]][col] = 'FBL'
                            continue
                        if right[0] == 'F' and below[0] == 'F':
                            self.board[lados[i]][col] = 'FCL'
                            continue
                        if right[0] == 'F' and left[0] == 'F':
                            self.board[lados[i]][col] = 'FBL'
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

        self.resolve_remaining_pieces()
                
                



    # def resolve_pipes_unlocked(pipes_unlocked):
    #     """Resolve os pipes na boarda que ficaram a faltar dar lock"""
    #     for pipe in pipes_unlocked:
    #         if( )

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
        rows = ['\t'.join(element[:2] for element in row) for row in self.board]
        return '\n'.join(rows)



class PipeMania(Problem):

    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""

        self.initial = PipeManiaState(board)
    
    def rotate_clockwise(self, name_pipe:str):
        """Rotate a pipe 90 degrees clockwise."""
        if name_pipe not in Board.piece_clockwise:
            return "None: ????"
        return Board.piece_clockwise[name_pipe]
        

    def rotate_anticlockwise(self, name_pipe:str):
        """Rotate a str 90 degrees anti-clockwise."""
        if name_pipe not in Board.piece_anticlockwise:
            return "None: ????"
        return Board.piece_anticlockwise[name_pipe]
        


    def actions(self, state: PipeManiaState):
        """Retorna uma lista de acoes que podem ser executadas a
        partir do estado passado como argumento."""

        possible_actions = []
        up_left=(0,0)
        down_left = (0,len(state.board.board)-1)
        up_right = (len(state.board.board)-1,0)
        down_right =(len(state.board.board)-1,len(state.board.board)-1)
        

        for row in range(len(state.board.board)):
            for col in range(len(state.board.board[row])):
                current_piece = state.board.board[col][row]
                piece_type = current_piece[0]
                side = current_piece[1]

                above, below = state.board.adjacent_vertical_values(row, col)
                left, right = state.board.adjacent_horizontal_values(row, col)

                for rotation in [True, False]:  # True for clockwise, False for anticlockwise
                    rotated_piece = self.rotate_clockwise(current_piece) if rotation else self.rotate_anticlockwise(current_piece)
                    if self.is_correctly_connected(state, row, col):
                        possible_actions.append((row, col, rotation))


        return possible_actions
        
    def is_correctly_connected(self, state: PipeManiaState, pipe, row: int, col: int):
        """Verifica se uma peca esta corretamente conectada."""
        desc = Board.pipe_description
        above, below = state.board.adjacent_vertical_values(row, col)
        left, right = state.board.adjacent_horizontal_values(row, col)

        return (
            (desc[pipe][LEFT] == (desc[left][RIGHT] if left else 0)) and
            (desc[pipe][ABOVE] == (desc[above][DOWN] if above else 0)) and
            (desc[pipe][RIGHT] == (desc[right][LEFT] if right else 0)) and
            (desc[pipe][DOWN] == (desc[below][ABOVE] if below else 0))
        )

                        

    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A acao a executar deve ser uma
        das presentes na lista obtida pela execucao de
        self.actions(state)."""

        row, col, clockwise = action
        new_board = [list(col) for col in state.board.board]  
        if clockwise:
            new_board[row][col] = self.rotate_clockwise(new_board[row][col])
        else:
            new_board[row][col] = self.rotate_anticlockwise(new_board[row][col])
        return PipeManiaState(new_board)
        

    def goal_test(self, state: PipeManiaState):
        """Retorna True se e so se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posicoes do tabuleiro
        estao preenchidas de acordo com as regras do problema."""

        for row in range(len(state.board.board)):
            for col in range(len(state.board.board[row])):
                pipe = state.board.get_value(row, col)
                if not self.is_correctly_connected(state, pipe, row, col):
                    return False
        return True

    def h(self, node: Node):
        """Funcao heuristica utilizada para a procura A*."""
        # TODO
        pass

    



if __name__ == "__main__":

    initial_board = Board.parse_instance()  
    pipe_mania_problem = PipeMania(initial_board)
    # solution_node = depth_first_tree_search(pipe_mania_problem)
    # solution_node = depth_first_tree_search(pipe_mania_problem)
    # if solution_node:     
    #     solution_board = solution_node.state.board
    #     print(solution_board)
    # is_goal = pipe_mania_problem.goal_test(pipe_mania_problem.initial)
    
    # Imprimir o resultado
   # print("O estado inicial é um estado objetivo?", is_goal)
    print(initial_board)
    pass
