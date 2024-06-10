class My2DArray:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.data = [[None] * cols]* rows
    def __str__(self):
        return str(self.data)

array1 = My2DArray(3, 5)
array2 = My2DArray(5, 3)
print(str(array1))
