from PIL import Image

WIDTH = 7
CELL_SIZE = 8
# inner size + 1

class MazeBlock:
    __image = None
    __color = (0, 0, 0)
    __h_wall = None
    __v_wall = None

    def __init__(self, color=None):
        self.__image = Image.new('RGBA', (CELL_SIZE * WIDTH + 1, CELL_SIZE * WIDTH + 1))
        if color is not None:
            self.__color = color
        self.__h_wall = Image.new('RGBA', (CELL_SIZE + 1, 1), color=self.__color)
        self.__v_wall = Image.new('RGBA', (1, CELL_SIZE + 1), color=self.__color)

    def add_wall(self, row: int, col: int, direction: int):
        '''Add wall to maze block at given coords and direction

        `direction`: 0, 1, 2, 3 for N, E, S, W walls respectively'''

        y = row * CELL_SIZE
        x = col * CELL_SIZE

        if direction == 0: # N wall
            self.__image.paste(self.__h_wall, (x, y))
        if direction == 1: # E wall
            x += CELL_SIZE
            self.__image.paste(self.__v_wall, (x, y))
        if direction == 2: # S wall
            y += CELL_SIZE
            self.__image.paste(self.__h_wall, (x, y))
        if direction == 3: # W wall
            self.__image.paste(self.__v_wall, (x, y))

    def export(self):
        '''Return `Image` object with current state'''
        return self.__image
    
    def parse_data(self, data: list):
        '''Parse list of hex strings (CS240 schema) and add walls'''
        for row, row_string in enumerate(data):
            for col, char in enumerate(row_string):
                value = int(char, 16)
                if value // 8 == 1: # N wall
                    self.add_wall(row, col, 0)
                if value % 8 // 4 == 1: # E wall
                    self.add_wall(row, col, 1)
                if value % 4 // 2 == 1: # S wall
                    self.add_wall(row, col, 2)
                if value % 2 == 1: # W wall
                    self.add_wall(row, col, 3)
