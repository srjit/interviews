
# Steps
# 1. Design the board
# 2. Design the pieces
# 3. Program the movements

class Piece:

    def __init__(self, name, color, alive=True):

        self.name = name
        self.color = color
        self.alive = alive

    def __str__(self):
        return f"{self.color} {self.name} : Alive: {self.alive}"
    

def get_pieces(color: str):

    pieces = [
            [Piece("Pawn", color)] * 8,
            [Piece("Rook", color)] * 2, 
            [Piece("Knight", color)] * 2,
            [Piece("Bishop", color)] * 2,
            [Piece("Queen", color)],
            [Piece("King", color)]
        ]
    
    return [item for items in pieces for item in items]


class Board:

    class Square:

        def __init__(self, rowid: str, columnid: int, piece: Piece=None):
            self.rowid = rowid
            self.columnid = columnid
            self.piece = piece

        def set_piece(self, piece_):
            self.piece = piece_

        def __str__(self) -> str:
            return f"{self.rowid} {self.columnid} : {self.piece.color} {self.piece.name}"


    def __init__(self):

        self.columns = list(range(1,9))
        self.rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        self.positions = [[self.Square(i, j) for j in self.columns] for i in self.rows]
        self.white_pieces = get_pieces("white")
        self.black_pieces = get_pieces("black")

        self.set_inital_position(self.white_pieces, "white")
        self.set_inital_position(self.white_pieces, "black")
        
        
    def set_inital_position(self, pieces: list, color: str):
        '''
        For easiness set white to be at the bottom
        '''
        def set_pieces(i_pawns, i_army):
            [self.positions[i_pawns][x].set_piece(piece) for x, piece in zip(list(range(8)), pieces[:8])]

            # Rooks
            self.positions[i_army][0].set_piece(pieces[8])
            self.positions[i_army][7].set_piece(pieces[9])

            # Knights
            self.positions[i_army][1].set_piece(pieces[10])
            self.positions[i_army][6].set_piece(pieces[11])
            
            # Bishops
            self.positions[i_army][2].set_piece(pieces[12])
            self.positions[i_army][5].set_piece(pieces[13])

            # Queen
            self.positions[i_army][3].set_piece(pieces[14])
            # King
            self.positions[i_army][4].set_piece(pieces[15])

        if color == "white":   
            set_pieces(1, 0)
        else:
            set_pieces(6, 7)


    def move(piece, start_pos, end_pos):
        NotImplementedError("Hasnt been implemented yet")


        

if __name__ == "__main__":

    board = Board()

    import ipdb
    ipdb.set_trace()













    