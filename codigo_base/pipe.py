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

    def __init__(self, board):

        self.board = board

    def get_value(self, row: int, col: int) -> str:
        """Devolve o valor na respetiva posição do tabuleiro."""

        return self.board[col][row]
        

    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""

        
        below = self.board[col +1][row] if col < len(self.board)-1 else None
        above = self.board[col-1][row] if col > 0 else None

        
        return above,below

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""

        left = self.board[col ][row-1] if row > 0 else None
        right = self.board[col][row+1] if row < len(self.board)-1 else None


        return left,right
        

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
        

    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""

        self.initial_state = PipeManiaState(board)

    def rotate_clockwise(str):
        """Rotate a pipe 90 degrees clockwise."""
        if str == 'FC':
            return 'FD'
        elif str == 'FB':
            return 'FE'
        elif str == 'FE':
            return 'FC'
        elif str == 'FD':
            return 'FB'
        elif str == 'BC':
            return 'BD'
        elif str == 'BB':
            return 'BE'
        elif str == 'BE':
            return 'BC'
        elif str == 'BD':
            return 'BB'
        elif str == 'VC':
            return 'VD'
        elif str == 'VB':
            return 'VE'
        elif str == 'VE':
            return 'VC'
        elif str == 'VD':
            return 'VB'
        elif str == 'LH':
            return 'LV'
        elif str == 'LV':
            return 'LH'

    def rotate_anticlockwise(str):
        """Rotate a str 90 degrees anti-clockwise."""
        if str == 'FC':
            return 'FE'
        elif str == 'FB':
            return 'FD'
        elif str == 'FE':
            return 'FB'
        elif str == 'FD':
            return 'FC'
        elif str == 'BC':
            return 'BE'
        elif str == 'BB':
            return 'BD'
        elif str == 'BB':
            return 'BB'
        elif str == 'BD':
            return 'BC'
        elif str == 'VC':
            return 'VE'
        elif str == 'VB':
            return 'VD'
        elif str == 'VE':
            return 'VB'
        elif str == 'VD':
            return 'VC'
        elif str == 'LH':
            return 'LV'
        elif str == 'LV':
            return 'LH'


    def actions(self, state: PipeManiaState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""

        possible_actions = []

        pass
        
        

    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""

        row, col, clockwise = action
        new_board = [list(row) for row in state.board]  
        if clockwise:
            #não sei porquê que não está a reconhecer as funções *angry emojis*
            new_board[row][col] = rotate_clockwise(new_board[row][col])
        else:
            new_board[row][col] = rotate_anticlockwise(new_board[row][col])
        return PipeManiaState(new_board)
        

    def goal_test(self, state: PipeManiaState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""

        for row in state.board:
            for pipe in row:
                if is_incorrectly_connected(state, pipe): #TODO: esta função :)
                    return False
        return True

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe



if __name__ == "__main__":

    initial_board = Board.parse_instance()  
    pipe_mania_problem = PipeMania(initial_board)

    #doesent work yet be patient
    solution_node = depth_first_tree_search(pipe_mania_problem)

    if solution_node:
        print("Solution found:")
    
    else:

        print("No solution found.")


    # print(board.adjacent_vertical_values(0, 0))
    # print(board.adjacent_horizontal_values(0, 0))
    # print(board.adjacent_vertical_values(1, 1))
    # print(board.adjacent_horizontal_values(1, 1))



    #TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass
