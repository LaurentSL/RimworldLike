class Array2D:

    def __init__(self, width: int, height: int, default_value=None):
        self.width = width
        self.height = height
        self.default_value = default_value
        self._array: list[list[object]] = []
        for y in range(self.height):
            self._array.append([])
            for _ in range(self.width):
                self._array[y].append(default_value)

    def get(self, column, row):
        return self._array[int(row)][int(column)]

    def set(self, column, row, value):
        self._array[int(row)][int(column)] = value

    def __str__(self):
        result = f"{self.__class__}[{self.width}, {self.height}] (Default value = '{self.default_value}') \n"
        result += "    "
        for x in range(self.width):
            result += f"{x} "
        result += "\n"
        for y in range(self.height):
            result += f"{y} "
            for x in range(self.width):
                result += f"{self.get(x, y)} "
            result += "\n"
        return result


class SquareArray2D(Array2D):
    def __init__(self, width: int, default_value=None):
        super().__init__(width, width, default_value)
