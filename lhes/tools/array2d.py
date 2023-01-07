class Array2D:

    def __init__(self, width: int, height: int, default_value=0):
        self.width = width
        self.height = height
        self.default_value = 0
        self._array: list[list[float]] = []
        for y in range(self.height):
            self._array.append([])
            for _ in range(self.width):
                self._array[y].append(default_value)

    def get(self, column, row):
        return self._array[row][column]

    def set(self, column, row, value):
        self._array[row][column] = value

    def __str__(self):
        result = f"{self.__class__}[{self.width}, {self.height}] (Default value = '{self.default_value}') \n"
        result += "    "
        for x in range(self.width):
            result += f"{x:3} "
        result += "\n"
        for y in range(self.height):
            result += f"{y:3} "
            for x in range(self.width):
                result += f"{self.get(x, y):3} "
            result += "\n"
        return result


class SquareArray2D(Array2D):
    def __init__(self, width: int, default_value=0):
        super().__init__(width, width, default_value)
